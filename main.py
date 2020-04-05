import sys
import time
import socket
from datetime import datetime, timezone
import ntplib
import threading
import pyuipc

from gui.gui import GUI
from shotwn import BasicTimeDelta
from shotwn import FlipFlop
from shotwn.settings import Settings
from shotwn.SingleInstance import SingleInstance

DEFAULT_SETTINGS = {
    "minimize_to_tray": True,
    "startup": {
        "auto_sync": False,
        "tray": False
    }
}

SIMULATORS = [
    "ANY",
    "MFS 98",
    "MFS 2000",
    "CFS 2",
    "CFS 1",
    "Reserved",
    "FS 2002",
    "FS 2004",
    "Flight Simulator X",
    "ESP",
    "Prepar3D",
    "Flight Simulator X64",
    "Prepar3D v4"
]


class OffsetSet:
    def __init__(self, offsets):
        self.offsets = offsets
        self.prepared_data = None
        self.latest_read = None
        self.prepare()

    def prepare(self):
        offsets_rough_dict = []
        for key, offset in self.offsets.items():
            offsets_rough_dict.append((offset[0], offset[1]))

        self.prepared_data = pyuipc.prepare_data(offsets_rough_dict, True)

    def read(self):
        offset_results = {}
        offset_values = pyuipc.read(self.prepared_data)

        for (key, offset), value in zip(self.offsets.items(), offset_values):
            offset_results[key] = value

        self.latest_read = offset_results
        return offset_results

    def write(self, offset, value):
        offset_raw = self.offsets[offset]
        pyuipc.write([(offset_raw[0], offset_raw[1], value)])


class FSSync:
    def __init__(self):
        self.offset_sets = []
        self.pyuipc_open = False
        self.opened_sim = None

    def reset(self):
        self.offset_sets = []
        self.close_pyuipc()

    def connect_pyuipc(self):
        if self.pyuipc_open:
            return self.pyuipc_open

        try:
            pyuipc.open(0)
        except pyuipc.FSUIPCException as exc:  # noqa: F841
            print(exc)
            return None

        sim_offset = self.create_offset_set({'SIM_VERSION': [0x3308, 'b']})
        result = sim_offset.read()
        self.pyuipc_open = result['SIM_VERSION']
        self.opened_sim = SIMULATORS[self.pyuipc_open]
        return True

    def close_pyuipc(self):
        self.pyuipc_open = False
        pyuipc.close()

    def create_offset_set(self, offsets):
        new_offset_set = OffsetSet(offsets)
        self.offset_sets.append(new_offset_set)
        return new_offset_set

    def read_all_offset_sets(self):
        for offset_set in self.offset_sets:
            offset_set.read()


class FSTimeSync:
    def __init__(self):
        self.si = SingleInstance(32092)
        self.settings = Settings('settings.json', DEFAULT_SETTINGS)
        self.fs_sync = FSSync()
        self.gui = GUI(self)
        self.mw_emit = self.gui.main_window.act.emit  # TODO: Switch from mw_emit to mw_act
        self.mw_act = self.gui.main_window_act
        self.time_offsets = None
        self.sync_run = False
        self.sync_thread = None
        self.time_run = False
        self.time_thread = None
        self.live_sync_enabled = False
        self.now_source = "S"
        self.ntp_client = ntplib.NTPClient()
        self.ntp_delta = None
        self.offset = BasicTimeDelta()

    def start(self):
        try:
            self.sync_thread = threading.Thread(None, self.sync_thread_runner, "Sync Thread", daemon=True)
            self.sync_thread.start()
            self.time_thread = threading.Thread(None, self.time_thread_loop, "Time Thread", daemon=True)
            self.time_thread.start()
            self.gui.start()  # locking
        finally:
            self.stop()

    def stop(self):
        self.sync_run = False
        self.time_run = False
        self.fs_sync.close_pyuipc()
        sys.exit(0)

    def get_now(self):
        if self.now_source == "NTP":
            try:
                if not self.ntp_delta:
                    response = self.ntp_client.request('pool.ntp.org')
                    print(time.ctime(response.tx_time))
                    self.ntp_delta = datetime.now(timezone.utc) - datetime.fromtimestamp(response.tx_time, timezone.utc)
                    print(self.ntp_delta)
                    self.gui.remove_message(1, 0)
                return datetime.utcnow() - self.ntp_delta
            except (ntplib.NTPException, socket.gaierror) as exc:
                self.gui.add_message(1, 0, "Can't reach NTP server.")
                print(exc)
                return datetime.utcnow()
        return datetime.utcnow()

    def switch_now_source(self):
        if self.now_source == "NTP":  # Will switch to S
            self.now_source = "S"
            self.mw_emit([self.gui.main_window.ui.utc_label.setText, "UTC.S"])
            self.mw_emit([self.gui.main_window.ui.utc_label.setToolTip, "UTC.S : Using System Time"])
        elif self.now_source == "S":  # Will switch to NTP
            self.ntp_delta = None  # Refresh NTP
            self.now_source = "NTP"
            self.mw_emit([self.gui.main_window.ui.utc_label.setText, "UTC.NTP"])
            self.mw_emit([self.gui.main_window.ui.utc_label.setToolTip, "UTC.NTP : Using Network Time Protocol, Online Time"])

        self.gui.remove_message(0, 1)  # Remove will sync message

    def time_thread_loop(self):
        self.time_run = True
        while self.time_run:
            now = self.get_now()
            self.mw_emit([self.gui.main_window.ui.real_time_hour.setText, "{:02d}".format(now.hour)])
            # self.mw_emit([self.gui.main_window.ui.real_time_seperator.setText, str(two_dots))
            self.mw_emit([self.gui.main_window.ui.real_time_minute.setText, "{:02d}".format(now.minute)])
            self.mw_emit([self.gui.main_window.ui.real_time_second.setText, "{:02d}".format(now.second)])
            self.mw_emit([self.gui.main_window.ui.real_date.setText, "{:02d}.{:02d}.{}".format(now.day, now.month, now.year)])
            # print(now)
            if bool(self.offset):
                offsetted_dt = self.offset + now
                self.gui.main_window_act(self.gui.main_window.ui.left_value.setText, f"{offsetted_dt.strftime('%H:%M | %d.%m.%Y')}")
            else:
                self.gui.main_window_act(self.gui.main_window.ui.left_value.setText, "")

            self.gui.main_window_act(self.gui.main_window.ui.left_status.setText, str(self.offset))
            time.sleep(0.5)

    def toggle_live_sync(self):
        print("toggle live sync")
        if not self.live_sync_enabled:
            self.enable_live_sync()
        else:
            self.disable_live_sync()

    def disable_live_sync(self):
        self.live_sync_enabled = False
        self.gui.remove_message(0, 1)  # Remove will sync message
        self.mw_emit([self.gui.main_window.ui.live_button.setIcon, self.gui.icons["sync_disabled"]])
        self.mw_emit([self.gui.main_window.ui.live_button.setToolTip, "Live Sync: Disabled"])

    def enable_live_sync(self):
        self.live_sync_enabled = True
        self.mw_emit([self.gui.main_window.ui.live_button.setIcon, self.gui.icons["sync"]])
        self.mw_emit([self.gui.main_window.ui.live_button.setToolTip, "Live Sync: Enabled"])

    def restart_sync_thread_runner(self, restart):
        self.mw_act(self.gui.main_window.ui.sim_label.setText, 'Waiting Simulator...')
        self.mw_act(self.gui.main_window.ui.sim_time_hour.setText, "")
        self.mw_act(self.gui.main_window.ui.sim_time_minute.setText, "")
        self.mw_act(self.gui.main_window.ui.sim_time_second.setText, "")
        self.mw_act(self.gui.main_window.ui.sim_time_second.setToolTip, "")
        self.mw_act(self.gui.main_window.ui.sim_time_seperator.setText, "")
        self.mw_act(self.gui.main_window.ui.sim_date.setText, "")
        self.fs_sync.reset()
        time.sleep(10)  # Sleep, make sure FSUIPC exits completely.
        self.sync_thread_runner(restart=restart + 1)

    def sync_thread_runner(self, restart=0):
        # Est. FSUIPC connection.
        # Try every 10 seconds.
        self.sync_run = True
        while self.sync_run:
            if not self.fs_sync.connect_pyuipc():
                # print(self.fs_sync.connect_pyuipc())
                # print("Cannot connect FSUIPC.")
                time.sleep(10)
                continue
            self.mw_act(self.gui.main_window.ui.sim_label.setText, self.fs_sync.opened_sim)
            break

        offsets = {
            "TIME_SECOND": [0x023A, "b"],
            "TIME_HOUR": [0x023B, "b"],
            "TIME_MINUTE": [0x023C, "b"],
            "DATE_DAY": [0x023D, "b"],
            "DATE_MONTH": [0x0242, "b"],
            "DATE_YEAR": [0x024A, "H"],
        }
        self.time_offsets = self.fs_sync.create_offset_set(offsets)

        try:
            self.sync_routine_loop()
        except (pyuipc.FSUIPCException, SystemError) as exc:
            if exc.errorCode == 12 or exc.errorCode == 13:
                print(f"Catched PYUIPC error, will restart. Code:{exc.errorCode}")
                self.restart_sync_thread_runner(restart=restart)

    def sync_routine_loop(self):
        two_dots = FlipFlop(":")
        while self.sync_run:
            data_delta = self.sync_sim()
            if not data_delta:
                continue

            data = data_delta[0]
            delta = data_delta[1]

            self.mw_emit([self.gui.main_window.ui.sim_time_hour.setText, "{:02d}".format(data["TIME_HOUR"])])
            self.mw_emit([self.gui.main_window.ui.sim_time_seperator.setText, str(two_dots)])
            self.mw_emit([self.gui.main_window.ui.sim_time_minute.setText, "{:02d}".format(data["TIME_MINUTE"])])
            self.mw_emit([self.gui.main_window.ui.sim_time_second.setText, "{:02d}".format(data["TIME_SECOND"])])
            self.mw_emit([self.gui.main_window.ui.sim_date.setText, "{:02d}.{:02d}.{}".format(data["DATE_DAY"], data["DATE_MONTH"], data["DATE_YEAR"])])
            self.mw_emit([self.gui.main_window.ui.sim_time_second.setToolTip, "ε: ±{}s Δ: {}s".format(30, int(delta))])
            # print(data)

            time.sleep(1)

    def sync_sim(self, force=False):
        """
        Returns initial data if no sync.
        Returns new data if there has been sync.
        """

        try:
            data = self.time_offsets.read()
            now = self.offset + self.get_now()
            time_from_data = datetime(data["DATE_YEAR"], data["DATE_MONTH"], data["DATE_DAY"], data["TIME_HOUR"], data["TIME_MINUTE"], second=data["TIME_SECOND"])
            delta = (now - time_from_data).total_seconds()
        except ValueError as exc:
            # ValueError generally thrown when FSUIPC is reporting year out of range.
            # Happens on scenerio screen.
            print(exc)
            time.sleep(0.5)
            return False

        if self.live_sync_enabled or force:
            if not self.fs_sync.pyuipc_open:
                return

            if abs(delta) > 30 or force:
                if force:
                    if data["TIME_SECOND"] - now.second > 20:
                        self.time_offsets.write("TIME_SECOND", 0)
                else:
                    if now.second > 3:
                        self.gui.add_message(0, 1, "Will Sync At: {:02d}:{:02d}z".format(now.hour, now.minute + 1))
                        return [data, delta]

                    self.time_offsets.write("TIME_SECOND", 0)

                print("DOING A ZULU TIME SYNC.")

                self.time_offsets.write("DATE_YEAR", now.year)
                self.time_offsets.write("DATE_MONTH", now.month)
                self.time_offsets.write("DATE_DAY", now.day)
                self.time_offsets.write("TIME_HOUR", now.hour)
                self.time_offsets.write("TIME_MINUTE", now.minute)

                self.gui.remove_message(0, 1)  # Remove will sync message
                self.gui.add_message(0, 2, "Last Sync: {:02d}:{:02d}:{:02d}z".format(now.hour, now.minute, now.second))
                return [self.time_offsets.read(), delta]  # Return fresh data

        return [data, delta]


if __name__ == "__main__":
    ROOT = FSTimeSync()
    ROOT.start()

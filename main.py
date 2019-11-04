import pyuipc
import time
import struct
from datetime import datetime


pyuipc.open(12)

def convert_bcd(data, length):
    """BCD to string"""
    bcd = ""
    for i in range(0, length):
        digit = chr(ord('0') + (data&0x0f))
        data >>= 4
        bcd = digit + bcd
    return bcd

def prepare_offsets(offsets):
    offsets_rough_dict = []
    for key, offset in offsets.items():
        offsets_rough_dict.append((offset[0], offset[1]))

    return pyuipc.prepare_data(offsets_rough_dict, True)

def format_radio_freq_to_string(freq):
    return """1{}.{}0""".format(hex(freq)[2:4], hex(freq)[4:6])

def format_string_to_radio_freq(string):
    return int("0x"+string[1:3] + string[4:6], 16)

def read_offsets(offsets_to_read):
    offset_results = {}
    offset_values = pyuipc.read(offsets_to_read)

    for (key, offset), value in zip(offsets.items(), offset_values):
        offset_results[key] = value
    
    return offset_results

"""
/**
 * Types:
 * - b: 1 byte unsigned char -> int
 * - c: 1 byte signed char -> int
 * - h: 2 byte signed short -> int
 * - H: 2 byte unsigned short -> int
 * - d: 4 byte signed integer -> int
 * - u: 4 byte unsigned integer -> long
 * - l: 8 byte signed long long -> long
 * - L: 8 byte unsigned long long -> long
 * - f: 8 byte double -> double
 */
 """
offsets = {
    "TIME_HOUR": [0x023B, "b"],
    "TIME_MINUTE": [0x023C, "b"]
}

offsets_to_read = prepare_offsets(offsets)

print("Script will check time every 10 seconds. After first sync you can close this window.")
while True:
    curr_offsets = read_offsets(offsets_to_read)
    now = datetime.utcnow()
    print("Current Time: {}:{}z Simulator Time: {}:{}z".format(now.hour, now.minute, curr_offsets["TIME_HOUR"], curr_offsets["TIME_MINUTE"]))

    if curr_offsets["TIME_HOUR"] != now.hour or curr_offsets["TIME_MINUTE"] > now.minute + 1 or curr_offsets["TIME_MINUTE"] < now.minute - 1:
        print("DOING A ZULU TIME SYNC.")
        pyuipc.write([(offsets["TIME_HOUR"][0], offsets["TIME_HOUR"][1], now.hour)])
        pyuipc.write([(offsets["TIME_MINUTE"][0], offsets["TIME_MINUTE"][1], now.minute)])

    # pyuipc.write([(offsets["RADIOSWAP"][0], offsets["RADIOSWAP"][1],8)])
    time.sleep(10)
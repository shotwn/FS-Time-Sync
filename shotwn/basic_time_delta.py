from datetime import datetime, timedelta
# from dateutil.relativedelta import relativedelta
from calendar import monthrange


class BasicTimeDelta:
    def __init__(self, *args, **kwargs):
        self.steps = ["minute", "hour", "day", "month", "year"]
        self.max_step = [60, 24, 32, 13, 3000]
        self.min_step = [0, 0, 1, 1, 0]
        self.inner_delta_day = 0

        for (i, var) in enumerate(self.steps):
            try:
                setattr(self, var, args[i])
            except IndexError:
                setattr(self, var, kwargs.get(var, 0))

    def __add__(self, param1: datetime, override_max_month=None) -> datetime:
        new = {}
        next_value = 0

        for (i, var) in enumerate(self.steps):
            if var == "day":
                new["day"] = param1.day
                continue

            new_value = getattr(param1, var) + getattr(self, var) + next_value
            (new_value, next_value) = self.overflow(self.min_step[i], self.max_step[i], new_value)

            new[var] = new_value

        # print(new)
        days_to_add = getattr(self, "day", 0)
        date_wo_days = datetime(**new)

        return date_wo_days + timedelta(days=days_to_add)

    def __str__(self):
        stringified = []
        for step in self.steps:
            value = getattr(self, step, 0)
            if value != 0:
                if value > 0:
                    stringified.append(f"+{value} {step}s")
                else:
                    stringified.append(f"{value} {step}s")

        if stringified:
            return ', '.join(stringified)
        return ''

    def __bool__(self):
        for step in self.steps:
            if getattr(self, step, 0) != 0:
                break
        else:
            return False
        return True

    def overflow(self, mini, maxi, var):
        normalized = maxi - mini
        var = var - mini
        overflow = var // normalized
        value = var % normalized + mini
        return (value, overflow)

    def ingest(self, param1: datetime, param2: datetime):
        for var in self.steps:
            ingested = getattr(param1, var) - getattr(param2, var)
            setattr(self, var, ingested)
        # print(self)
        return self

from datetime import datetime, timedelta

class MyDate():
    def __init__(self, num=1):
        self._num = num
        self.col_headers = []
        week_day = datetime.weekday(datetime.now())
        if self._num == 1:
            deltaToSun = 7 - week_day
        else:
            deltaToSun = 14 - week_day
        # יימי השבוע
        days_of_week = [' yom a', 'yom b', 'yom 3', 'yom 4', 'day 5', 'shishi', 'shabat']
        for i in range(7):
            dday = (datetime.now() + timedelta(days=deltaToSun + i))
            month = dday.strftime("%m")
            day = dday.strftime("%d")
            date_time = dday.strftime("%d/%m")
            self.col_headers.append(days_of_week[i] + ' ' + date_time)
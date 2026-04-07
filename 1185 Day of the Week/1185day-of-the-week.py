from datetime import date

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        day1 = date(1971, 1, 1)
        day2 = date(year, month, day)
        d = day2 - day1
        days = d.days
        ls = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        
        day = ls[days % 7]
        
        return day
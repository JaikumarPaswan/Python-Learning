#Q2

days = {"sun": 0,
        "mon": 1,
        "tue": 2,
        "wed": 3,
        "thu": 4,
        "fri": 5,
        "sat": 6
        }

def NumOfSundays(day, N):
    num = days[day] + N
    return num//7

print(NumOfSundays("thu", 13))
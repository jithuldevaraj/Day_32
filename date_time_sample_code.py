import datetime as dt

now = dt.datetime.now()   # <class 'datetime.datetime'>

print(f"Year : {now.year}")                              # Year : 2026
print(f"Month : {now.month}")                            # Month : 7
print(f"Day : {now.day}")                                # Day : 18
print(f"Time : {now.hour}:{now.minute}:{now.second}")    #  Time : 11:14:56
print(f"Week : {now.weekday()}")                         # Week : 5

date_of_birth = dt.datetime(year=1996, month=10, day=19)
print(date_of_birth)                                     # 1996-10-19 00:00:00








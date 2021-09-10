import datetime

#date
today = datetime.date.today()
print(today)

my_birthday = datetime.date(2005,10,26)
days_since_birth = (today - my_birthday).days

print(int(days_since_birth))
print((datetime.date.today()-datetime.date(2005,10,26)).days)

print(today + datetime.timedelta(days=10))

if today.day == my_birthday.day and today.month == my_birthday.month :
    print('happy birthday')
else :
    print('mhm')

#time
time_n = datetime.time(23,59,59,999999)
print(time_n)
print(datetime.time)

#datetime
datetime_ehe = datetime.datetime(2010,10,10,10,10,10,10)
print(datetime_ehe)
delta = datetime.timedelta(hours=10)
print(datetime.datetime.now())
print(datetime.datetime.now()+ delta)

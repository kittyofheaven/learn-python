import datetime
import pytz

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

print(' ')

datetime_today = datetime.datetime.now(tz=pytz.UTC)
print(datetime_today)
datetime_jakarta = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
print(datetime_jakarta)

#for tz in pytz.all_timezones :
 #   print (tz) #for print all time zone

#string formating with dates strftime
#2012-12-12 -> September 12, 2012
stringtime = datetime_jakarta.strftime('%B %d, %Y')#%B buat bulan %d buat hari %Y buat tahun
print(stringtime)
print(type(stringtime))

#string parsing with dates strptime
print(datetime.datetime.strptime('March 09, 2019', ('%B %d, %Y')))
print(type((datetime.datetime.strptime('March 09, 2019', ('%B %d, %Y')))))
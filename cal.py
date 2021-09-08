import calendar

#calendar
#calendar buat panggil library trus week header buat panggil hari" gitu trus (dalam kurung isinya berapa huruf yg ditulis)
print(calendar.weekheader(3))
print(calendar.month(2021, 1, w=3))
#jalanin app klo mau tau hasilnya, keren si

#ini fiungsi  bentuk matrix
print(calendar.monthcalendar(2021, 1))

#ini whole year
print(calendar.calendar(2021, w=3))

#print dalam bentuk matrix
hari_ini = calendar.weekday(2021, 7 ,18)
print(hari_ini)

#melihat kabisat atau engga
kabisat = calendar.isleap(2021)
print(kabisat)

#how many leap days
berapa_kabisat = calendar.leapdays(1999, 2019)
print(berapa_kabisat)

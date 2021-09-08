#pake ini klo mau dictionary order
from collections import OrderedDict


#dictionary
#pake {}

groceries = {'bananas': 5, 'orange': 3, 'apple': 'apel itu enak'}
print(groceries['bananas'])#kita print keynya nanti yang keluar hasil yang ditulis di atas

#fungsi dibawah ini jika tidak ditemukan apel maka akan mengahsilkan none, bukan error
#bedanya sama get biasa klo get biasa klo gaada bakal hasilin error
print(groceries.get('apel'))


yang_dicari = "apple"
if groceries.get(yang_dicari) == None : 
    print('tidak di temukan', yang_dicari)
else :
    print('ditemukan', yang_dicari)
    print(groceries.get('apple'))


#kita bisa buat contact database dengan ini juga
contacts = {
    'hazel': ('Hazel', '085790826168', 'hazelhandrata@gmail.com') ,
    'joe': ('Joe', '085712312323', 'joeuedan@gmail.com'),
    'edward':('Edward', '08123476523', 'Edwardserigala@gmail.com') ,
    'james' : ('James', '08123497697', 'Jamesggantenganakbaik@gmail.com'),
}
print(contacts['james'])
print(contacts.get('hazel')[1])

#bisa buat dictionary in dictionary juga
kontak = {
    'hazel': {'name': 'Hazel','numbers':'085790826168','email':'hazelhandrata@gmail.com'} ,
    'joe': {'names': 'Joe','numbers':'085712312323','email':'joeuedan@gmail.com'},
    'edward':{'names':'Edward','numbers':'08123476523','email':'Edwardserigala@gmail.com'},
}
print(kontak.get('hazel').get('email'))
#bisa buat dictionary didalam dictionary didalam dictionary lagi
intelegence = {
    'hazel' : {
        'names': {
            'name_1': 'hazel',
            'name_2': 'Masiluy',
            'name_3': 'Kitty of Heaven',
        },
        'numbers': {
            'numbers_1': '085790826168',
            'numbers_2': '08576865657',
        },
        'emails': {
        'emails_1': 'hazelhandrata@gmail.com',
        'emails_2': 'echoind1945@gmail.com'
        }
    },
    'Joe' : {
        'names': {
            'name_1': 'Joe',
            'name_2': 'Mama',
            'name_3': 'Mas be Joe',
        },
        'numbers': {
            'numbers_1': '081290826168',
            'numbers_2': '08126865657',
        },
        'emails':{
        'emails_1': 'joeuedan@gmail.com',
        'emails_2': 'joemama@gmail.com'
        }
    }
} 
#mau print yang mana mas?, mau print yang email keduanya joe
print(intelegence.get('Joe').get('emails').get('emails_2'))
#mau delete emails hazel 2
intelegence.get('hazel').get('emails').pop('emails_2')
print(intelegence.get('hazel').get('emails').get('emails_2'))

#aga ribet tapi gapapa lah worth it 

#beberapa fungsi tambahan yang berguna

#dict.items()  merubah dict menjadi tuple berisikan keys sama values
#dict.keys() merubah dict menjadi tuple berisikan keys only
#dict.value() merubah dict menjadi tuple berisika values only

dikte = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5
}

print(dikte.items())
print(dikte.keys())
print(dikte.values())
#untuk delete dict
dikte.pop('a')
print(dikte)
dikte.popitem() #buat hapus last item
print(dikte)

#cara add ke dictionary
dikte['key'] = 4 
print(dikte)

#buat clear dictionary
dikte.clear()
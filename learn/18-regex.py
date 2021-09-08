#regex start coding
#regular expresion
import re #import the regex library

#create regular expression pattern
text = "i have random string on this text mfs"
pattern = re.compile("random string") #re sifatnya case sensitive
result = pattern.search(text)
pattern = re.compile("Random String") #re sifatnya case sensitive dan klo ga ketemu resultnya bakal 'none'
result = pattern.search(text)

print(result)
#jadi fungsinya kaya buat search pattern yg ada dalam text ber paragraf gitulah 

pattern = re.compile("[aiueo]") #klo dikasih [] dia jadi nyari setiap chara yg disitu satu-satu dan resultnya diambil yg ketemu duluan
result = pattern.search(text)

print(result)

#what u can do
pattern = re.compile("[a-c]") #sama aja kaya pattern = re.compile("[abc]") tanda itu artinya 'a sampai c'

text = "rando0090829284m string"
pattern = re.compile("[a-z0-9]+") #so basicly dia bakal nyari a-z dan 0-9 dan tanda "+" diakhir itu buat nyatain
#klo dia bisa search huruf apapun dan masukin ke result sampai dia nemu satu chara yg ga sesuai dan dia akan terminate
#jadi seharusnya dia cuma print sampe rando0090829284m karena kita ga include ' ' space di charanya, coba aja print
result = pattern.search(text)
print (result)

pattern = re.compile("[a-z 0-9]+") #ini kita tambahin ' ' jadi ada chara space di search juga, harusnya ke print semuanya
result = pattern.search(text)
print (result)

#ini contohnya kegunaan regex dalam search email
email_text = "randome string and i love you but you love someone else foolpeople@email.com are makes me so mad af madman@email.com"
print(re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9.]+").search(email_text)) #males pake variable" bullshit
#"+" disini bukan penjumlahan tapi simbol buat dia bisa cari sebanyak mungkin sampe nemu chara yang ga sesuai
#nah kan biasanya email bentuknya awdwdabwd@eaawd.com jadi 
#[a-zA-Z0-9]+ ini nyataim klo kita bisa nyari chara didepan @ sebanyak apapun dan klo dibatasi selain dari "a-zA-Z0-9" maka stop
#@ nyatain harus kata yang ada @ nya
#[a-zA-Z0-9.]+ nyatain klo kita bisa nyari chara di belakang @ sebanyak apapun dan klo dibatasi selain dari "a-zA-Z0-9." maka stop
print(re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+").search(email_text)) #bisa kaya gini juga terserahmu cuk
#sekian regex

#imma head out
#imma sleep now

#nah sekarang gimana klo isi textnya itu
random_text = "<>[]+"
#sedangkan itu digunain buat syntax kaya gini misalnya
#print(re.compile("[]+").search(random_text)) #nah error kan klo dijalanin

#jadi penyelesaiannya harus add \ didepannya biar dianggap string bukan syntax
print(re.compile("\[\]\+").search(random_text)) #gituh okeh

#nah gimana klo ada multiple email adress
print(re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+").search(email_text)) #ini kan cuma buat 1 kalimat doang
print(re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+").findall(email_text))#nah function findall ini juaranya okeh
#yey baka yarou
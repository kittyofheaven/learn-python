#file io membuat input outpot file

file = open('21-file_io.txt', 'w') 
"""
w = write mode & overwrite mode + create the file if the file hasnt been created yet
r = read mode 
a =  appending mode / insert data on last line
r+ = write and read mode
"""

file.write('this is me writing using file io method')
file.write('\nsecond try')
file.write('\nthird try')
file.write('\nfourth try')
file.close() #setelah open langsung close unuk ngesave

print(open('21-file_io.txt', 'r').read()) #klo baca doang gausah di close
print(open('21-file_io.txt', 'r').read(10)) #10 adalah banyak chara dari awal
print(open('21-file_io.txt', 'r').readline()) #buat read line berapa
open('21-file_io.txt', 'r').close()

#this is append mode
open('21-file_io.txt', 'a').write('\nthis last line created with append method')

print(open('21-file_io.txt', 'r').read())
open('21-file_io.txt', 'r').close()
open('21-file_io.txt', 'a').close()
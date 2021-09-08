t = (1,2,3,4,5,6,7,8,9)
#tuple seperti list tapi dengan tanda kurung, bedanya dengan list 
#tuple tidak dapat diubah diganti dihapus dan lebih aman

credit_card = (123123123121, "Hazel Handrata", '10/26', "alamat rumah b3/18", 123)
credit_card1 = (123126723121, "Ajel Handrata", '8/21', "alamat rumah 67", 321)

credit_cards = [credit_card, credit_card1]

print(credit_cards)

person_1 = ('hazel', 15, 'male')
person_2 = ('ajel', 17, 'male')


people = [person_1, person_2]

print(people)
for name, age, gender in people :
    print()
    print(name)
    print(age)
    print(gender) 

list1 = [1,2,3,4,5,]
list2 = ['one', 'two', 'three', 'four', 'five', 'six'] #if the list have diferent length then the 6 one will be ignored (chunked)

zipped = list(zip(list1, list2))
print(zipped)

list3 = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'), (6, 'six'), (7, 'seven')]
#print(list3)

unzipped =list(zip(*list3))# add asterisk to reverse it (*) and it will unzip
#print(unzipped)
list_unzip1 = list(unzipped[0])
list_unzip2 = list(unzipped[1])


for unzip in unzipped :
    print(list(unzip))

#for (l1, l2) in zip(list1,list2):
 #   print(l1)
  #  print(l2)

items = ['apple', 'book', 'sugar', 'oil']
counts = [3, 6, 4]
prices = [0.99, 1, 0.25, 0.50]
sentences = []
#cari tau apa fungsi (a,b,c) oke besok
for (item, count, price) in zip(items,counts,prices):
    sentence = 'I bought '+ str(count) + ' ' + str(item) + 's at '+ str(price) +' cents'
    sentences.append(sentence)
print(sentences)
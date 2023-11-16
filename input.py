name = input('Input Your Name:  ')
age= input('Input Your age: ')
print('Your name is '   + name  + 'and you are ' + age + 'Years old')
##again using string and integer




 ####building a simple word replacement program##
sentence = input('Enter your sentence')
print('your sentence is: ' + sentence)
word1 = input('Enter the word to replace : ')
word2 =input('Enter the word to replace it with : ')
print(sentence.replace(word1, word2)) 

#####LISTS INN PYTHON  DIFFERENT VALUES 
countries = ['United Kingdom' ,'Ghana','Kenya ','America']
print(countries)
print(countries[0])
print(countries[3][0])
print(countries[1:])
print(countries[3:])

print(type(countries))
name = 'Limo'
print(type(name))
countries[0]  = 'Uganda '
countries[3]  = ' Namibia'
print(countries)

print(countries[-1])
print(len(countries))
print(type(countries))
print(type(list))


##LIST METHODS## FUNCTIONS ON PYTHON

list1 = [1,2,3,4,6]
list2 = ['banana ','mangoes','mango','Oranges']
list1.extend(list2)
print(list2)
list2.append('cherry')
list2.remove('banana')
###deleting a list

list2.clear()
###index no..of Mnango 
print(list2.index('mango'))
#####reversing
list1 = [1,2,3,4,6]
list2 = ['banana ','mangoes','mango','Oranges']
list2.reverse()
print(list2)
###deleting 

list1 = [1,2,3,4,6]
list2 = ['banana ','mangoes','mango','Oranges']
del list2
print(list2)

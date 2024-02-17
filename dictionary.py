numbers = [12,56,98,78,56,12,6,98]

person1 = ['Kala chan','Kalipur',23,'student']

#key value
#dictionary
#overlap with set
#{key:value,key:value,}
person={'name':'Kala pakhi','address':'Kalipur','age':23,'job':'bekar'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())
person['language']='python'
person['name']='Sada pakhi'
del person['age']
print(person)

for key,value in person.items():
    print(key,value)


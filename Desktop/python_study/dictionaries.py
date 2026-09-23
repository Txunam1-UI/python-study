
student1={
'name':'mike',
'age':21,
'country':'kenya',
'gender':'male',
'name':'alex'
}
print(type(student1))
print(student1['name'])

#add and update properties
#add

student1['city']='nairobi'
student1['county']='kisumu'
print(student1)

#update
student1['age']=30
print(student1)

student1['name']='txunami'
student1['country']='Egypt'
print(student1)
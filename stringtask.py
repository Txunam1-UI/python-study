#Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 

name1="  JOHn  "
name1=name1.strip()
name1=name1.lower()
print(name1)

sentence_one = "The Dog Breed is German Shepherd "
sentence_one=sentence_one.replace('The Dog Breed is German Shepherd','Breed is German')
print(sentence_one)

sentence_two = 'Defeats for the Clinton forces, this was her moment of triumph'
sentence_two=sentence_two.replace('Defeats for the Clinton forces, this was her moment of triumph','Clinton Forces')
print(sentence_two)

text='The lazy dog; ran so fast; it hit the wall.'
text=text.split(';')
print(text)
print(len(text))

first_name="Joh.n" 
last_name="Do,e" 
first_name=first_name.replace('Joh.n','John')
last_name=last_name.replace('Do,e','Doe')
full_name=first_name+' '+last_name
print(full_name)

r = '["E","W","C"]'
r=r.replace('["E","W","C"]' ,'EWC')
print(r)
addressBook = {"David": {"address" : "555 Home St", "phone" : "4045551234", 
                          "email" : "david@david.com"},
               "Lucy" : {"address" : "555 Home St", "phone" : "4045555678", 
                         "email" : "lucy@lucy.com"},
               "Dana" : {"address" : "123 Here Rd", "phone" : "4045559101", 
                         "email" : "dana@dana.net"}}
print('David info:', addressBook['David'])
print('Dana phone:', addressBook['Dana']['phone'])
print('--------------------------------------------------------------------')

ANSWER_KEY = {"1" : "A", "2" : "B", "3" : "C", "4" : "D", "5" : "A"}

students={}
students["David"] = {"1" : "A", "2" : "B", "3" : "A", "4" : "B", "5" : "C"}
students["Terra"] = {"1" : "A", "2" : "B", "3" : "C", "4" : "D", "5" : "A"}
students["Lugos"] = {"1" : "A", "2" : "C", "3" : "C", "4" : "D", "5" : "A"}


for student, answers in students.items():
    grade = 0
    for question, answer in answers.items():
        if answer == ANSWER_KEY[question]:
            grade += 1
    students[student]['grade'] = grade

print(students)
for student, answers in students.items():
    print('{}: {};'.format(student, answers['grade']), end=' ')

print('--------------------------------------------------------')
my_str = 'This is my cat. My cat is very cute.'
print(my_str)
print('---------------------------------------------------------')
my_str = my_str.replace(".", "")
print(my_str)
print('---------------------------------------------------------')
my_str = my_str.replace(",", "")
my_str = my_str.replace("''", "")
my_str = my_str.lower()
my_split_str = my_str.split()
print(my_str)
print(my_split_str)
word_dict = {}
for word in my_split_str:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
print(word_dict)
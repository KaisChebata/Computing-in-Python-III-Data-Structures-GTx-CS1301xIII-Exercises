little_text = """
This is the string whose words we would like to count. \
This string contains some repeated words, as well as some unique words. \
It contains punctuation, and it contains words that are capitalized in different ways. \
If the method we write runs correctly, it will count 4 instances of the word 'it', \
3 instances of the word 'this', and 3 instances of the word 'count'.
"""
print('counting words in string or text using dictionary .....')
print('little_text before cleaning and spliting to list of words....')
print(little_text)

# cleaning little_text from punctuation

for punc in ('.', ',', "'"):
    little_text = little_text.replace(punc, '')
# make all lower case and split little_text to list of words
little_text_list = little_text.lower().split()
print('little_text_list ->', little_text_list)

words_dictionary = {}

for word in little_text_list:
    # if word in words_dictionary:
    #     words_dictionary[word] += 1
    # else:
    #     words_dictionary[word] = 1
    words_dictionary[word] = words_dictionary.get(word, 0) + 1

print(words_dictionary)
print('-------------------------------------------------------')
print('seating chart for wedding example using dictionary ....')

seatingChart = {"David" : 3, "Lucy" : 3, "Dana" : 2,
                "Addison" : 2, "Vrushali" : 1, "Bilbo" : 3,
                "Sara" : 1, "Lugos" : 1, "Mireia" : 1,
                "Partha" : 2, "Venijamin" : 1, "Terra" : 2, 
                "Tryphon" : 3, "Gevorg" : 1, "Raza" : 3,
                "Rein" : 3, "Sofia" : 2, "Perle" : 2}
# print the table for the name:
for name, table in seatingChart.items():
    print('{} is at table #{}'.format(name, table))
print()

# print all guests on each table

for i in range(1, 4):
    print('the guests at table {}# are:'.format(i), sep='', end=' ')
    for name, table in seatingChart.items():
        if i == table:
            print(name, end=' ')
    print()

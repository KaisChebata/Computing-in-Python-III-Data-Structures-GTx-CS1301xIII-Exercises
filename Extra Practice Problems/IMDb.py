#Write a function called imdb_dictionary. imdb_dictionary
#should have one parameter, a string representing a
#filename.
#
#On each row of the file will be a performer's name, then
#a semicolon, then a comma-separated list of movies the have
#been in. For example, one file's contents could be:
#
#Robert Downey Jr.; Avengers: Infinity War, Sherlock Holmes 3, Spider-Man: Homecoming
#Scarlett Johansson; Avengers: Infinity War, Isle of Dogs, Ghost in the Shell
#Elizabeth Olsen; Avengers: Infinity War, Kodachrome, Wind River, Ingrid Goes West
#
#You may assume that the only semi-colon will be after the
#performer's name, and that there will be no commas in the
#movie titles.
#
#Return a dictionary where the keys are each actor's name,
#and the values are alphabetically-sorted lists of the movies
#they have been in. For example, if imdb_dictionary was called
#on the file above, the output would be:
#{"Robert Downey Jr.": ["Avengers: Infinity War", "Sherlock Holmes 3", "Spider-Man: Homecoming"],
#"Scarlett Johansson": ["Avengers: Infinity War", "Ghost in the Shell", "Isle of Dogs"],
#Elizabeth Olsen": ["Avengers: Infinity War", "Ingrid Goes West", "Kodachrome", "Wind River"]}
#
#Make sure the list of movies is sorted alphabetically. Don't
#worry about the order the keys (names) appear in the dictionary.


#Add your code here!



#Below are some lines of code that will test your function.
#You can change the contents of some_performers.txt from
#the dropdown in the top left to test other inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{"Robert Downey Jr.": ["Avengers: Infinity War", "Sherlock Holmes 3", "Spider-Man: Homecoming"], "Scarlett Johansson": ["Avengers: Infinity War", "Ghost in the Shell", "Isle of Dogs"], Elizabeth Olsen": ["Avengers: Infinity War", "Ingrid Goes West", "Kodachrome", "Wind River"]}
print(imdb_dictionary("some_performers.txt"))


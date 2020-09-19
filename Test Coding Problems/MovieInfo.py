#Write a function called write_movie_info. write_movie_info
#will take as input two parameters: a string and a
#dictionary.
#
#The string will represent the filename to which to write.
#
#The keys in the dictionary will be strings representing
#movie titles. The values in the dictionary will be lists
#of strings representing performers in the corresponding
#movie.
#
#write_movie_info should write the list of movies to the file
#given by the filename using the following format:
#
# Title: Actor 1, Actor 2, Actor 3, etc.
#
#The movies and the actor names should be sorted
#alphabetically.
#
#So, for this dictionary:
#
# {"Chocolat": ["Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"],
#  "Skyfall": ["Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris"]}
#
#The file printed would look like this:
#
# Chocolat: Alfred Molina, Johnny Depp, Judi Dench, Juliette Binoche
# Skyfall: Daniel Craig, Javier Bardem, Judi Dench, Naomie Harris
#
#HINT: the keys() method of a Dictionary will return a list
#of the dictionary's keys. So, to get a sorted list of a_dict's
#keys, you could call key_list = a_dict.keys(), then call 
#key_list.sort().


#Write your function here!

def write_movie_info(file_name, movies_dictionary):
    # solution 1
    file_writer = open(file_name, 'w')
    for title in sorted(movies_dictionary):
        # print(f"{title}: {', '.join(sorted(movies_dictionary[title]))}", file=file_writer)
        file_writer.write(f"{title}: {', '.join(sorted(movies_dictionary[title]))}\n")
    file_writer.close()

    # solution 2
    # file = open(file_name, "w")
    # for movie in sorted (movies_dictionary):
    #     file.write(movie + ": ")
    #     movies_dictionary[movie].sort()
    #     for i in range(0, len(movies_dictionary[movie]) - 1):
    #         file.write(movies_dictionary[movie][i] + ", ")
    #     file.write(movies_dictionary[movie][len(movies_dictionary[movie]) - 1] + "\n")
    # file.close()
    # return

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print nothing -- however, it should write the same contents
#as Sample.txt to Test.txt.
movies = {"Chocolat": ["Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"], "Skyfall": ["Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris"]}
write_movie_info(r"Test Coding Problems\\Test.txt", movies)

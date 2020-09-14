"""
The Short Version: Write a function that makes sure these files are correctly-formatted.

The Long Version: One of the reasons that filetypes work is that 
everyone agrees how they are structured. 
A ".png" file, for example, always contains "PNG" in the first four characters 
to assure the viewer that the file is actually a png. 
If these standards were not set, 
it would be hard to write programs that know how to open and read the file.

Let’s define a new filetype called ".cs1301". 
In this file, every line should be structured like so:

number assignment_name grade total weight

In this file, each component will meet the following description:

    - number: an integer-like value of the assignment number
    - assignment_name: a string value of the assignment name
    - grade: an integer-like value of a student’s grade
    - total: an integer-like value of the total possible number of points
    - weight: a float-like value ranging from 0 to 1 representing 
    	the percent of the student’s grade this assignment is worth. 
    	All the weights should add up to 1.

Each component should be separated with exactly one space. 
A good sample file is available to view as "sample.cs1301".

Write a function called format_checker that accepts a filename and returns True if the file contents accurately conform to the described format. Otherwise the function should return False. In other words, it should return True if:

    Each line has five elements separated by spaces, AND
    The first, third, and fourth elements are integers, AND
    The fifth element is a decimal number, AND
    All the fifth elements add to 1.

You can make changes to test.cs1301 to test your function, or test it with sample.cs1301. Right now, running it on sample.cs1301 should return True, and on test.cs1301 should return False.

Hint 1: .split() will likely help separate each line into its components.
Hint 2: .split() returns a list. So, if you were to do something like say splitLine = line.split(), then splitLine[0] would give the first item, splitLine[1] would give the second item, etc.
Hint 3: Remember, the moment you find a single place where the file doesn't conform to the structure, then you can return False. Then, if you reach the end of the file, then it must be correct and you should return True.
"""


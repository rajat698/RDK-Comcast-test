# RDK-Comcast-test

Make sure you have Python and C languages installed on your system.

## Activity 1

Activity 1 - Weather app is made in python. It is located in the folder named 'Activity 1'.

1. Main application is in main.py, while timeFormatter.py contains a helper function to format time.
2. Application runs on the command line, simply run ```cd /location/to/Activity 1 folder``` and ```python main.py``` in the terminal to run the application.
3. The features of the application are as follow :-
     
    1. Enter name of a city to see the current weather
    2. Press 1 to add a city to favourites list
    3. Press 2 to display favourites
    4. Press 3 to remove a city from favourites
    5. Enter 'exit' to exit the application
              
    Note - Imperial system is used for units

## Activity 2

Activity 2 is done in C. It has a bunch of functions and comes with predefined test cases.

# Instructions
The file is present in main.c in the folder named 'Activity 2'
Either compile the file in your IDE or run it in the terminal:
1. ```cd /location/to/Activity 2 folder```
2. ```gcc main.c -o main```
3. ```./main```

It has following functions:-

1. split function to split the array around the last element (used for quick sort).
2. -- sort function to sort the array. It uses quick sort.
3. -- sortAndFindMedian as described in the pseudo code. This function does not have empty array exception as it wasn't given in the pseudo code. Also, length is passed as a parameter, because that is a good practice in C.
4. showArray function to print the array.
5. testCase function to run a test case.
6. main driver function.
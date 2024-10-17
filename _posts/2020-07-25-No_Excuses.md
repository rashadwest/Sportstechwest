---
layout: post
title: "No Excuses"
thumbnail: "assets/img/blog-img/Screen Shot 2020-08-30 at 9.37.28 PM.webp"
---
T
he code below was right and I needed no hint and it all made sense.  I am getting somewhere. Stick with it. 

```
 # Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
```

Im not sure what they are talking about with this problem set.  I am looking to learn more about this now.  

Maybe you already know the name of a Python function, but you still have to figure out how to use it. Ironically, you have to ask for information about a function with another function: help(). In IPython specifically, you can also use ? before the function name.

To get help on the max() function, for example, you can use one of these calls:

help(max)
?max
Use the Shell on the right to open up the documentation on complex(). Which of the following statements is true?

Possible Answers
complex() takes exactly two arguments: real and [, imag].

complex() takes two arguments: real and imag. Both these arguments are required.

complex() takes two arguments: real and imag. real is a required argument, imag is an optional argument.

complex() takes two arguments: real and imag. If you don't specify imag, it is set to 1 by Python.


I figured most of this problem set out but I struggle with how to sort full_sorted.  I had to take the hind and then the answer for the first time in a while. 

-asking
Multiple arguments

In the previous exercise, the square brackets around imag in the documentation showed us that the imag argument is optional. But Python also uses a different way to tell users about arguments being optional.

Have a look at the documentation of sorted() by typing help(sorted) in the IPython Shell.

You'll see that sorted() takes three arguments: iterable, key and reverse.

key=None means that if you don't specify the key argument, it will be None. reverse=False means that if you don't specify the reverse argument, it will be False.

In this exercise, you'll only have to specify iterable and reverse, not key. The first input you pass to sorted() will be matched to the iterable argument, but what about the second input? To tell Python you want to specify reverse without changing anything about key, you can use =:

sorted(___, reverse = ___)
Two lists have been created for you on the right. Can you paste them together and sort them in descending order?

Note: For now, we can understand an iterable as being any collection of objects, e.g. a List. 

- answer
```
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)

# Print out full_sorted
print(full_sorted)
```

What I thought the answer was. 
```
In [4]: # string to experiment with: place
        place = "poolhouse"
        
        # Use upper() on place: place_up
        place_up = upper(place)
        
        # Print out place and place_up
        print(place)
        print(place_up)
        
        # Print out the number of o's in place
        count(place)
```        

What the answer was.  I am not sure about the place.upper().  When I went to help() I did not see that with upper. 
```
# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))
```

---
layout: post
title: "First week of Python"
thumbnail: "assets/img/blog-img/Screen Shot 2020-08-30 at 9.37.28 PM.webp"
---

# 1st week of Python
## Learning the basics

Operation with other types 

I struggled with this example. The instructions got me confused.  I have listed them below.

Calculate the product of savings and growth_multiplier. Store the result in year1.
- To me I thought to put the code below for this one so I got this right.
```
growth_multipler * savings = year1
```
What do you think the resulting type will be? Find out by printing out the type of year1.
- I had no idea what to do here because we never talked about this type formula.  How was I supposed to figure this out.  I think I will try to use stack overflow next time.

Calculate the sum of desc and desc and store the result in a new variable doubledesc.
- This was pretty easy

Print out doubledesc. Did you expect this?
- I forgot how to print.  Now I know it is like below. 
```
print()
```

This is the solution below

```savings = 100
growth_multiplier = 1.1
desc = "compound interest"

# Assign product of savings and growth_multiplier to year1
year1 = savings * growth_multiplier

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc

# Print out doubledesc
print(doubledesc)
```

Type Conversion 
- Using + operator to paste together 2 strings can be very useful 

All of these can be used to do type conversion.
str() 
float()
int()

I didnt understand how to type convert in the problem they game me. 
- I am still working on the problem. 

```
v# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"


# Convert pi_string into float: pi_float
pi_float = float(pi_string)
```

I got it right!  I used the hint because I did not understand how to create this at first glance. 
- Use float() on pi_string and store the result in pi_float.

I ended up prining out with the code above and it worked!

```
In [11]: I started with $100 and now have $194.87171000000012. Awesome!

<script.py> output:
    I started with $100 and now have $194.87171000000012. Awesome!
```
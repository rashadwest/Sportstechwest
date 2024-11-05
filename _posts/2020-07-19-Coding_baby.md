---
layout: post
title: "Coding baby"
thumbnail: "assets/img/blog-img/Screen Shot 2020-08-30 at 9.37.28 PM.webp"
---

# Being able to get through errors 

I have been running into errors lately and instead of getting frustrated and going off and doing something else and then coming back I am going to 
try to figure it out myself more now.  I see that it is always simple mistakes.  

![Error]({{site.url}}{{site.baseurl}}/assets/img/blog-img/Screen%20Shot%202020-07-19%20at%202.10.55%20PM.webp)


Sometimes it is the simple things like the word areas and not area. 
![Solution]({{site.url}}{{site.baseurl}}/assets/img/blog-img/Screen%20Shot%202020-07-19%20at%202.10.55%20PM.webp)

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

```
# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))
```
## 2D Numpy Array 

I am learning how to use these but I got a little confused on this one.  This is the correct answer below.  I was introduced to it differently in the video. 

```
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)
```
I thought that I would need to put np_baseball = np.array([[baseball]]).  I thought the two brackets would do the trick but it did not need them. 

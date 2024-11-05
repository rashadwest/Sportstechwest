---
layout: post
title: "Histogram flow"
thumbnail: "assets/img/blog-img/Screen Shot 2020-08-30 at 9.37.28 PM.webp"
---

# Histogram flow

## Histograph, Commute, Filter 

I learned about histogram this weekend.  I was familiar with them before but never identified it as a histogram.  They are really cool for data science.  It reminds 
me of when you are in school.  Some of my favorite classes included research where you use graphs.  It made sense to me.  

It would be great to create a histogram of player data.  It could include many different things.  For this project I will focus on shooting performance.  It will be interesting 
to see who does better in the playoffs.  I amy focus on critical time periods of the game at some point as well.  Like who does best under pressure.  

Now that I understand computer vision I am thinking about ways this can be incorporated as well. 


Here is the assignment below:
## Make a histogram

Histograms are one of the most useful tools in exploratory data analysis. They quickly give you an overview of the distribution of a variable, that is, what values the variable can have, and how many times each value appears.

As we saw in a previous exercise, the NSFG dataset includes a variable 'agecon' that records age at conception for each pregnancy. Here, you're going to plot a histogram of this variable. You'll use the bins parameter that you saw in the video, and also a new parameter - histtype - which you can read more about here in the matplotlib documentation. Learning how to read documentation is an essential skill. If you want to learn more about matplotlib, you can check out DataCamp's Introduction to Matplotlib course.

![Histogram]({{site.url}}{{site.baseurl}}/assets/img/blog-img/Screen%20Shot%202020-08-02%20at%209.25.03%20PM.webp?raw=true)

This is an assignment where I messed up on the code in the second line.  I was not sure how to make it happen.  You can see the error below.  As you can see my solution 
intitally I just have birth_weight and full_term out of order.  
![Compute:Infant baby weight assignment]({{site.url}}{{site.baseurl}}/assets/img/blog-img/Screen%20Shot%202020-08-02%20at%208.57.35%20PM.webp?raw=true)

```
# Create a Boolean Series for full-term babies
full_term = nsfg['prglngth'] >= 37

# Select the weights of full-term babies
full_term_weight = full_term[birth_weight]

# Compute the mean weight of full-term babies
print(full_term_weight.mean())
```

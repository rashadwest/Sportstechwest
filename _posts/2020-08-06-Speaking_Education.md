---
layout: post
title: "Speaking Education"
thumbnail: "assets/img/blog-img/Screen Shot 2020-08-30 at 9.37.28 PM.webp"
---

# Speaking Education

The current excercise I am doing is about education and I was also introduced to this great resource below that helps you compute complex equations and explains the output.  
![]({{site.url}}{{site.baseurl}}/assets/img/blog-img/Screen%20Shot%202020-08-07%20at%203.07.25%20AM.webp)

```
# Select educ
educ = gss['educ']

# Bachelor's degree
bach = gss(educ >= 16)

# Associate degree
assc = gss(educ >= 14 & educ < 16)

# High school
high = (educ <= 12)
print(high.mean())
```

Speaking of education I think this is a really useful and cool tool that I will use for sure in the near future.  This will help with data science no question. 
![]({{site.url}}{{site.baseurl}}/assets/img/blog-img/Screen%20Shot%202020-08-07%20at%203.34.18%20AM.webp)

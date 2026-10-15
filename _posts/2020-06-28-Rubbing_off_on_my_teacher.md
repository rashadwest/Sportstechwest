---
layout: post
title: "Rubbing off on my teacher"
thumbnail: "assets/img/blog-img/Screen Shot 2020-08-30 at 9.37.28 PM.webp"
---

# Rubbing off on my teacher (a little)

## Basketball is the greatest game in the world 

This was how I was approaching it when I first started.  I have come a long way. Now I am only focusing on a problem that is simple.  Who is the best point guard shooter of all time! 
If you have a chance, check out some of the things she mentioned.  It is cool to see someone who understands data but does not know much about basketball dive in because they want to help 
their student succeed. 

Student Prompt:

"I want to tell stories. Like look at how Chris Mullin's career got affected by his team getting better and having two All-Stars and a Hall of Fame coach with him. Although his stats went down, the team started winning."

Data:

Chris Mullin

[https://www.basketball-reference.com/players/m/mullich01.html](https://www.basketball-reference.com/players/m/mullich01.html)
[https://www.basketball-reference.com/players/m/mullich01/gamelog/1989/](https://www.basketball-reference.com/players/m/mullich01/gamelog/1989/)
[https://www.basketball-reference.com/players/m/mullich01/gamelog/1990/](https://www.basketball-reference.com/players/m/mullich01/gamelog/1990/)
[https://www.basketball-reference.com/players/m/mullich01/gamelog/1991/](https://www.basketball-reference.com/players/m/mullich01/gamelog/1991/)
Tim Hardaway

[https://www.basketball-reference.com/players/h/hardati01.html](https://www.basketball-reference.com/players/h/hardati01.html)
[https://www.basketball-reference.com/players/h/hardati01/gamelog/1990/](https://www.basketball-reference.com/players/h/hardati01/gamelog/1990/)
[https://www.basketball-reference.com/players/h/hardati01/gamelog/1991/](https://www.basketball-reference.com/players/h/hardati01/gamelog/1991/)
Mitch Richmond

[https://www.basketball-reference.com/players/r/richmmi01.html](https://www.basketball-reference.com/players/r/richmmi01.html)
[https://www.basketball-reference.com/players/r/richmmi01/gamelog/1989/](https://www.basketball-reference.com/players/r/richmmi01/gamelog/1989/)
[https://www.basketball-reference.com/players/r/richmmi01/gamelog/1990/](https://www.basketball-reference.com/players/r/richmmi01/gamelog/1990/)
[https://www.basketball-reference.com/players/r/richmmi01/gamelog/1991/](https://www.basketball-reference.com/players/r/richmmi01/gamelog/1991/)
Assumptions:

"Chris Mullin is above; We are trying to figure out why he had a decrease in performance year after year. 27 points, 6 rebounds and 4 assists is comparable to LeBron James, and this was early in Chris Mullin's career."
"Tim Hardaway is below; he is a point guard that really did well in the assist category as a rookie with 8.7 per game."
"George Karl was the coach from 1986-1988 and then Don Nelson came in with a more open coaching style. Nelson has the most wins of any coach in NBA history, with 1,335."
"The team's performance increased with Don Nelson, Mitch Richmond, and Tim Hardaway."
"Chris may also have taken a step back since he knew he had another elite scorer and an elite passer on the team."
"This could be the reason why his numbers started to go down."
Alright students, let's go down this rabbit hole...
I don't know much about basketball at all, but I am relatively logical and am very familiar with structuring data science projects, so let's turn some of these assumptions into actual data driven projects or more specifically one project. This student claims they would like to tell stories with data- makes sense given most people seem to want to do this nowadays. The student provides a data set, so let's start with the first question from the student:

why did Chris Mullin's performance decrease year over year?
When we are thinking about performance what are we talking about? How are we defining performance and what does that mean? Is this performance relative to some baseline and if so what is that baseline? Or are we defining the performance of the player relative to themself? I'm not sure just yet but after exploring the data just giving it a once over here are a few fields that stick out to me as being important, when thinking about performance:

Position: Small forward and shooting guard | this is important because it will give us something to start with. If we understand what the position of small forward and shooting guard and what they are evaluated on, then we can take a look at those metrics in relation to our baseline to determine what the performance of the player means.
Opp (Opponent) - this seems like an important metric to think about because if you are playing against a winning team with players who are more skilled than you, you are likely not going to perform as well as you would against someone who more closely matched your skill level. The opposite would be true for a less skilled team, we would assume that a weaker team would score fewer points. There is also a lot of nuance here in relation to specific players. From the Michael Jordan documentary about his team dynamics and large part of the winning streak they were on could be attributed to the technical depth of the players on the team, all the players were fire so they were collectively better than everyone else. It does feel like with this information we should be sure to think through how complementary players could affect the performance of the player in question.
FG% - Field Goal Percentage, this represents how successful the player was at the shots taken. Of the shots taken how many went in the hoop.
DRB - Defensive rebounds [rebounds are important for guards?]
ORB - Offensive rebounds [rebounds are important for guards?]
TRB - Total rebounds [rebounds are important for guards?]
Even with all of this information I don't feel comfortable enough yet to create any model or really analyze this data. We could certainly visualize this data so that it is easier to interpret. We will spend the day working on that and come back tomorrow with more information about how this could be useful to create a better hypothesis, or figure out a few more questions we could ask of our data.

The basketball wikipedia page seems to be very useful when trying to understand a bit more about the game. I was even able to find more specific information about the different positions:

Point guard (often called the "1") : usually the fastest player on the team, organizes the team's offense by controlling the ball and making sure that it gets to the right player at the right time.

Shooting guard (the "2") : creates a high volume of shots on offense, mainly long-ranged; and guards the opponent's best perimeter player on defense.

Small forward (the "3") : often primarily responsible for scoring points via cuts to the basket and dribble penetration; on defense seeks rebounds and steals, but sometimes plays more actively.

Power forward (the "4"): plays offensively often with their back to the basket; on defense, plays under the basket (in a zone defense) or against the opposing power forward (in man-to-man defense).

Center (the "5"): uses height and size to score (on offense), to protect the basket closely (on defense), or to rebound.

And there is an even more descriptive position page on the site that breaks down the positions in more depth. Basketball Positions

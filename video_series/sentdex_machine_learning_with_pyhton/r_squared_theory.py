'''
We would like to determine the 'accuracy' of our best-fit line. The coefficient
of determination is calculated with squared error. The error is the distance 
between a point and the best fit line, and then you square it. You square 
it because there will be positive and negative values, and we care about total
distance, but we use it instead of absolute value because we want to penalize
outliers. You can actually penalize even more for outliers by using higher 
powers, but the standard is squared. You calculate the coefficient of determination
(R^2) = 1 - (squarrederror(yhat)/squarederror(mean(y))
What this does is compare the accuracy of the best fit line to a line that
is just the mean of the ys. Obviously, we want this to be way better. 
So what are good values for R^2?

R^2 = 0.8, this means (squarrederror(yhat)/squarederror(mean(y)) = 0.2,
this means data is pretty linear 

R^2 = 0.3 means (squarrederror(yhat)/squarederror(mean(y)) = 0.7,
this means data is not as linear.

So, we want R^2 to be high, how high is dependent on the situation
'''
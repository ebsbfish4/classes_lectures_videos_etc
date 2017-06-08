'''
included soft-margin SVM
'''

'''
We have been talking about how to handle for non-linearly seperated
data. K(x, x') = z.z'  z = function(x), z' = function(x')
When you use a kernel, you convert x to z and x' of z'. Then
you find the dot product of z and z'. The two functions have to 
be the same. Remeber, the dot product returns a scaleature set.
feature set is X = [x1, x2ar value. So all we 
need (and get) from the z space is an inner product. 

First, we will consider a nice, two dimensional feature set.
feature set is X = [x1, x2] # a vector
Converting that to a 2nd order plynomial will give us 6 features
Z = [1, x1, x2, x1^2, x2^2, x1x2] # our new z space

K(x,x') = z.z'
That dot product is each value multiplied by itself.
K(x, x') = 1 + x1x'1 + x2 x'2 + x1^2x'1^2 + x2^2x'2^2 + x1x'1x2x'2

Simplified, the polynomial kernel is
K(x, x') = (1+ x.x')^p
There is no z in this calculation, how we can bypass it.
For however many features n
K(x,x') = (1 + x1x'1 + ... + xnx'n)^p
Increasing n and p, even significantly, using this equation is much
less costly than the previous operation in the z-space.

Another kernel is RBF (radial basis function)
K(x,x') exp(-g||x-x'||^2) # exp = e^x
###

You have to watch out for overfitting
In theory, you want a lot of data that is not part of the support vectors.
Training and testing is a good way to catch overfitting. 
You probably don't want more than 10% of your data to be in support vectors
(obviously this isn't exact but look out for things like this)
Soft-margin has some degree of error that we allow with slack
Remember
yi(xiw + b)>= 1
we can introduce some slack
yi(xiw + b) >= 1 - slack
Slack must be >= 0
The more slack you give, the softer your margin is going to be.
We most likely want to minimize the slack

from earlier but add
minimize 1/2||w||^2 + c sum(slack)
The more we raise c, the more we punish violations of the margin
C is somehting that you set. The smaller you make it, the less it
matters what the slacks (errors) are.
'''
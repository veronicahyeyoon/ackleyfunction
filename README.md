# video simulation for optimization
The Ackley function is a mathematical test function that is often used to test how well algorithms can find a global minima among many other local minima. This code is written in python to help you visualize how an optimal minimum point can be found in an Ackley function in 3D.

The Ackley function can be represented as:

__$f(x) = -a \exp(-b\sqrt(\frac{1}{n}\sum_{i=1}^d x_i^2))-\exp(\frac{1}{d}\sum_{i=1}^d \cos(cx_i))+a+\exp(1)$__

where recommended parameters are __$a=20$__, __$b=0.2$__, and __$c=2\pi$__, which are what this code uses. 

![](./optimal%20mimimum%20point.gif)

## explanations for modules & cells

### modules!
#### README
- What you are reading right now :o

#### ackleyfunctionminimizer
- This is the parent jupyter notebook that you will run the code in. The cells have comments in the first line explaining their function, but this will be repeated in the README here to give you a quick overview.

#### ackleyfunctionoutput
- This is a folder containing a function calculating the z value (or the Ackley function output). It will be imported into the parent jupyter notebook for graph plotting & finding the global minima. ackleyfunctioncalculator.py is where the actual code for calculating the function output is stored. 

#### graphimages
- This is a folder where the output 3D graph images of the local minima for each iteration of the loop will be saved. Images are saved in png and are numbered in the order the loops are run. 


### cells!
#### required imports
- All required packages imported here

#### function import
- Required function (ackleyfunctioncalculator) imported here

#### random number generator
- Random numbers generated for x,y points

#### list generator
- x,y inputs will be received and put into a list

#### example graph plotter
- Example 3D graph of ackley function plotted

#### optimal minimal point generator
- Uses a for loop that generates 5 random points and adds it to the points previously randomly generated. Appends the points to an empty list defined outside the loop. Takes the list and checks the z value of each x,y values, if z value is smaller than previous, defines it as a new minimum z, if not, returns nothing. Takes each redefined new minimum z and plots a 3D figure of it. Saves each figure in graphimages. 

#### save as video
- All output images in graphimages outputted as a single mp4 video. Can now visually track point on graph moving towards (0,0,0).

### the end


p.s.
book recs: arnold lobel's mouse soup <3

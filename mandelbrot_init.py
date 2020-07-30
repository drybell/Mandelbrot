# Daniel Ryaboshapka 

import numpy as np
from PIL import Image

### CURRENT APPROACHES ARE ALL BRUTE FORCE 
### TODO: OPTIMIZE SPEED AND DEPTH OF IMAGES 


# make a system that determines if the sequence   n^2 + x  for n -> infinity 
# converges in a confined space or diverges 

# mandelbrot making sits at radius 2 


# fc(z) = z^2 + c for fc(0), fc(fc(0)), 
# Its a julia set when iterating for z != 0 

# bail out threshold 
num_steps = 1000

def mandelbrot(num_steps, z, c, bounding):

	temp = z 
	print(temp)
	steps = np.linspace(0,num_steps - 1, num_steps)
	new_z = np.square(temp) + c  
	if new_z.real > bounding: 
		return num_steps, False, new_z, c	
	temp = new_z 


	return num_steps, True, z, c 


# print(mandelbrot(1000, 0, .23, 10))

## INPUT 
# 
# first value is the number of steps to iterate by (the color threshold)
# second value is z 
# third value is c 
# fourth value is bounding box 

## OUTPUT 
# step count, converge, z value (after computation), c  

# based on a bounding circle, iterate c and print to screen 

import matplotlib.pyplot as plt


def create_mandelbrot_plot(bounding_real, steps, bounding_iterator):
	complex_set = []

	r = np.linspace(0.0, float(bounding_real), steps)
	r2 = np.linspace(0.0, float(bounding_real), steps)
	x, y = np.meshgrid(r,1j * r2)
	c = [x,y]
	result = mandelbrot(steps, 0, c, bounding_iterator)
	if result[1]: 
		complex_set.append(result[3])

	return complex_set


# print(create_mandelbrot_plot(2.0, 1000, 2))

def array_for(x, steps):
    return np.array([simple_mandelbrot(steps, complex(xi[0], xi[1])) for xi in x])


def simple_mandelbrot(steps, start):
	z = 0 
	temp = z
	for i in range(steps): 
		new_z = np.square(temp) + start
		if new_z.real > 2: 
			return steps
		temp = new_z

	return steps

def run_mandelbrot(steps, grid): 
	converged = []
	for complex_num in grid: 
		test = simple_mandelbrot(steps, complex_num)
		if type(test) != bool: 
			converged.append(test)
	return converged


# steps = 100

# # Scale to rgb value equation
# # rgb_scale = (max_steps - steps)/max_steps * 255

# r = np.linspace(-2.0, 2.0, steps)
# r2 = np.linspace(-2.0, 2.0, steps)
# xs, ys = np.meshgrid(r, 1j * r2)

# grid = np.zeros((len(r), len(r2)))

# converged = []
# for a, x in enumerate(xs):
# 	for b, y in enumerate(ys): 
# 		c = x + y 	
# 		for item in c:
# 			test = simple_mandelbrot(steps, item)
# 			if not test[2]: 
# 				val = (steps - test[1])/steps * 255
# 				grid[a,b] = int((steps - test[1])/steps * 255)

# # print(converged)

# # xs = [s.real for s in converged]
# # ys = [s.imag for s in converged]

# w = len(xs)
# h = len(ys)


# 4K resolution = 3840 x 2160
# let those be the resolution of our graph
# 1.78:1 ratio

# -2 - .5 is the width at 3840 pixels --> .00065104 increment 

graph_width = 2.5 
graph_height = 2 
graph_x_min = -2.0 
graph_x_max = .5
graph_y_min = -1.0 
graph_y_max = 1.0 

resolution = [3840, 2160]
x_scale = resolution[0]/graph_width
y_scale = x_scale # but mapped from -1 to 1 

steps = 1275

xy = np.mgrid[graph_x_min:graph_x_max:complex(0,steps),
			  graph_y_min:graph_y_max:complex(0,steps)].reshape(2,-1).T

colors = array_for(xy, steps)

from rgbmap import rgbmap

def rgbify(steps, colors):
	try:
		return colors[steps]
	except Exception as e:
		print(e)

colors_rgb = np.array([rgbify(s, rgbmap) for s in colors])

# width of 2.5 scaled to 3840 pixels

# USE PIL TO MAKE THE PIXELS BE THE RIGHT COLOR INSTEAD
# FORMULATE A REPRESENTATION OF THE IMAGE PIXEL GRID AS THE NxN MATRIX 
# AND ASSIGN COLOR TO THE STEP COUNT 

# technically want to do a big step size, and color the step size of things diverging,
# black is points that converged

# plt.scatter(xs,ys)


# plt.show()

""" A memoization of the factorial function could look like this:
If n = 0, return 1
Otherwise if n is in the memo, return the memo's value for n
Otherwise,
	(n-1) * n
	Store result in the memo
	Return result """

# class Memo():
# 	def __init__(self, ):  


# RGB CONTINUATIONS 
# BLUE IS MORE COMPLEX (LONGER TIME)
# RED IS FASTER 
# ALWAYS MAKE THE CALCULATION OF TIME STEPS OVER 255

# R G B 
# (0,0,255) --> (0,255,255) --> (0,255,0) --> (255,255,0) --> (255, 0, 0)
# 255 * 5 total steps --> 1275 

# class Pixel():
# 	def __init__(self, x, y, rgb):
# 		self.x = x
# 		self.y = y 
# 		self.rgb = rgb 

# 	def setCoords(self, x, y): 
# 		self.x = x
# 		self.y = y

# 	def setRGB(self, rgb):
# 		self.rgb = rgb

# 	def getRGB(self):
# 		return self.rgb

# mndlbrt = np.vectorize(simple_mandelbrot)





img = Image.fromarray(colors_rgb, 'RGB')
img.show()













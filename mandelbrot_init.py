# Daniel Ryaboshapka 

import numpy as np

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


print(mandelbrot(1000, 0, .23, 10))

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



def simple_mandelbrot(steps, start):
	z = 0 
	temp = z
	for i in range(steps): 
		new_z = np.square(temp) + start
		if new_z.real > 2: 
			return False
		temp = new_z

	return start

def run_mandelbrot(steps, grid): 
	converged = []
	for complex_num in grid: 
		test = simple_mandelbrot(steps, complex_num)
		if type(test) != bool: 
			converged.append(test)
	return converged


steps = 100

r = np.linspace(-2.0, 2.0, steps)
r2 = np.linspace(-2.0, 2.0, steps)
xs, ys = np.meshgrid(r, 1j * r2)

converged = []
for x in xs:
	for y in ys: 
		c = x + y 
		for item in c:
			test = simple_mandelbrot(steps, item)
			if type(test) != bool: 
				converged.append(test)

print(converged)

xs = [s.real for s in converged]
ys = [s.imag for s in converged]

# USE PIL TO MAKE THE PIXELS BE THE RIGHT COLOR INSTEAD
# FORMULATE A REPRESENTATION OF THE IMAGE PIXEL GRID AS THE NxN MATRIX 
# AND ASSIGN COLOR TO THE STEP COUNT 

plt.scatter(xs,ys)


plt.show()














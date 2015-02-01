from django.shortcuts import render
from matplotlib import pylab
from pylob import *

def graph():
	x=[1,2,3,4,5,6]
	y=[5,2,6,7,2,7]
	plot(x,y,linewidth=2)

	xlabel('x axis')
	ylabel('y axis')
	title('sample graph')
	grid(True)
	pylab.show()

import matplotlib 
import fileinput 
matplotlib.use('TkAgg')


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler


from matplotlib.figure import Figure

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
from math import *

"""so to plot for the x axis it is just going to be numbers 1- 240""" 

#file_name = "/Users/MLee/Desktop/testdata4.txt"
file_name1 = "/Users/MLee/Desktop/testdata4.txt"
file_name2 = "/Users/MLee/Desktop/testdata4-comp.txt"
file_name3 = "/Users/MLee/Desktop/testdata4-reconst.txt"

#My Lists are below
x_axis = []
y_axis = []
reduced_x_axis = []
reduced_y_axis = []
final_reduced_x_axis = []
final_reduced_y_axis = []
reconstructed_x_axis = []
reconstructed_y_axis = []
#Below is the code for the first file
counter = 0
for legnth in fileinput.input([file_name1]):
	counter = counter + 1
print "The amount of values in the original data is" ,(counter)
#The amount of values in the first is 240 so xrange(240)
for x in xrange(240):
	x_axis.append(x)

for data in fileinput.input([file_name1]):
	paring = data.split()
	y_axis.append(float(paring[0]))
print "This is the original data X axis" ,x_axis
print "This is the original data Y axis" ,y_axis

#Below is the code for the second file

print "The amount of values in the reduced data is 15"
"""for moreGX in xrange(240):
	reconstructed_x_axis.append(moreGX)
"""



for xtra in fileinput.input([file_name2]):
	parsing = xtra.split()
	reduced_y_axis.append(float(parsing[0]))


#Below is the code for the third file 
counter2 = 0
for all_numbers in fileinput.input([file_name3]):
	counter2 = counter2 + 1

for hj in xrange(15):

	final_reduced_x_axis.append(hj)
#final_reduced_x_axis.append(reduced_x_axis[1:16])




print "This is the final reduced x axis" ,final_reduced_x_axis

#This will make the value only be 15
final_reduced_y_axis.append(reduced_y_axis[1:16])


print "This is the final reduced Y axis" ,final_reduced_y_axis

#Parsing below
for moreG in fileinput.input([file_name3]):
	parsing2 = moreG.split()
	reconstructed_y_axis.append(float(parsing2[0]))
#Making sure legnth is 240
counter3 = 0
for hmm_numbers in xrange(240):
	reconstructed_x_axis.append(hmm_numbers)
	counter3 = counter3 + 1

#Printing reconstructed code
print "The amount of values in the reconstructed data is" ,counter3
print "This is the reconstructed X axis" ,reconstructed_x_axis
print "This is the reconstructed Y axis" ,reconstructed_y_axis



#Below is all the Tkinter stuff
root = Tk.Tk()
root.attributes('-fullscreen', True)
root.wm_title("Comparing Three plots")

f = Figure(figsize=(5,3), dpi=100)
canvas = FigureCanvasTkAgg(f, master=root)
canvas.get_tk_widget().pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
toolbar = NavigationToolbar2TkAgg( canvas, root )
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
canvas.show()


#f = Figure(figsize=(5,4), dpi=100)
a = f.add_subplot(131)

a.scatter(x_axis,y_axis)
a.set_title("Original Data")
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
#canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
#toolbar = NavigationToolbar2TkAgg( canvas, root )
#toolbar.update()
#canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


x_io = [1,2]
y_io = [1,2]

#hill = Figure(figsize=(5,4), dpi=100)
apple = f.add_subplot(132)
apple.set_title("Reduced data")
apple.scatter(final_reduced_x_axis, final_reduced_y_axis)
#canvas1 = FigureCanvasTkAgg(hill, master=root)
canvas.show()
#canvas1.get_tk_widget().pack(side=Tk.BOTTOM, fill=Tk.BOTH, expand=1)

#canvas1._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)	


#canvas2 = FigureCanvasTkAgg(hill, master=root)


#hill2 = Figure(figsize=(5,4), dpi = 100)
pen = f.add_subplot(133)
pen.set_title("Reconstructed data")
#This wil graph the third plot which is the reconstructed data
pen.scatter(reconstructed_x_axis, reconstructed_y_axis)
#canvas3 = FigureCanvasTkAgg(hill2, master=root)
canvas.show()
#canvas3.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
#toolbar = NavigationToolbar2TkAgg( canvas, root )
#toolbar.update()

#canvas3._tkcanvas.pack(side=Tk.BOTTOM, fill=Tk.BOTH, expand=1)

Tk.mainloop()
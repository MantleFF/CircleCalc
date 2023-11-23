from math import sqrt
import numpy as np
from numpy import sin, cos, pi, linspace
from matplotlib import pyplot as plt, patches

class Circle:
  pi = pi
  def area(self,radius):
    return Circle.pi * radius ** 2 
  def circumfrence(self,diameter):
    return Circle.pi * diameter
  def radius_from_area(self,area):
    return sqrt((area/ Circle.pi))
  def radius_from_circumfrence(self,circumfrence):
    return circumfrence / (2 * Circle.pi)
circle = Circle()

class CircleFigure:
  def circlegraph(self,r):
    #draw point at origin (0, 0)
    plt.plot(0,0, color = 'red', marker = 'o')
    #draw a circle
    angles = linspace(0 * pi, 2 * pi, 100 )
    xs = r * cos(angles)
    ys = r * sin(angles)
    plt.plot(xs, ys, color = 'green')

    #draw diameter
    plt.plot(0, r, marker = 'o', color = 'blue')
    plt.plot(0, -r, marker = 'o', color = 'blue')
    plt.plot([0, 0], [r, -r])
    plt.plot((0.1),r/2, marker='D=${}$'.format(round((r*2),2)), markersize=30, label=r, color = 'blue')

    #draw radius
    plt.plot(0, 0, marker = 'o', color = 'purple')
    plt.plot(r, 0, marker = 'o', color = 'purple')
    plt.plot([0, r], [0, 0], color = 'purple')
    plt.plot(r/2,(0.1), marker='R=${}$'.format(round(r,2)), markersize=30, label=r, color = 'purple')

    #circumfrence number
    plt.plot(r-(r/2),r-(r/2), marker='C=${}$'.format(round(((2*pi*r)),2)), markersize=30, label=r, color = 'red')

    #area number
    plt.plot(-r+(r/2),r-(r/2), marker='A=${}$'.format(round(((r*r)*pi),2)), markersize=30, label=r, color = 'green')

    # setting x/y limit
    plt.xlim(None)
    plt.ylim(None)
    plt.gca().set_aspect('equal')

    #Graph header
    plt.title("Your Circle!")
    #
    plt.show()
vcircle = CircleFigure()

while True:
    calculator_choice = input("Make a choice: I know the (R)ADIUS, (A)REA or (C)IRUMFRENCE of the circle or E(X)it: ").lower()

    
    if calculator_choice == "r":
        while True:
          try:
            r = float(input("Input the radius of the circle : "))
            diameter = r*2
            print("The diameter of the circle is: " + str(round(diameter,2)))
            circumfrence = circle.circumfrence(r*2)
            print("The circumfrence of the circle is: " + str(round(circumfrence,2)))
            area = circle.area(r)
            print("The area of the circle is: " + str(round(area,2)))
            visuals = vcircle.circlegraph(r)
            break
          except ValueError:
            print("The input was not a valid number. Try again!")


    elif calculator_choice == "a":
        while True:
           try:
            a = float(input("Input the area of the circle : "))
            radius = circle.radius_from_area(a)
            print("The radius of the circle is: " + str(round(radius,2)))
            diameter = radius*2
            print("The diameter of the circle is: " + str(round(diameter,2)))
            circumfrence = circle.circumfrence(radius*2)
            print("The circunfrence of the circle is: " + str(round(circumfrence,2)))
            visuals = vcircle.circlegraph(radius)
            break
           except ValueError:
              print("The input was not a valid number. Try again!")


    elif calculator_choice == "c":
       while True:
          try:
            c = float(input("Input the circumfrence of the circle : "))
            radius = circle.radius_from_circumfrence(c)
            print("The radius of the circle is: " + str(round(radius,2)))
            diameter = radius*2
            print("The diameter of the circle is: " + str(round(diameter,2)))
            area = circle.area(radius)
            print("The area of the circle is: " + str(round(area,2)))
            visuals = vcircle.circlegraph(radius)
            break
          except ValueError:
            print("The input was not a valid number. Try again!") 


    elif calculator_choice == "x":
       break
    else:
       print("Error, invalid choice. Pick (R)ADIUS, (A)REA, (C)IRUMFRENCE or E(X)it")



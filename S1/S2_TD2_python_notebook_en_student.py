#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue"> <center>Student / TD2 : 4TPU279U $-$ Bachelor 1st year $-$ spring 2023</center></span>
# # <center>Introduction to python programming</center>
# # <hr style="border:1px solid black"><center>  Advanced basics </center><hr style="border:1px solid black">
# </br>
# 
# <div style="text-align: right"> Credits: R. Boisgard, L. Truflandier, Philippe Paillou, Julien Burgin, Sara Zein, Leo Delmarre, Simon Villain-Guillot </div>
# 

# The following topics will be cover in this notebook:
# - Function
# - Python intrinsic functions
# - Libraries
# - Printing format
# - Numpy array
# - Functions and array

# ## <hr style="border:1px solid black">  Function  <hr style="border:1px solid black">
# 
# In computer programming, a [function](https://en.wikipedia.org/wiki/Function_(computer_programming)) is a sequence of program instructions that performs a specific task, packaged as a unit (or block). This unit can then be used in programs wherever that particular task should be performed.
# 
# Functions may be defined within *programs*, or separately in *libraries* that can be used by many programs. In different programming languages, a function may be called a *routine*, *subprogram*, *subroutine*, *method*, or more generally a *procedure*.
# 
# In python we referred to as a function or when embedded in a class as a *method* (*vide infra*). The syntax for a python function is:

# In[ ]:


def name( arguments ):
    statements


# > ***name*** is the name of the function. As for variables, it should respect some basic syntaxic rules  (cf. TD1).
# 
# > ***arguments*** is a collection of values which are involved in managing the instructions. The collection may be empty. If several arguments are introduced, they must be separated by a coma. In any case, the parenthesis are mandatory. As for the basis constructs, the colon symbol closes the function header.
# 
# > ***statements*** is a set of instructions which are performed when the function is called. They must be *indented* from `def` by 4 spaces. Take-care: non-indented statements are said to be *outside* the function,
# they are not part of the function! 

# Sometimes, we want the function to return some result, as below:

# In[ ]:


def name( arguments ):
    statements
    return result


# Let's have for some abstract function of one single argument $x$: $f(x)=3x^2 - 2x^3$ where $x$ is the argument. We want this function to print the result of $f(x)$. An example is given below:

# In[ ]:


def func(x):
    print(3*x**2 - 2*x**3)


# Having defined the function `func` we need to *call it* in order to *run it*

# > for $x\in\mathbb{R}$, say $x=3.0$ let's call $f(x)$:

# In[ ]:


func(x=3.0)


# > Now let's try with $x\in\mathbb{B}$ (Remember, in that case, True and False are converted to 1 and 0).

# In[ ]:


func(x=True)


# > What will happen with a list ?

# In[ ]:


#func(x=[0,1,-1])


# ##### Exercise 2.0 <hr style="border:1px solid grey">

# > Using a `for` loop compute and print $f(x)$ over the list element $x=[0,1,-1]$.

# In[ ]:





# <hr style="border:1px solid grey">

# If now, we want the function to return the result we will write:

# In[ ]:


def func(x):
    result = 3*x**2 - 2*x**3
    return result


# > Note that for such simple function the statement $3x^2-2x^3$ can be put straight after `return`

# In[ ]:


def func(x):
    return 3*x**2 - 2*x**3


# > When calling the function we can ask to store the result in a new variable, such as: $y=f(x)$

# In[ ]:


y = func(x=1)
print(y)


# ##### Exercise 2.1 <hr style="border:1px solid grey">
# 
# For each function below : $$f(x)=4x^2\exp(-2x)$$ 
# 
# $$g(x)=\frac{x^2}{2}\left(1-\frac{x}{2}\right)^2\exp(-x)$$
# 
# $$h(x)= \frac{4x^2}{243}\left(3 - 2x + \frac{2}{9}x^2\right)^2 \exp\left(-\frac{2x}{3}\right)$$
# 
# 0. Define a function called `func_f`, `func_g` and `func_h`, respectively with $x$ as argument.
# 1. Compute $f(x=1)$, $g(x=2)$. 
# 2. It turns out that $f(x=1)$ is a the $\max$ of $f$ and $g(x=2)$ is a $\min$ for $g$. Is it expected ?
# 2. Compute $h(x)$ for $x_{+}=-\frac{3}{2}\left(\sqrt{3}-3\right)$ and $x_-=\frac{3}{2}\left(\sqrt{3}+3\right)$.
# 2. Using the code of **Exercice 1.8** in **TD1** compute the roots of $h(x)$ and compare to $x_{+}$ and $x_{-}$

# In[ ]:


from numpy import exp, sqrt


# In[ ]:





# ## <hr style="border:1px solid black">  Python intrinsic (built-in) functions  <hr style="border:1px solid black">
# 
# Python comes with a set of [built-in functions](https://docs.python.org/3/library/functions.html). 
# 
# - Basic mathematical functions are given below. 
# 
# > In the example, $x=[-11,-10,...,0,1,2,...,10]$ and we search for : $\max x$, $\min x$ and $|\min x|$
# 

# In[ ]:


x = list(range(-11,11))
print(x)
max_val = max(x)
min_val = min(x)
abs_val = abs(min_val)

print('the max  is: ', max_val)
print('the min  is: ', min_val)
print('abs(min) is: ', abs_val)


# > for $x=1.6$ and $y=1.4$ we search for and $\lfloor x\rceil$ and $\lfloor y\rceil$, ie. the nearest integer

# In[ ]:


x = 1.6
y = 1.4
print('x =',x, '=> round(x) =', round(x))
print('y =',y, '=> round(y) =', round(y))


# - `zip` to iterate over several lists

# In[ ]:


days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
num  = list(range(1,8))

for item in zip(num,days):
    print(item)


# ##### Exercice 2.2 : <hr style="border:1px solid grey">
# Review all the build-in functions already used in **TD1** and give an example

# <hr style="border:1px solid grey">

# In[ ]:





# ## <hr style="border:1px solid black"> Libraries  <hr style="border:1px solid black">
# 
# - [Numpy](https://numpy.org/doc/stable/index.html) = Numerical Python : library containing basic numerical tools and the `array`class
# - [Scipy](https://docs.scipy.org/doc/scipy/index.html) = Scientific Python : for advanced algorithms including linear algebra, numerical PDE and integration, fitting, optimisation, Fourier transform...
# - [Matplotlib](https://matplotlib.org) = Mathematical plotting library : for plotting in 1D/2D(3D)
# 
# ### There are 3 basic ways of using a library

# > import straight the library using `import`. Then points towards the function you need.
# > Here the sinus function is imported from numpy as `sin`.  where $x$ can 
# > 

# In[ ]:


import numpy
numpy.sin(0.1)


# > import the library and assign an *alias* ; here `np`

# In[ ]:


import numpy as np
np.sin(0.1)


# > import explicitely the funtion using `from *library_name* import *the_function*`

# In[ ]:


from numpy import sin
sin(0.1)


# ### Library scipy.constants for physical and mathematical constants and units.
# 
# > This library [scipy.constants](https://docs.scipy.org/doc/scipy/reference/constants.html) gives access to all the fundamental constants internationally recommended by [CODATA](https://physics.nist.gov/cuu/Constants/index.html)
# 

# In[ ]:


from scipy.constants import h, c, e, epsilon_0
from scipy.constants import unit

print('Planck constant   = ',h)
print('speed of light    = ',c)
print('elementary charge = ',e)
print()
print('Planck constant   = ',h, unit('Planck constant'))
print('speed of light    = ',c, unit('speed of light in vacuum'))
print('elementary charge = ',e, unit('elementary charge'))


# > you can search through the dictionnary using the `find()` function

# In[ ]:


from scipy.constants import find, physical_constants

name = find('Planck')
print(name)

print()
value, unit, uncertainty = physical_constants['molar Planck constant']
print(value, unit, uncertainty)

#name = find('speed of light')
#print(name)

#value, unit, uncertainty = physical_constants[name[0]]
#print(value, unit, uncertainty)


# In[ ]:


from scipy.constants import find, physical_constants

name = find('permittivity')
print(name)


# In[ ]:


from scipy.constants import giga, femto, yotta, inch, foot, angstrom

print('giga   =',giga)   
print('femto  =',femto)    
print('yotta  =',yotta)    
print('1 inch =',inch,'m')    
print('1 foot =',foot,'m')   
print('1 Anstrom =',angstrom,'m')   


# ## <hr style="border:1px solid black"> Printing format  <hr style="border:1px solid black">

# > unformatted print of the Planck constant $h$

# In[ ]:


from scipy.constants import h

print('Planck constant = ',h)


# > formatted print using scientific notation $\{e\}$ :
# 
# > $\{$%$\}$ indicate where to print the number in the characters string
# 
# > $\{$12.4$\}$ = length of 12 characters (total) with 4 decimals 
# 
# > Warning : remember that `6.6261e-34` means $6.6261\times 10^{-34}$

# In[ ]:


print('Planck constant = %12.4e '%h)


# > You can let python adapts the length of the scientific number by typing $\{$.4e$\}$

# In[ ]:


print('Planck constant = %.4e '%h)


# In[ ]:


print('Planck constant = %.4e J.s'%h)


# > $\{$s$\}$ is used for strings

# In[ ]:


print('Planck constant = %.4e %s'%(h,'J.s'))


# > formatted print using floating point notation $\{f\}$ :  

# In[ ]:


from scipy.constants import c

print('speed of light = ',c)
print('speed of light = %20.4f'%c)
print('speed of light = %.4f'%c)


# ##### Exercice 2.3 : constants

# Using the `scipy.constants` module:
# 
# - Compute the force between two electrons separated by 1 Ang. using the Coulomb law:
# $$||\vec{F}_C||  = \frac{1}{4\pi\epsilon_0}\frac{e^2}{r^2}$$
# - Compute the Rybderg constant $$R_H=\frac{mq_e^4}{8\varepsilon^2_0h^3c}$$ where 
#   - $\epsilon_0$ is the vacuum electric permittivity
#   - $q_e$ the elementary charge
#   -  $m$ the electron mass
#   - $h$ is the Planck constant
#   - $c$ the speed of light
# 
# - Compare to the Rydberg contant implemented in `scipy.constants` as `Rydberg`

# In[ ]:





# ## <hr style="border:1px solid black">  Numpy array  <hr style="border:1px solid black">

# ### `list`

# In[ ]:


L1 = [1,20,3.14,1+3j]
L2 = [2.5,'toto', L1]


# In[ ]:


print(L1,L2)


# In[ ]:


type(L1), type(L2)


# In[ ]:


print(L1+L2)


# ### `array`

# > build an `array` from a `list`

# In[ ]:


from numpy import array, pi, zeros

L = [5,pi/2,6.3] 
print(L, type(L))

A = array(L)
print(A, type(A))


# > build and initialize an `array` with zeros or ones

# In[ ]:


from numpy import zeros, ones

A = zeros((4))
print(A, type(A))

B = ones((4))
print(B,type(B))


# ### Differences between a `list` and an `array`
# 

# In[ ]:


L1 = [3,6,2]
L2 = [8,1,4]
print(L1)
print(L2)

L = L1+L2
print(L)

L = L1*4
print (L)


# In[ ]:


A1 = array(L1)
A2 = array(L2)
A  = A1+A2
print(A)

B = A1*A2
print(B)


# ### `arange`

# > arange($x_{inf}$, $x_{sup}$, $\delta$) with $\delta$ the step
# 
# > create an `array` of floats $x\in[x_{inf},x_{sup}[$
# such that $x=\{x_{inf},\;x_{inf}+\delta,\;x_{inf}+2\delta,...\}$
# 
# > it stops before $x_{sup}$ !

# In[ ]:


from numpy import arange

A = arange(2,3,0.2)
print(A,type(A))


# ### `linspace`

# > linspace($x_{inf}$, $x_{sup}$, $n$) with $n$ number of points
# 
# > create an `array` of floats $x\in[x_{inf},x_{sup}]$
# 
# > such that $x=\{x_{inf},\;x_{inf}+\delta,\;x_{inf}+2\delta,...,x_{sup}\}$ and $\delta=\frac{x_{sup}-x_{inf}}{n-1}$

# In[ ]:


from numpy import linspace

A = linspace(0,10,6)
print(A,type(A))


# ### Accessing 1D `array` elements

# > print the entire array

# In[ ]:


from numpy import linspace

x = linspace(2,12,6) 
print(x)
print(x[:])


# > print only some elements by the index

# In[ ]:


print(x[0], x[3])


# > from $n=3$ (included) to $m=5$ (excluded)

# In[ ]:


print(x[3:5])


# > from $n=3$ (excluded) to the end

# In[ ]:


print(x[3:])


# > from the beginning to $n=3$ (included) 

# In[ ]:


print(x[:3])


# > print the last element

# In[ ]:


print(x[-1]) 


# ### Accessing 2D `array` elements

# > let's have: $M\in\mathbb{N}^{3\times 3}$

# In[ ]:


from numpy import array

M = array([[1,   2,  3],
           [10, 11, 12],
           [20, 21, 22]])
print(M)


# > print the first row

# In[ ]:


print(M[0,:])


# > print the first column

# In[ ]:


print(M[:,0])


# > print an element

# In[ ]:


print(M[1,2])


# ## <hr style="border:1px solid black"> Function and array  <hr style="border:1px solid black">

# > Let's have for some abstract $x$: $f(x;a,b)=a\times x + b$ where $x$ is the variable and $(a,b)$ some parameters

# In[ ]:


def func(x,a,b):
    y = a*x + b
    return y


# > for $x\in\mathbb{R}$, say $x=3.2$ and $(a=2.0,b=1.0)$, let's compute $f(x)$:

# In[ ]:


# print result straight in standard output
func(x=3.2,a=2.0,b=1.0)


# In[ ]:


# store result in a variable
c = func(x=3.2,a=2.0,b=1.0)
print(c)

# implicit assignment of arguments
c = func(3.2,2.0,1.0)
print(c)


# > for $v\in\mathbb{R}^{3}$, with $(a=2.0,b=1.0)$, let's compute $f(v)$:

# In[ ]:


from numpy import array

v = array([1,2,3])
y = func(x=v,a=2.0,b=1.0)

print('v vector:')
print(v)
print('y vector:')
print(y)


# > we found that if $v\in\mathbb{R}^{3}$ then $f(v)\in\mathbb{R}^{3}$ ! Note that $b$ does not need to be a vector !
# 
# > `python` has interpreted: $a\times v + b\times o$ with $o=[1,1,1]$.

# ##### Exercice 2.4 : vector norm <hr style="border:1px solid grey">
# Given $v\in\mathbb{R^{3}}$, write a function wich computes $||v||$ ; compare to the function `norm`
# from the library `numpy.linalg`.
# 
# Compute $||a||$, $||b||$, $||c||$ using $a=(1/\sqrt{2},\; 0,\: -1/\sqrt{2})$, $b=(1/\sqrt{6},\; -2/\sqrt{6},\: 1/\sqrt{6})$ and
# $c=(1/\sqrt{3},\; 1/\sqrt{3},\: 1/\sqrt{3})$

# In[ ]:


from numpy.linalg import norm
from numpy import sqrt, array
 


# <hr style="border:1px solid grey">

# ##### Exercice 2.5 : inner product (= dot product) <hr style="border:1px solid grey">
# Given $(v,w)\in\mathbb{R^{3}}$, write a function wich computes $v\cdot w$ ; compare to the function `inner`
# from the library `numpy`.
# 
# Compute $a\cdot b$, $b\cdot c$ and $a\cdot c$ with $a=(1/\sqrt{2},\; 0,\: -1/\sqrt{2})$, $b=(1/\sqrt{6},\; -2/\sqrt{6},\: 1/\sqrt{6})$ and
# $c=(1/\sqrt{3},\; 1/\sqrt{3},\: 1/\sqrt{3})$

# In[ ]:


from numpy import array, inner


# <hr style="border:1px solid grey">

# ##### Exercice 2.6 : externalize the function in a `python` file <hr style="border:1px solid grey">
# 
# 0. Create a new `python` file named `my_lib.py` using **Anaconda/Spyder**.
# 1. Copy the function `my_norm` and `my_inner` into that file.
# 2. Save the file at the same location than the jupyter-notebook file.
# 3. Import `my_norm` and `my_inner` from `my_lib` and test them.

# In[ ]:





# <hr style="border:1px solid grey">

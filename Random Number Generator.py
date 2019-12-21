#!/usr/bin/env python
# coding: utf-8



class LCG:    # how computer generates random values
    
    def __init__(self,sd,mul,inc,mod): #constructor defining data attributes seed, multiplier, increment , modulus
        self.seed = sd #seed
        self.multiplier = mul #multiplier
        self.increment = inc #increment
        self.modulus = mod #modulus
        
    def get_seed(self):   # method to get the seed of the random no generator
        return self.seed
        
    def set_seed(self, new_seed):  # method to set the seed for the random generator
        self.seed = new_seed
        
    def init_generator(self):   # method to calculate the the random no using the recurrence relation for LCG 
        x_new = (self.multiplier*self.seed + self.increment)
        rand_no = x_new%self.modulus 
        rand_n = rand_no/self.modulus
        self.seed = rand_no
        return rand_n
        
    def next_random(self):  # method to generate the next random no by calling the init_generator() method 
        
        rand_n = self.init_generator()
        self.seed = rand_n*self.modulus
        return rand_n

        
    def list_random(self, length): # method to create a list of random numbers by taking the length of list as parameter
        
        rand_list = [] 
        
        for i in range(length):
            aa = self.init_generator()
            rand_list.append(aa)
            
        return rand_list # rand_list returns a list of random no

        
l1 = LCG(1,1103515245,12345,2**32)
print("The seed is by using the get_seed() function is: ", l1.get_seed())
print("\n")
print("The list of random numbers is : ", l1.list_random(50))
print("\n")
print("Random no :", l1.init_generator())
print("\n")
print("The next random number is", l1.next_random())
print("\n")
l1.set_seed(1)
print("The seed is by using the get_seed() function is: ", l1.get_seed())


# In[55]:


import sys
class SCG(LCG):  # defining a class SCG by inheriting the class LCG
    
    def __init__(self,seed,modulus): # here we over-ride the constructor and take seed and modulus as data attributes 
        self.seed = seed
        self.modulus = modulus
        
        if self.seed%4 == 2:   # We check whether the seed satisfies the condition
            pass
        else:
            print("The seed no entered is not correct")
            sys.exit()
        
    def init_generator(self):   # method to calculate the random no  using the SCCG recurrence relation
        x_new = self.seed*(self.seed + 1)
        rand = x_new%self.modulus 
        rand_n = rand/self.modulus   
        self.seed = rand
        return rand_n
                 
    def __next__(self):    #BONUS POINT QN  # method to find the next random no
        rand_n = self.init_generator()
        self.seed = rand_n*self.modulus
        return rand_n
    
cc = SCG(6,2**32)
print("The seed we get after using the get_seed() method is ", cc.get_seed())
print("\n")
print("The random no generated is :", cc.init_generator())
print("\n")
print("The next random no using the __next__ method is: ", cc.__next__())
print("\n")
cc.set_seed(6)
print("The list of random numbers is :", cc.list_random(50))


# In[9]:


# CIRCLE POINTS
import math
from sklearn import preprocessing  

class point:   # class to represent the points in the rectangular coordinate
    
    def __init__(self, x_cor, y_cor):
        self.x_cor = x_cor
        self.y_cor = y_cor
        
    def distance(self): # calculates the distance of the point from the origin
        dist = math.sqrt(x_cor*x_cor + y_cor*y_cor)
        return dist
        


# In[56]:


l1.set_seed(1) # setting the seed back to 1, here l1 is an instance of the class LCG
populate_list = l1.list_random(2*10**7)  # creating a list of 2 million random numbers 


# In[71]:


cc.set_seed(1)
scg_populate = cc.list_random(2*10**7)


# In[57]:


print(len(populate_list))


# In[73]:


populate_scaled = []
def scale(mylist, out_range=(-1,1)):   # method to scale the random numbers bettween the range [-1,1]
        domain =[]
        domain = [min(mylist), max(mylist)]
        for i in range (len(mylist)):
            y = (mylist[i] - (domain[1] + domain[0])/2) / (domain[1] - domain[0])
            populate_scaled.append(y*(out_range[1] - out_range[0]) + (out_range[1]+out_range[0])/2)
        return populate_scaled
    
scale(populate_list)


# In[74]:


populate_scg = []
def scale(mylist, out_range=(-1,1)):   # method to scale the random numbers bettween the range [-1,1]
        domain =[]
        domain = [min(mylist), max(mylist)]
        for i in range (len(mylist)):
            y = (mylist[i] - (domain[1] + domain[0])/2) / (domain[1] - domain[0])
            populate_scaled.append(y*(out_range[1] - out_range[0]) + (out_range[1]+out_range[0])/2)
        return populate_scg
    
scale(scg_populate)


# In[59]:


print(len(populate_scaled))


# In[66]:


import numpy as np
import random
theta = np.linspace(0, 2*np.pi, 100) # Here we plot the scaled random numbers in a rectangular box
                                    # we also plot the circle with radius 1 and center (0,0)
r = np.sqrt(1.0)

x1 = r*np.cos(theta)
x2 = r*np.sin(theta)

fig, ax = plt.subplots(1)

ax.plot(x1, x2)
ax.set_aspect(1)

plt.xlim(-1,1)
plt.ylim(-1,1)

import matplotlib.pyplot as plt
x = []
y = []

for i in range(len(populate_scaled)):
    
    x_cor = random.choice(populate_scaled)
    x.append(x_cor)
    y_cor = random.choice(populate_scaled)
    y.append(y_cor)
    # x is the list consisting of all the x co-ordinates and y is the list consisting of all the y co-ordinates
plt.scatter(x, y, alpha = 0.1)  # here we plot the points 


plt.show()


# In[61]:


#calculate the distance of the points from the origin
import math

def distance(x_cor, y_cor): # calculates the distance of the point from the origin
        dist = math.sqrt(x_cor*x_cor + y_cor*y_cor)
        return dist
    
distance_point = []
for i in range(len(x)):
    dis_pt = distance(x[i], y[i])
    distance_point.append(dis_pt)
    


# In[75]:


x_scg = []
y_scg = []
for i in range(len(scg_populate)):
    
    x_cor = random.choice(scg_populate)
    x_scg.append(x_cor)
    y_cor = random.choice(scg_populate)
    y_scg.append(y_cor)


# In[76]:


distance_scg = []
for i in range(len(x)):
    dis_scg = distance(x_scg[i], y_scg[i])
    distance_scg.append(dis_pt)
    


# In[62]:


points_inside = 0
points_outside = 0

for i in range(len(distance_point)):
    if distance_point[i] < 1:
        points_inside += 1
    else:
        points_outside += 1
        
print("The no of points inside the circle are : ",points_inside)
print("The no of points outside the circle are : ", points_outside)

        


# In[77]:


points_in_scg = 0
points_out_scg = 0

for i in range(len(distance_scg)):
    if distance_scg[i] < 1:
        points_in_scg += 1
    else:
        points_out_scg += 1
        
print("The no of points inside the circle are : ",points_in_scg)
print("The no of points outside the circle are : ", points_out_scg)

        


# In[63]:


ratio = points_inside/len(populate_scaled)
print("The ratio of the no of points within the circle", ratio)


# In[ ]:


ratio_scg = points_in_scg/len(scg_populate)
print("The ratio of the no of points within the circle for SCG IS : ", ratio_scg)


# In[67]:


#difference between theoretical and my ratio
difference = ratio - 0.78539816339
print("difference between theoretical and my ratio ", difference)


# In[ ]:


#difference between theoretical and my ratio
difference_scg = ratio_scg - 0.78539816339
print("difference between theoretical and my ratio ", difference_scg)


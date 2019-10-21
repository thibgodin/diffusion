
# coding: utf-8

# In[11]:


#%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt

def randomPermutation(n):
    ## creates a random permutation on n elements
    tableau = []
    for i in range(n): ## we create an array of length n: [1,2,...,n]
        tableau.append(i+1)
    
    permutation = []
    for i in range(n): 
       	#np.random.choice()

        #tab.append()

        #tab.remove(random_elmt)

        #print(tab)

    return(permutation)


# In[12]:


#test

p=randomPermutation(10)


# In[13]:


def hasOneCycle(permutation):
    ## determines if the permuation is formed by a unique cycle
    ## returns 1 if yes, 0 otherwise

    start=permutation[0]
    ## first element of the permutation
    #print(start)
    next_elt=permutation[start-1]
    ## successor element
    cycle_length=1
    #print(next_elt)
    while next_elt != start:
      

        #print(next_elt)

    if  cycle_length>=?:
        return 1
    else:
        return 0


# In[14]:


#test
p=randomPermutation(10)

hasOneCycle(p)
#hasOneCycle([2,3,4,5,6,1])
#hasOneCycle([2,3,4,5,6,1,7])


# In[15]:


def countOneCycle(n,k):
    ## counts the number of permutations on n elements that are formed by one cycle
    ## random sampling
    #n: size of perm, k: nb tries
    nb=0
    for i in range(k):

    return nb



# In[16]:


#test

n=25
k=10000
c=countOneCycle(n,k)
print(c)
print(c/k)
print(1/n)


# In[20]:


def plot(n):
    plot=[]
    for i in range(1,n):
        plot.append(countOneCycle(i,5000)/5000)
        print(plot[i-1])
    return plot


# In[21]:


#test

t=plot(30)
t




plt.plot(range(1,30),t)


#!/usr/bin/env python
# coding: utf-8

# # Broadcasting

# The term broadcasting describes how numpy treats arrays with different shapes during arithmetic operations. Subject to certain constraints, the smaller array is “broadcast” across the larger array so that they have compatible shapes.

# # Why is it needed? 

# - Broadcasting solves the problem of arithmetic between arrays of differing shapes by in effect replicating the smaller array along the last mismatched dimension.
# - In ML we deal with the data(learning and traning data) in which we perfrome different opperation on it like multiplication,addtion and subtaction.So, this data in from of matrices that is multply with sacalar or different demintation matrices.
# - Broadcasting provides a means of vectorizing array operations so that why we doest'n need looping in Python.It does this without making needless copies of data and usually leads to efficient algorithm implementations. 
# - But in some cases where broadcasting is a bad idea because it leads to inefficient use of memory that slows computation.

# # How do you do it? 

# - **Scalar and One-Dimensional Array**

# In[1]:



a=np.arange(3)
print(a)
#here numpy extende b into 1*3 from ([1,1,1])
b=1
print(b)
c=a+b
print(c)


# In[6]:


a=np.arange(3)
print(a)
#here numpy extende b into 1*3 from ([2,2,2])
b=2
print(b)
c=a*b
print(c)


# - **Scalar and Two-Dimensional Array**

# In[9]:


a=np.arange(4)
x=a.reshape(4,1)
print(x)
#here numpy extende b into 4*1 from
b=2
print(b)
c=a+b
print(c)


# - **One-Dimensional and Two-Dimensional Arrays**

# In[13]:


a=np.array([[1,2,3],[4,5,6]])
b=np.array([7,8,9])
c=a*b
print(c)


# # Limitations of Broadcasting

# Arithmetic, including broadcasting, can only be performed when the shape of each dimension in the arrays are equal or one has the dimension size of 1. The dimensions are considered in reverse order, starting with the trailing dimension; for example, looking at columns before rows in a two-dimensional case.

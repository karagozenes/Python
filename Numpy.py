#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


listem = 20,30,40
np.array(listem)


# In[3]:


listem2 = [[10,20,30],[40,50,60],[70,80,90]]
np.array(listem2)


# In[4]:


np.arange(0,10,2)


# In[5]:


listem3 = [np.arange(0,7,2), np.arange(6,11,2), np.arange(12,17,2)]
print(listem3)


# In[6]:


np.linspace(0,10,11)


# In[7]:


np.eye(10)


# In[8]:


np.random.randn(4,4)


# In[9]:


benimdizim = np.arange(30)
benimdizim.reshape(6,5)


# In[10]:


benimdizim.argmin()


# In[11]:


benimdizim.argmax()


# In[12]:


listem3 = np.arange(10,30,2)
print(listem3)

# 10 ile 30 arasında 2 şer 2 şer artan bir dizi oluşturur


# In[13]:


listem3.reshape(2,5)

# dizi elemanlarından matris oluşturur


# In[14]:


listem3.reshape(2,5).T

# Oluşturulan matrisin transpozunu alır


# In[15]:


listem3.sum()

# dizinin elemanlarını toplar


# In[16]:


a = [[2,5,6],[3,4,5]]
b = [[4,3],[5,7],[6,9]]

np.dot(a,b)

# a ve b matrislerini çarpar (matris çarpımı)


# In[17]:


a = np.array([[1,4,9],[16,25,36]])
b = np.array([[4,3,8],[5,7,4]])

np.dot(a,b.T)

# b'nin transpozunu alıp a ile matrisi ile çarpar


# In[18]:


print(np.sqrt(144))

# parametre olarak verilen elemanın karekökünü alır

np.sqrt(a)

# a matrisinin her elemanın karekökünü alır


# In[19]:


np.ravel(a)

# a matrisini diziye çevirir


# In[20]:


c = np.ravel(a)
d = np.ravel(b)

dikey = np.vstack((c,d))
print(dikey)

# c ve d matrisleri ayrı ayrı diziye çevirilir sonra bu diziler yatay olarak (alt alta) birleştirilir


# In[21]:


yatay = np.hstack((c,d))
print(yatay)

# c ve d dizileri dikey olarak (yan yana) birleştirilir


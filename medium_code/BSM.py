#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np  
from scipy.stats import norm
import math


# In[2]:


def d1(underlying, strike, dte, vol, interest):
    """
    

    Parameters
    ----------
    underlying : float or int
        Underlying stock price.
    strike : float or int
        Strike price.
    dte : int
        # days to expiration .
    vol : float
        underlying volatility as 0.xx.
    interest : float
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    dte = dte/365
    return (1/(vol*np.sqrt(dte)))*(np.log(underlying/strike)+(interest+(vol**2)/2)*dte)


# In[3]:


def d2(underlying, strike, dte, vol, interest):
    return d1(underlying, strike, dte, vol, interest)-(vol*np.sqrt(dte/365))


# In[4]:


def nd1(underlying, strike, dte, vol, interest):
    return np.exp(-(d1(underlying, strike, dte, vol, interest)**2)/2)/np.sqrt(2*math.pi)


# In[5]:


def price_call(underlying, strike, dte, vol, interest):
    return (norm.cdf(d1(underlying, strike, dte, vol, interest))*underlying)-(norm.cdf(d2(underlying, strike, dte, vol, interest))*strike*np.exp(-interest*(dte/365)))


# In[6]:


def price_put(underlying, strike, dte, vol, interest):
    return (norm.cdf(-d2(underlying, strike, dte, vol, interest))*strike*np.exp(-interest*(dte/365)))-(norm.cdf(-d1(underlying, strike, dte, vol, interest))*underlying)


# In[11]:


def strike_put(underlying, delta, dte, vol, interest):
    dte = dte/365
    return underlying*np.exp(norm.ppf(-1*delta)*vol*np.sqrt(dte)+(.5*vol**2*dte))


# In[32]:


def strike_call(underlying, delta, dte, vol, interest):
    dte = dte/365
    return underlying*np.exp(-norm.ppf(delta)*vol*np.sqrt(dte)+(.5*vol**2*dte))


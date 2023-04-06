# -*- coding: utf-8 -*-
"""1D_HarrisSheet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uvOTTbSGhbLtnAwpQ-LmVn80nUiel7Do
"""

import numpy as np
import math
import astropy.units as u
import astropy.constants as const

class HarrisSheet:
  
  def __init__(self,B0,delta,P0=0*u.Pa):
    self.B0=B0
    self.delta=delta
    self.P0=P0
  
  def magnetic_field(self, y):
    return self.B0*math.tanh(y/self.delta)
    "Defines magnetic field"
  def current_density(self,y):
    return self.B0/(self.delta*const.mu0)*(math.sech(y/self.delta)**2)

  def plasma_pressure(self,y):
    return self.B0**2/(2*const.mu0)*(math.sech(y/self.delta)**2)+self.P0


"""
    Compute Harris Sheet

    Parameters
    
    B0-------------- Intial Magnetic field
    delta--------Thickness of current sheet
    P0--------------Intial Plasma Pressure



    Returns
    
    Magnetic Field
    Current Density 
    Plasma Pressure

    Raises
    ------

    Warns
    -----

    See Also
    --------

    Notes
    -----

    References
    ----------

    Examples
    --------

    """

harris_sheet = HarrisSheet(delta = 3*u.m ,B0 = 2*u.T)
harris_sheet.magnetic_field(y = 5*u.m)

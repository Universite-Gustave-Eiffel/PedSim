* intro
* context
* problem presentation

Pedestrian traffic meets a lot of issue as daily operations optimization or management in crowded areas such as airports or train stations, or as linked to the safety and evacuation plans issues. 

We develop a platform coded in Python to model pedestrian flows. 


# Models and assumptions used to developp the platform
## Flow equations and numerical scheme
The built model is macroscopic dynamic, so the traffic is considered as a continuous flow and pedestrians’ general behavior is treated by analogy to transport models in fluid dynamics.

The equilibrium relation links pedestrians’ speed with their density. The model is essentially based on Stéphane Mollier’s thesis, « Two-dimensional models for large-scale traffic networks » about flow equations and numerical schemes.
### Time discretization
* Runge Kutta
### Space discretization
* Weno scheme
* splitting method

## Global and local direction 
We use the paper of Hoogendoorn Serge P.et al., «Continuum theory for pedestrian traffic flow: Local route choice modelling and its implications » about pedestrian direction which includes a global component determined before their start and a local one that adjusts the original direction according to local variations.
### Fast marching method
### global and local direction 
<a href="https://github.com/Ifsttar/PedSim/blob/master/Docs/Flow%20equations%20and%20numerical%20scheme.rst"> To see more about global and local direction<a/>

## Parameters and global variables used
## Boundaries conditions
* Ghost cells
## Bibliography


# Functioning of the platform
## How to use it?
## Test cases
## Results
## areas of improvement 


# Computer programming
## Functions
## General loop
## useful to know 
* Python modules used

Pedestrian traffic meets a lot of issue as daily operations optimization or management in crowded areas such as airports or train stations, or as linked to the safety and evacuation plans issues. 

We develop a platform coded in Python to model pedestrian flows. 

The built model is macroscopic dynamic, so we consider the traffic as a continuous flow, and pedestrians’ general behavior is treated by analogy to transport models in fluid dynamics. The equilibrium relation links pedestrians’ speed with their density. 

Pedestrians are divided into different layers according to their original direction, that is to say, according to their entrance and exit doors. Thus, we separately compute the pedestrian density of each layer before the global density.

# Functioning of the platform
The platform enables us to describe the pedestrian traffic evolution in a network. A mesh modelizes the latter. So, we compute the pedestrian density in each cell of the mesh for each layer. The code returns the global density at each time step. For some of them, it displays for each layer, the layer density (so the pedestrian flow for each pedestrian class), and the global density (so the general pedestrian traffic).

## Use of the platform
It is suitable for many test cases. Users can create a new one by defining the domain, entrances, exits, the number of layers, obstacles. 
<a href=" https://github.com/Ifsttar/PedSim/blob/master/docs/Use%20of%20the%20platform.rst "> To see more about the use of the platform <a/>
  
## Test cases
The code integrates several test cases to become aware of what the platform can provide. Thus, there are simple tests with only two layers to examine what precisely happens at crossing points. We also find test cases with multiple layers, and somewhere pedestrian demands fluctuate over time.
<a href=" https://github.com/Ifsttar/PedSim/blob/master/docs/Test%20cases.rst "> To see more about the different test cases <a/>

## Areas of improvement
<a href=" https://github.com/Ifsttar/PedSim/blob/master/docs/Areas%20of%20improvement.rst "> To see more about areas of improvement<a/>)

# Models and assumptions used to develop the platform
## Flow equations, numerical schemes, and boundary conditions

We essentially used flow equations and numerical schemes described in Stéphane Mollier’s thesis, « Two-dimensional models for large-scale traffic networks » [1] to construct the model. Thus, we use the WENO scheme, the total variation diminishing (TVD) Runge Kutta time discretization, and the dimensional splitting. It is a fifth-order method in space and a third-order in time. That provides us the convergence, stability, and consistency of the solution. 

<a href=" https://github.com/Ifsttar/PedSim/blob/master/docs/Flow%20equations%20and%20numerical%20scheme.rst "> To see more aboutFlow equations, numerical schemes and boundary conditions<a/>

## Global and local direction 
We use the paper of Hoogendoorn Serge P.et al., «Continuum theory for pedestrian traffic flow: Local route choice modeling and its implications » [2] about the pedestrian direction. It includes a global component determined before their start and a local one that adjusts the original direction according to local variations. 

We first compute the pedestrian direction with the fast marching method. We assume the presumption that pedestrians will use the shortest way, that is to say, the one with the lowest travel time, which takes into account the distance and the delay caused by high density. We add a local term reflecting that pedestrians will try to avoid pedestrians who do not have the same direction as them (not the same layer).

<a href=" https://github.com/Ifsttar/PedSim/blob/master/docs/Global%20and%20local%20direction.rst "> To see more about global and local direction<a/>


## Global variables and parameters used
<a href=" https://github.com/Ifsttar/PedSim/blob/master/docs/Global%20variables%20and%20parameters%20used.rst "> To see all parameters and global variables used<a/>
  
## Bibliography 
<a href=" https://github.com/Ifsttar/PedSim/blob/master/docs/Bibliography.rst "> Bibliography<a/>


# Computer programming

## Functions
<a href=" https://github.com/Ifsttar/PedSim/blob/master/docs/Functions.rst "> To see functions used <a/>
  
## General loop
<a href=" https://github.com/Ifsttar/PedSim/blob/master/docs/General%20loop.rst "> To see more about genral loop <a/>
  




.. _here: https://github.com/Ifsttar/PedSim

.. _almost compliant: index.html

.. _GPL 3 license: License.html


.. toctree::
    :maxdepth: 3
    :caption: Functionning of the platform
    
    docs/Use of the platform
    docs/Test cases
    docs/Areas of improvement
    

.. toctree::
    :maxdepth: 3
    :caption: Model and assumptions used to develop the platform

    docs/Flow equations, numerical schemes, and boundary conditions
    docs/Global and local direction
    
make html
.readthedocs.yml
Read the Docs configuration file
See https://docs.readthedocs.io/en/stable/config-file/v2.html for details



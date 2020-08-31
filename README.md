(intro, context,problem presentation)

Pedestrian traffic meets a lot of issue as daily operations optimization or management in crowded areas such as airports or train stations, or as linked to the safety and evacuation plans issues. 

We develop a platform coded in Python to model pedestrian flows. 

The built model is macroscopic dynamic, so we consider the traffic as a continuous flow, and pedestrians’ general behavior is treated by analogy to transport models in fluid dynamics. The equilibrium relation links pedestrians’ speed with their density. 

Pedestrians are divided into differents layers according to their original direction, that is to say according to their entrance and exit doors. Thus, we compute separately the pedestrian density of each layer before the global density.

# Functioning of the platform
The platform enables to describe the pedestrian traffic evolution in a network. The latter is modelised by a mesh. So, we compute the pedestrian density in each cell of the mesh for each layer. The code returns the global density at each time step. For some of them, it displays for each layer, the layer density (so the pedestrian flow for each pedestrian class), and the global density (so the general pedestrian traffic).

## Use of the platform
It is suitable to a large serie of test cases. Users can define the domain, entrances, exits, the number of layer, obstacles. 
<a href="https://github.com/Ifsttar/PedSim/blob/master/Docs/Use%20of%20the%20platform.rst "> To see more about the use of the platform <a/>
  
## Test cases
The code integrates several test cases to become aware of what the platform can provide. Thus, there are simple tests with only two layers to look precisely what happens at crossing points. We also find test cases with multiple layers and some where pedestrian demands are fluctuate over time.
<a href="https://github.com/Ifsttar/PedSim/blob/master/Docs/Test%20cases.rst"> To see more about the different test cases <a/>

## Areas of improvement
<a href="https://github.com/Ifsttar/PedSim/blob/master/Docs/Areas%20of%20improvement.rst "> To see more about areas of improvement<a/>)

# Models and assumptions used to develop the platform
## Flow equations and numerical scheme

We essentially used flow equations and numerical schemes described in Stéphane Mollier’s thesis, « Two-dimensional models for large-scale traffic networks » [1] to construct the model.

(### Time discretization
* Runge Kutta ### Space discretization * Weno scheme * splitting method)
<a href="https://github.com/Ifsttar/PedSim/blob/master/Docs/Flow%20equations%20and%20numerical%20scheme.rst "> To see more about Flow equations and numerical scheme<a/>

## Global and local direction 
We use the paper of Hoogendoorn Serge P.et al., «Continuum theory for pedestrian traffic flow: Local route choice modeling and its implications » [2] about the pedestrian direction. It includes a global component determined before their start and a local one that adjusts the original direction according to local variations.
(### Fast marching method ### global and local direction )
<a href="https://github.com/Ifsttar/PedSim/blob/master/Docs/Flow%20equations%20and%20numerical%20scheme.rst"> To see more about global and local direction<a/>

## Boundaries conditions
* Ghost cells
<a href="https://github.com/Ifsttar/PedSim/blob/master/Docs/Boundaries%20conditions.rst "> To see more about boundaries conditions <a/>

## Global variables and parameters used
<a href="https://github.com/Ifsttar/PedSim/blob/master/Docs/Global%20variables%20and%20parameters%20used.rst "> Parameters and global variables used<a/>
  
## Bibliography 
<a href="https://github.com/Ifsttar/PedSim/blob/master/Docs/Bibliography.rst"> Bibliography<a/>



# Computer programming

## Functions
<a href="https://github.com/Ifsttar/PedSim/blob/master/Docs/Functions.rst"> To see more about functions <a/>
  
## General loop
<a href="https://github.com/Ifsttar/PedSim/blob/master/Docs/General%20loop.rst"> To see more about genral loop <a/>
  
## Useful to know 
<a href="https://github.com/Ifsttar/PedSim/blob/master/Docs/Useful%20to%20know.rst "> Useful to know <a/> 

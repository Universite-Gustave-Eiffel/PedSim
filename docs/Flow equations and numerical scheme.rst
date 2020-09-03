Flow equations and numerical schemes 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We essentially used flow equations and numerical schemes described in Stéphane Mollier’s thesis, « Two-dimensional models for large-scale traffic networks » [1] to construct the model. It uses conversation laws with a two-dimensional density described in equation (1) in [1].

The model combines a time discretization with a step time dt and a space discretization with a step dx and dy. A mesh modeled the network. We compute the density for each cell of the mesh (see about the organization of all the methods). 

The density in each cell is defined as ρ_i,j.

Figures come from [1]

.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/rapports/figure%204.2%20%5B1%5D%20p%2076.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/rapports/table%201%201.png
   :align: center

Space discretization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Dimensional splitting
--------------------------

The dimensional splitting is a method that allows us to compute a two-dimensional flux by calculate it first in one dimension and then in the other. Thus, we compute the flux first in x-dimension, then all the densities are updated. Next, we calculate it in y dimension and update all the densities. 

We consider:
- p_i_j_prev the density value for the cell i,j for the layer n before we apply the dimensional splitting method, 
- p_i_j_int the density value for the cell i,j for the layer n  after we compute the density in x_dimension
- p_i_j_next the density value for the cell i,j for the layer n  after we compute the density in y_dimension
- F_i-1/2,j_prev the flux (Lax-Friedrichs Flux ) at the interface between the cell i, j, and the cell i-1, j for the layer n before we apply the dimensional splitting method.

.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/rapports/4.14.png
   :align: center
   Equation 4.14 [1]
   

Lax-Friedrichs Flux
-------------------------

We can define the flux at the interface (F_i+1/2, j) between the cell i,j and the cell i+1,j computed by the Lax-Friedrichs Flux as follow: 

.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/rapports/4.13.png
   :align: center
   equation 4.13 [1]

WENO method
----------------------

The Weighted Essentially Non-Oscillatory (WENO) method is a way to interpolate the discrete density. It is a high order numerical method that computes the density values at the interface of the cells (ρ_right and ρ_left) thanks to a spatial polynomial using the five neighboring densities. 
Thanks to the Weno method, we get the densities needed to compute the flux at the interface using the Lax-Friedrichs Flux.
We can find all formulas in [3].
This method is stable under standard CFL conditions.

Time discretization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We need a method that maintains stability.

Total Variation Diminishing (TVD) Runge-Kutta
------------------------------------------------

The TVD provides that the total variation of the solution does not increase in avoiding new extrema creation.
We use the third order. Thus there are three time steps in each step.

.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/rapports/TVD.png
   :align: center
More descriptions can be find in [5].


Boundary conditions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We use the fifth-order finite difference WENO scheme, which uses the five neighboring densities. So, we need three rows of ghost points above and below the mesh boundary and three columns of ghost points on the right and the left of the mesh boundary.

At the inflow boundary, we use an inverse Lax-Wendroff procedure that is to say we construct an Sth order approximation of ghost point values by a Taylor expression. In our code, S=4. [3]

  






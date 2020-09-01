Flow equations and numerical schemes 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We essentially used flow equations and numerical schemes described in Stéphane Mollier’s thesis, « Two-dimensional models for large-scale traffic networks » [1] to construct the model. It uses conversation laws with a two dimensional density as described in equation (1) in [1].

The model combines a time discretization with a step time dt and a space discretization with a step dx and dy. A mesh modeled the network. We compute the density for each cell of the mesh (see about the organization of all the methods). 

The density in each cell is defined as rho_i_j.

The 
Thanks to the Weno method we get densities needed to compute the flux at the interface. 
Dimensionnal splitting
TVD 

(.. figure:: lien
   :height: 600px
   :align: center)

(### Time discretization

Runge Kutta ### Space discretization * Weno scheme * splitting method) To see more about Flow equations and numerical scheme

Flow equations and numerical schemes 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We essentially used flow equations and numerical schemes described in Stéphane Mollier’s thesis, « Two-dimensional models for large-scale traffic networks » [1] to construct the model. It uses conversation laws with a two dimensional density as described in equation (1) in [1].

The model combines a time discretization with a step time dt and a space discretization with a step dx and dy. A mesh modeled the network. We compute the density for each cell of the mesh (see about the organization of all the methods). 

The density in each cell is defined as ρ_i,j.

   flux [Φ = v (vector) * ρ] = veh/s/m (vector)
   density [ρ] = veh/m2 (scalar)
   velocity [v] = m/s (vector)
   equation ∂tρ + ∇ · Φ( ~ t, x, y, ρ) = 0
   table 1.1 [1]

Space discretization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

schéma comme figure 4.2 [1] p 76

WENO method
----------------------

The Weighted Essentially Non-Oscillatory (WENO) method is a way to interpolate the discrete density. It is a high order numerical method wich computes the density values at the interface of the cells (ρ_right and ρ_left) thanks to a spatial polynomial using the five neighboring densities. 
Thanks to the Weno method we get densities needed to compute the flux at the interface using the Lax-Friedrichs Flux.
formule in [3]


Lax-Friedrichs Flux
-------------------------

We can define the flux at the interface (F_i+1/2, j) between the cell i,j and the cell i+1,j computed by the Lax-Friedrichs Flux as follow:
   F_i+1/2, j = 1/2 ( Φ(ρ_i+1_moins,j) + Φ(ρ_i_plus,j) - vmax (ρ_i_plus,j - ρ_i+1_moins,j)) 
   equation 4.13 [1]
   

Dimensionnal splitting
--------------------------


The dimensionnal splitting is a method that allows to compute a two-dimensional flux by computing first in one dimension and then in the other. Thus, we compute the flux first in x-dimension, then all the densities are updated. Next, we compute the flux in y dimension and update all the densities.

We consider:
- p_i_j_prev the density value for the cell i,j for the layer n before we apply the dimensionnal splitiing method, 
- p_i_j_int the density value for the cell i,j for the layer n  after we compute the density in x_dimension
- p_i_j_next the density value for the cell i,j for the layer n  after we compute the density in y_dimension
- F_i-1/2,j_prev the flux (Lax-Friedrichs Flux ) at the interface beetween the cell i, j and the cell i-1, j for the layer n before we apply the dimensionnal splitting method.

   Equation 4.14 [1]
   p_i_j_int = p_i_j_prev + dt/dx * (cos(teta_i-1/2,j) * F_i-1/2,j_prev - cos(teta_i+1/2,j) * F_i+1/2,j_prev)
   p_i_j_next = p_i_j_int + dt/dy * (sin(teta_i,j-1/2) * F_i,j-1/2_int - sin(teta_i,j+1/2) * F_i,j+1/2_int)
  

Time discretization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Total Variation Diminishing (TVD) Runge-Kutta
------------------------------------------------

This is a third order method.


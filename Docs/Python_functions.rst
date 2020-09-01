Get Started - Tutorial
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Functions to use the platform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


To define test case
----------------------

def test_cases ():
  if the number of the test case exists, return entrance_doors_coord, exit_doors_coord, list_direction, demand, num_layers
  else, return None
(entrance_doors_coord and exit_doors_coord are called inflows and outflows too)

To define the geometry of the domain
---------------------------------------

def create_geo():
  if the number of the geo_case exists, return domain, obstacles
  else, return None
  
To generate a rectangular finite volume grid
----------------------------------------------

def generate_mesh(domain, inflows, outflows, obstacles, num_layers):
  return mesh
(préciser tout ce que le mesh contient)

lien pour note to the user

Functions for boundaries conditions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To get time derivates of boundary conditions
----------------------------------------------

def time_derivative_bc(t, direction):
  if the number of the geo_case exists, return time_der
  else, return None
  
To compute density values in ghost cells
-------------------------------------------

def extrapolate_ghostcells(t, dt, rkstep, domain, density, demand, mesh, direction, layer):
  return density
lagrangian interpolation???
It uses time_dericative_bc (t, direction).

lien pour boundary conditions

Functions for flow equations and numerical schemes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To estimate speed thanks to the fundamental diagram
----------------------------------------------------

def estimate_speed(rho):
  return v_d
  
To compute flux
-----------------

def compute_flux(rho):
  return f
rho is a density matrix.
?????
It uses estimate_speed (rho[np.logical_and(rho <= rho_j, rho > 0)])

Functions for WENO
-------------------------------------------

- To compute smoothness indicators for WENO
def smoothness_indicator(den):
  return beta

- To build stencils for WENO
def construct_stencils(nx, ny):
  return xstencils, ystencils
 
 - To reconstruct WENO
def WENO_scheme(density, stencils):
  return np.sum(denlAll * weightL, axis=0), np.sum(denrAll * weightR, axis=0)
It uses smoothness_indicator (density)

To compute Lax_Friedrich scheme
---------------------------------

def lax_friedrich_flux(density, mesh, direction, phi_x, phi_y, xstencils, ystencils):
  return fij
It uses compute_flux (denl), compute_flux (denr), WENO_scheme (den, xstencils), WENO_scheme (phi, xstencils), WENO_scheme (den, ystencils), WENO_scheme (phi, ystencils)

Function for the dimensional splitting
---------------------------------------

def dimensional_splitting(density, F_i_j, dt, mesh, direction):
  return density

lien pour flow equations and numerical schemes

Functions for computing the direction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To compute the fast marching scheme
-------------------------------------

def crowdedness_direction(nlayers, densities, layer):
    return gradpsi
 ????????????

def fast_marching_scheme(density, mesh, layer, nlayers, densities):
  return -gradphi[1], -gradphi[0]
It uses estimate_speed(density), crowdedness_direction (nlayers, densities, layer)

To compute the direction vectors
---------------------------------
 
def compute_direction_vectors(density, mesh, theta, layer, nlayers, densities):
  return phi_x, phi_y
It uses fast_marching_scheme (density, mesh, layer, nlayers, densities)
  
General loop
~~~~~~~~~~~~~~

Time integration loop
----------------------

def time_integration(domain, mesh, demands, directions, nlayers):
  return alldensities
It uses construct_stencils (nx, ny), lax_friedrich_flux (density, mesh, dimension, phi_x, phi_y, xstencils, ystencils), dimensionnal_splitting (density, fij, dt, mesh, dimension), compute_direction_vectors(sumdensities, mesh, theta, layer, nlayers, densities)
  
Main function
----------------------

def main():

It uses test_cases (), create_geo (), generate_mesh (domain, inflows, outflows, obstacles, num_layers), time_integration(domain, mesh, demand, directions, num_layers), plot_solution(domain, solution, num_layers)


lien boucle général
  
To plot solution
~~~~~~~~~~~~~~~~~~~

To plot snapshots of solution
-------------------------------

def plot_solution(domain, solution, nlayers):

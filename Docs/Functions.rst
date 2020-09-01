Functions
^^^^^^^^^^

Functions to use the platform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To define test case
----------------------

def test_cases ():
  if the number of the test case exists, return entrance_doors_coord, exit_doors_coord, list_direction, demand, num_layers
  else, return None

To define the geometry of the domain
---------------------------------------
def create_geo():
  if the number of the geo_case exists, return domain, obstacles
  else, return None
  
To generate a rectangular finite volume grid
----------------------------------------------
def generate_mesh(domain, inflows, outflows, obstacles, nlayers):
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
?????

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

To compute Lax_Friedrich scheme
---------------------------------

def lax_friedrich_flux(density, mesh, direction, phi_x, phi_y, xstencils, ystencils):
  return fij
It uses 

Function for the dimensional splitting
---------------------------------------

def dimensional_splitting(density, F_i_j, dt, mesh, direction):
  return density

lien pour flow equations and numerical schemes

Functions for computing the direction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- def crowdedness_direction(nlayers, densities, layer):
    return gradpsi
 ????????????

To compute the fast marching scheme
-------------------------------------

def fast_marching_scheme(density, mesh, layer, nlayers, densities):
  return -gradphi[1], -gradphi[0]

To compute the direction vectors
---------------------------------
 
def compute_direction_vectors(density, mesh, theta, layer, nlayers, densities):
  return phi_x, phi_y

General loop
~~~~~~~~~~~~~~

Time integration loop
----------------------

def time_integration(domain, mesh, demands, directions, nlayers):
  return alldensities
  
Main function
----------------------

def main():

lien boucle général
  
To plot solution
~~~~~~~~~~~~~~~~~~~

To plot snapshots of solution
-------------------------------

def plot_solution(domain, solution, nlayers):

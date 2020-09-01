Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^

To define test case
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_cases ():
  if the number of the test case exists, return entrance_doors_coord, exit_doors_coord, list_direction, demand, num_layers
  else, return None
lien pour note to the user

To define the geometry of the domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def create_geo():
  if the number of the geo_case exists, return domain, obstacles
  else, return None
lien pour note to the user
  
To generate a rectangular finite volume grid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def generate_mesh(domain, inflows, outflows, obstacles, nlayers):
  return mesh
(préciser tout ce que le mesh contient)

To get time derivates of boundary conditions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def time_derivative_bc(t, direction):
  if the number of the geo_case exists, return time_der
  else, return None
lien pour boundary conditions

To compute 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To define test case
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To define test case
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

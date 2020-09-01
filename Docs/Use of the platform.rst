Use of the platform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To define the geometry of domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The domain
----------------------

Obstacles
----------------------

To define a test case
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The demand
----------------------
We can have three different phases of demand for each layer. So, the demand is a list of lists. The lenght of the list is equal to the number of layers and the lenght of each sub list is equal to three (the three possible phases of demand).

The doors 
----------------------


The initial direction
---------------------------

Layers or pedestrian class
---------------------------

What can be changed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Tmax
* some parameters and global variables (to see more put the link)
Tmax = 40.0
geo_case = 1
test_case = 6
        demand = [0.5 * rho_c * vmax * largeur_porte]  # ped/s

        # inflow
        num_entrance_doors = 1
        entrance_doors_coord = [[[[0, 0], [0, 40]]]]

        # outflow
        num_exit_doors = 1
        exit_doors_coord = [[[[20, 20], [8, 12]], [[20, 20], [28, 32]]]]

        num_mix_doors = 0

        # directions
        num_directions = 1
        list_direction = [[0]]

        # number of layers
        num_layers = 1
geo_case == 1:

        # [[x0, x1], [y0, y1]]
        domain = [[0, 20], [0, 40]]

        # give coordinates of [x0, xn] and [y0, yn]
        obstacles = []

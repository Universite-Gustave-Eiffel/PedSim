Use of the platform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To define the geometry of domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The domain
----------------------
Domain is a list of two lists. The first sub list gives the x coordinates of the domain and the second one the y coordinates.

        domain = [[x0, X1], [y0, y1]]

Obstacles
----------------------
Obstacles is a list of lists. The lenght is equal to the obstcales number. For each one, we give a list of two lists. The first sub list gives the x coordinates of the door and the second one the y coordinates.

        If there are not obstacles, Obstacles = [] 
        Else, Obstacles =  [[[x0, xn for the obstacle 1], [y0, yn for the obstacle 1]],..., [[x0, xn for the obstacle m], [y0, yn for the obstacle m]]]

To define a test case
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The demand
----------------------
We can have three different phases of demand for each layer. So, the demand is a list of lists. The lenght of the list is equal to the number of layers and the lenght of each sub list is equal to three (the three possible phases of demand). 

        demand = [[first demand phase for the layer 1, second demand phase for the layer 1, third demand phase for the layer 1],...,[first demand phase for the layer n, second demand phase for the layer n, third demand phase for the layer n]]

The doors 
----------------------
We have to define the number of entrance doors and exit doors and their coordinated. For each layer we have to give an entrance and an exit door even if they are the same. Each door are defined by a list of two lists. The first sub list gives the x coordinates of the door and the second one the y coordinates. Thus, entrance_doors_coord and exit_doors_coord are a list of the different doors.

        entrance_doors_coord = [[[xo , xn for the layer 1], [yo, yn for the layer 1]],..., [[xo , xn for the layer n], [yo, yn for the layer n]]]

The initial direction
---------------------------
l'enlever à priori????

The number of layers or pedestrian class
------------------------------------------
We give the number of the layer.

        num_layers = n


        l'exemple
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

What can be changed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We have to put the number of the test case, the number of the geo case we want to run and Tmax.
There are some parameters you can change too (see more about parameters).
 


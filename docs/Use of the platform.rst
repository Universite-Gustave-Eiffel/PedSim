Use of the platform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To define the domain geometry.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To define a new domain geometry, you have to create a new geo_case in the create geo_case() function where you define the domain dimensions and obstacles. Then, you have to change the number of the geo case you run in parameters you can change.

The domain
----------------------

Domain is a list of two lists. The first sub-list gives the x coordinates of the domain and the second one the y coordinates as shown below.

        domain = [[x0, X1], [y0, y1]]

Obstacles
----------------------

Obstacles is a list of lists. The length is equal to the number of obstacles. For each one, we give a list of two lists. The first sub-list gives the x coordinates of the door and the second one the y coordinates.

        If there are not obstacles, Obstacles = [] 
        Else, Obstacles =  [[[x0, xn for the obstacle 1], [y0, yn for the obstacle 1]],..., [[x0, xn for the obstacle m], [y0, yn for the obstacle m]]]
        
instance of a test case defined in the create_geo() function
-----------------------------------------------------------
        
        if geo_case == 1:

                # [[x0, x1], [y0, y1]]
                domain = [[0, 20], [0, 40]]

                # give coordinates of [x0, xn] and [y0, yn]
                obstacles = []
        

To define a test case
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To define a new test case, you have to create a new one in the test_case() function where you define the demand, the doors coordinates, directions of the different layers, and their number. Then, you have to change the number of the test case you run in parameters you can change. You have to add the number of your test case in the list of the test cases defined in the time_derivative_bc(t, direction) function.

The demand
----------------------

We can have three different phases of demand for each layer. So, demand is a list of lists. The length of the list is equal to the number of layers, and the size of each sub-list is equal to three (the three possible phases of demand), as shown below. 

        demand = [[first demand phase for the layer 1, second demand phase for the layer 1, third demand phase for the layer 1],...,[first demand phase for the layer n, second demand phase for the layer n, third demand phase for the layer n]]
        
The doors 
----------------------

We have to define the number of entrance doors and exit doors and their coordinates. We have to give each layer an entrance and an exit door even if they are the same. A list of two lists defines each door. The first sub-list gives the x coordinates of the door and the second one the y coordinates. Thus, entrance_doors_coord and exit_doors_coord are a list of different doors.

        entrance_doors_coord = [[[xo , xn for the layer 1], [yo, yn for the layer 1]],..., [[xo , xn for the layer n], [yo, yn for the layer n]]]

The direction
---------------------------

You have to precise the number of directions, that is to say, the number of layers. You have to give an initial direction as a list of directions, as shown below in the instance.
        
        num_directions = the number of layers = 2 
        list_direction = [[0], [math.pi * 0.5]]

The number of layers or pedestrian class
------------------------------------------

We give the number of the layer, as shown below.

        num_layers = n


Instance of a test case defined in the test_case() function:
-------------------------------------------------------------------

        if test_case == 1:

                demand = [[0.5 * rho_c * vmax * largeur_porte, 0.5* rho_c * vmax * largeur_porte,0.5 * rho_c * vmax * largeur_porte],[0.5 * rho_c * vmax * largeur_porte, 0.5 * rho_c * vmax * largeur_porte,0.5 * rho_c * vmax * largeur_porte]] # ped/s

                # inflow
                num_entrance_doors = 2
                entrance_doors_coord = [[[[0, 0], [18, 22]]], [[[8, 12], [0, 0]]]]

                # outflow
                num_exit_doors = 2
                exit_doors_coord = [[[[20, 20], [18, 22]]], [[[8, 12], [40, 40]]]]

                # directions
                num_directions = 2
                list_direction = [[0], [math.pi * 0.5]]

                # number of layers
                num_layers = 2
        
       
What can be changed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You have to put the number of the test case and of the geo case you want to run. You have to define a Tmax too.
There are some parameters you can change too (see more about it in https://github.com/Ifsttar/PedSim/blob/master/docs/Global%20variables%20and%20parameters%20used.rst).
 


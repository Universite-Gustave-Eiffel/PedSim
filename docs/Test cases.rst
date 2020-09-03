Test cases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

<a href="https://github.com/Ifsttar/PedSim/blob/master/docs/Areas%20of%20improvement.rst"> To learn more about areas of improvement paths <a/>
There are test cases predefined to see what the platform can do.
Lien pour indications sur ce qu'il faut changer

The default value of alpha_d is 0.75. It is the weight on crowdedness in direction computation, to learn more about it, see https://github.com/Ifsttar/PedSim/blob/master/docs/Global%20variables%20and%20parameters%20used.rst <a href="https://github.com/Ifsttar/PedSim/blob/master/docs/Global%20variables%20and%20parameters%20used.rst"> Global variables and parameters used<a/>, <a href="https://github.com/Ifsttar/PedSim/blob/master/docs/Functions.rst"> Functions used <a/> and <a href="https://github.com/Ifsttar/PedSim/blob/master/docs/Global%20and%20local%20direction.rst"> Global and local direction<a/>). 
We will specify when we use another alpha_d value in the test case descriptions.
We use parameters or global variables defined in <a href="https://github.com/Ifsttar/PedSim/blob/master/docs/Global%20variables%20and%20parameters%20used.rst"> Global variables and parameters used<a/>.

Test_case == 1: the cross with demand constant over time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two different layers: one for pedestrians who go from north to south and one for those who go from west to east.
The demand is constant over time, the same for both layers, and equal to 0.5 * rho_c * Vmax * largeur_porte ped/s.

Geo_case 1: Without any obstacles
------------------------------------

* alpha = 0.4
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case1/alpha%20%3D%200.4/Figure_5.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case1/alpha%20%3D%200.4/Figure_10.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case1/alpha%20%3D%200.4/Figure_15.png
   :align: center
   

Geo_case 2: With an obstacle in the middle
--------------------------------------------------

.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case_2/geo%20case%202/Figure_5.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case_2/geo%20case%202/Figure_15.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case_2/geo%20case%202/Figure_20.png
   :align: center


Geo_case 3: With corridors
---------------------------------

.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case_3/alpha%20%3D%200.75/alpha%20%3D%200.75/Figure_5.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case_3/alpha%20%3D%200.75/alpha%20%3D%200.75/Figure_15.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case_3/alpha%20%3D%200.75/alpha%20%3D%200.75/Figure_20.png
   :align: center


Test_case == 2: the cross with demand not constant over time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two different layers: one for pedestrians who go from north to south and one for those who go from west to east.
The demand is the same for the two entrance doors.

If 0 <= t <= Tmax/3 (20 s) :  demand = 0.8 * rho_c * vmax * largeur_porte ped/S
Elif Tmax/3 < t <= 2 * Tmax/3 (40 s) : demand = 0.1* rho_c * vmax * largeur_porte ped/s
Elif 2*Tmax/3 < t <=Tmax (60 s) : demand = 0.5 * rho_c * vmax * largeur_porte ped/s


Geo_case 1: Without any obstacles 
-----------------------------------------

.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test%20case%203%20geo%20case%201%20alpha%20%3D%200.75/Figure_3.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test%20case%203%20geo%20case%201%20alpha%20%3D%200.75/Figure_8.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test%20case%203%20geo%20case%201%20alpha%20%3D%200.75/Figure_13.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test%20case%203%20geo%20case%201%20alpha%20%3D%200.75/Figure_18.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test%20case%203%20geo%20case%201%20alpha%20%3D%200.75/Figure_23.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test%20case%203%20geo%20case%201%20alpha%20%3D%200.75/Figure_28.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test%20case%203%20geo%20case%201%20alpha%20%3D%200.75/Figure_33.png
   :align: center


Test case == 3: the diagonal cross 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two different layers: one for pedestrians who go from north west to south east and one for those who go from east to south west.
The demand is constant over time, the same for the both layers and equal to 0.5 * rho_c * vmax * largeur_porte ped/s.

Geo_case 1: Without any obstacles
-----------------------------------

* alpha = 0.75
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/Test%20case%203/test%20case%203%20geo%20case%201%20alpha%20%3D%200.75/Figure_8.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/Test%20case%203/test%20case%203%20geo%20case%201%20alpha%20%3D%200.75/Figure_15.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/Test%20case%203/test%20case%203%20geo%20case%201%20alpha%20%3D%200.75/Figure_21.png
   :align: center

* alpha = 0.1
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/Test%20case%203/Test%20case%203%20geo%20case%201%20alpha%20%3D%200.1/Figure_8.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/Test%20case%203/Test%20case%203%20geo%20case%201%20alpha%20%3D%200.1/Figure_15.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/Test%20case%203/Test%20case%203%20geo%20case%201%20alpha%20%3D%200.1/Figure_21.png
   :align: center


Test case == 4: Horizontal crossing flows 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two different layers: one for pedestrians who go from west to east and one for thoses wo go from east to west.
The demand is constant over time, the same for the both layers and equal to 0.5 * rho_c * vmax * largeur_porte ped/s.

Geo_case 1: Without any obstacles
------------------------------------------

* alpha = 0.75
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/Test%20case%204/geo%20case%201%20alpha%20%3D%200.75/Figure_8.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/Test%20case%204/geo%20case%201%20alpha%20%3D%200.75/Figure_15.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/Test%20case%204/geo%20case%201%20alpha%20%3D%200.75/Figure_21.png
   :align: center

* alpha = 0.1
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/Test%20case%204/geo%20case%201%20alpha%20%3D%200.1/Figure_8.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/Test%20case%204/geo%20case%201%20alpha%20%3D%200.1/Figure_15.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/Test%20case%204/geo%20case%201%20alpha%20%3D%200.1/Figure_21.png
   :align: center
   

Test case == 5: multilayers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are four different layers: one for pedestrians who go from west to east, one for those from east to west, one for those from north to south and one for those from south to north.
The demand is constant over time, the same for the both layers and equal to 0.5 * rho_c * vmax * largeur_porte ped/s.

Geo_case 1: Without any obstacles
------------------------------------------

* alpha = 0.75
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/Test%20case%205%20geo%20case%201%20alpha%20%3D%200.75/Figure_2.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/Test%20case%205%20geo%20case%201%20alpha%20%3D%200.75/Figure_8.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/Test%20case%205%20geo%20case%201%20alpha%20%3D%200.75/Figure_14.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/Test%20case%205%20geo%20case%201%20alpha%20%3D%200.75/Figure_20.png
   :align: center


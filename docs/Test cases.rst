Test cases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are test cases predefined to see what the platform can do.
Lien pour indications sur ce qu'il faut changer

Default value of alpha_d (weight on crowdedness in direction computation  lien paramètres) is 0.75. It would be precised in test cases descriptions when we use an another alpha_d value.
For any parameters or global see (lien paramètres) we use these ones

Test_case == 1: the cross with demand constant over time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two different layers: one for pedestrians who go from north to south and one for thoses wo go from west to east.
The demand is constant over time, the same for the both layers and equal to 0.5 * rho_c * vmax * largeur_porte ped/s.


Geo_case 1: Without any obstacles
------------------------------------

* alpha = 0.4
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case1/alpha%20%3D%200.4/Figure_5.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case1/alpha%20%3D%200.4/Figure_10.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case1/alpha%20%3D%200.4/Figure_15.png
   :align: center



Geo_case 2: With an obtacle in the middle
--------------------------------------------------

.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case_2/geo%20case%202/Figure_5.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case_2/geo%20case%202/Figure_15.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case_2/geo%20case%202/Figure_20.png
   :align: center


Geo_case 3: With corridors defines
--------------------------------------------

* alpha = 0.75

.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case_3/alpha%20%3D%200.75/alpha%20%3D%200.75/Figure_5.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case_3/alpha%20%3D%200.75/alpha%20%3D%200.75/Figure_15.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case_3/alpha%20%3D%200.75/alpha%20%3D%200.75/Figure_20.png
   :align: center

* alpha = 0.1

.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case_3/alpha%20%3D%200.1/alpha%20%3D%200.1/Figure_5.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case_3/alpha%20%3D%200.1/alpha%20%3D%200.1/Figure_15.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case_3/alpha%20%3D%200.1/alpha%20%3D%200.1/Figure_25.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case_3/alpha%20%3D%200.1/alpha%20%3D%200.1/Figure_35.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test_case%201/geo_case_3/alpha%20%3D%200.1/alpha%20%3D%200.1/Figure_45.png
   :align: center


Test_case == 2: the cross with demand not constant over time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two different layers: one for pedestrians who go from north to south and one for thoses wo go from west to east.
The demand is the same for the two entrance doors.

If 0 <= t <= Tmax/3 (20 s) :  demand = 0.8 * rho_c * vmax * largeur_porte ped/S
Elif Tmax/3 < t <= 2 * Tmax/3 (40 s) : demand = 0.1* rho_c * vmax * largeur_porte ped/s
Elif 2*Tmax/3 < t <=Tmax (60 s) : demand = 0.5 * rho_c * vmax * largeur_porte ped/s


Geo_case 3: With corridors defines
-----------------------------------------

* alpha = 0.1
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test%20case%202%20geo_case%203%20alpha%3D%200.1/Figure_5.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test%20case%202%20geo_case%203%20alpha%3D%200.1/Figure_10.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test%20case%202%20geo_case%203%20alpha%3D%200.1/Figure_15.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test%20case%202%20geo_case%203%20alpha%3D%200.1/Figure_20.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test%20case%202%20geo_case%203%20alpha%3D%200.1/Figure_25.png
   :align: center
.. figure:: https://github.com/Ifsttar/PedSim/blob/master/docs/images/test%20case%202%20geo_case%203%20alpha%3D%200.1/Figure_30.png
   :align: center



Test case == 3: the diagonal cross
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Geo_case 1: Without any obstacles
-----------------------------------

Test case == 4: bidirectionnel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Geo_case 1: Without any obstacles
------------------------------------------

Geo_case 2: With an obtacle in the middle
------------------------------------------------

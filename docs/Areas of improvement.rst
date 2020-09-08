Areas of improvement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

What we can add on the code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Stairs or lifts
----------------------

To improve the code, we could add stairs or lifts, that is to say, to have entrance and exit doors not only in the network boundary but also inside this one. Thus, we could generate or computed inflows and outlows inside the mesh.

Pedestrians counter
----------------------

For now, we only test the code with demands supposed to be handled by our network. But, we could imagine a pedestrian counter which does not let them enter where the demand is too high and remember those awaiting to enter to let them when the demand becomes lesser.


On model assumptions 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Other pedestrian class types
--------------------------------

We assume that pedestrians with the same destination have the same behavior, so the same class. We could imagine other factors influencing their behavior. Thus, in Delft paper [2], they propose constructing and adding different class types to these class definitions as walking purpose, age, gender, etc.

The fact that pedestrians will choose the travel with the minimum cost
--------------------------------------------------------------------------

Pedestrians can't compute as the fast marching method the different travel times, and they have not necessarily the same standards to determine a travel cost. Maybe, some of them prefer to take more time but avoid as much as possible other pedestrians even if they have to make a considerable detour.





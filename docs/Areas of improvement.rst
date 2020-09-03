Areas of improvement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

What we can add on the code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Stairs or lifts
----------------------

The next steps to improve the code would be to model stairs or lifts that is to say to have entrance and exit doors not only in the network boundary but also inside this one. Thus, we could generated or computed inflows and inflows inside the mesh.

Pedestrians counter
----------------------

For now, we only test the code with demands supposed to be handled by our network. But, we could imagine a pedestrian counter wich does not let them enter where the demand is to high and remeber those awaiting to enter to let them  when the demand become lesser.


On model assumptions 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Other pedestrian class types
--------------------------------

We assume that pedestrians with the same destination have the same behaviour so are in the same class. We could imagine other factors influating their behaviour. Thus, in Delft paper [2], they propose to construct and add other class types to these class definition as walking purpose, age, gender, etc.

The fact that pedestrians will choose the travel with the minimum cost
--------------------------------------------------------------------------

Pedestrians can't compute as the fast marching methood the different travel times and they have not necessarily the same standards to determine a travel cost. Maybe, some of them prefere to take more time but avoid as much as possible other pedestrians even if they have to make a large detour.





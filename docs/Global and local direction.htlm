Global and local direction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use the paper of Hoogendoorn Serge P.et al., «Continuum theory for pedestrian traffic flow: Local route choice modeling and its implications » [2] about the pedestrian direction. 
The model is based on the assumption that pedestrians will try to minimise locally their travel cost and it presumes that pedestrians with the same destination behave the same way. So, pedestrians are divised in class depending on their destination.

Global and local direction's theory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The direction includes a global component determined before their start and a local one that adjusts the original direction according to local variations. 

equation 

Global direction
----------------------

A pedestrian class d has the same origin and destination desbribed in the global value direction. It is determined before the pedestrians trip start so it excludes the moving of traffic conditions.

Local direction
----------------------

So,a local value fonction is introduced. It presumes that flow conditions depend on the different class-specific densities. Thus, interactions between pedestrians of the same class and theses between the different class impact the travel cost. Therefore the local value fonction includes a crowdedness and a delay factor.

equation (15) [2]

* The crowdedness factor translated interactions between the different pedestrians class. They will go to areas where the density of pedestrian class d is the smallest and they will try harder to avoid pedestrians of other class than their own.
equation (17) [3]

*The delay factor reflects the fact that pedestrians will avoid areas where high density values according to the density gradient.



Global and local direction in the code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We first compute the pedestrian direction with the fast marching method. We assume the presumption that pedestrians will use the shortest way, that is to say, the one with the lowest travel time, which takes into account the distance and the delay caused by high density. We add a local term reflecting that pedestrians will try to avoid pedestrians who do not have the same direction as them (not the same layer).

Fast marching method
----------------------

Thus, we compute pedestrian direction with the fast marching method wich is used to find the travel, with the lowest travel time, between the origin and the destination of the pedestriian class. The travel times are depending on distance and on speed. So, in each mesh cell we compute the travel time with the distance between it and a door cell, and according to the speed cell computed with the fundamental diagramm so depending on the density cell. 

At each TVD step, we apply the fast marching method. Therefore, direction is adjusted at the sime time that density values evolue. So, our fast marchin method includes the delay factors described before.

Crowdedness term
----------------------

We had a crowdedness term as described in [2]. The combination between the two terms of the local value functions and with the global value function can't be the same as in [2]. 


lien pour fonction, paramètres, théorie...


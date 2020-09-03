Global and local direction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use the paper of Hoogendoorn Serge P.et al., «Continuum theory for pedestrian traffic flow: Local route choice modeling and its implications » [2] about the pedestrian direction. 
The model is based on the assumption that pedestrians will try to minimize their travel costs locally, and it presumes that pedestrians with the same destination behave the same way. So, pedestrians are divided into classes depending on their destination.

Global and local direction's theory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

According to local variations, the direction includes a global component determined before starting and a local one that adjusts the original orientation. 

equation 

Global direction
----------------------

All pedestrians in class d have the same origin and destination. The travel, which links them, is described by the global value direction and is determined before the pedestrians trip start, so it excludes traffic conditions variations.

Local direction
----------------------

So, a local value function is introduced. It presumes that flow conditions depend on the different class-specific densities. Thus, interactions between pedestrians of the same class and theses between the different classes impact travel costs. Therefore the local value function includes a crowdedness and a delay factor (see equation (15) in [2]).


* The crowdedness factor translated interactions between the different pedestrians class. They will go to areas where the density of pedestrian class d is the smallest, and they will try harder to avoid pedestrians of other classes than their own (see equation (17) in [2]).

*The delay factor reflects the fact that pedestrians will avoid areas where high-density values according to the density gradient (see equation (18) in [2]).


The global and local direction in the code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We first compute the pedestrian direction with the fast marching method. We assume the presumption that pedestrians will use the shortest way, that is to say, the one with the lowest travel time, which takes into account the distance and the delay caused by high density. We add a local term reflecting that pedestrians will try to avoid pedestrians who do not have the same direction as them (not the same layer).

Fast marching method
----------------------

Thus, we compute pedestrian direction with the fast marching method, which is used to find the travel, with the lowest travel time, between the origin and the pedestrian class's destination. The travel times are depending on distance and speed. In each mesh cell, we compute the travel time according to the distance until a door cell and the speed cell calculated with the fundamental diagram so depending on the density cell. 

At each TVD step, we apply the fast marching method. Therefore, the direction is adjusted at the same time that density values evolve. So, our fast marching method includes the delay factors described before.

Crowdedness term
----------------------

We had a crowdedness term, as described in [2]. We add the crowdedness term to the term computes by the fast marching method. We name alpha_d  weight on crowdedness in direction computation.


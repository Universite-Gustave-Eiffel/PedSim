Global and local direction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use the paper of Hoogendoorn Serge P.et al., «Continuum theory for pedestrian traffic flow: Local route choice modeling and its implications » [2] about the pedestrian direction. It includes a global component determined before their start and a local one that adjusts the original direction according to local variations. Pedestrians are divised in class depending on their destination. The model is based on the assumption that pedestrians will try to minimise locally their travel cost and it presumes that pedestrians with the same destination behave the same way.

Global direction
----------------------

Local direction
----------------------



The local value fonction includes a crowdedness and a delay factor.

Global and local direction's theory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



Global and local direction in the code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We first compute the pedestrian direction with the fast marching method. We assume the presumption that pedestrians will use the shortest way, that is to say, the one with the lowest travel time, which takes into account the distance and the delay caused by high density. We add a local term reflecting that pedestrians will try to avoid pedestrians who do not have the same direction as them (not the same layer).

Fast marching method
----------------------


Crowdedness term
----------------------


Global and local direction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use the paper of Hoogendoorn Serge P.et al., «Continuum theory for pedestrian traffic flow: Local route choice modeling and its implications » [2] about the pedestrian direction. It includes a global component determined before their start and a local one that adjusts the original direction according to local variations. 

We first compute the pedestrian direction with the fast marching method. We assume the presumption that pedestrians will use the shortest way, that is to say, the one with the lowest travel time, which takes into account the distance and the delay caused by high density. We add a local term reflecting that pedestrians will try to avoid pedestrians who do not have the same direction as them (not the same layer).


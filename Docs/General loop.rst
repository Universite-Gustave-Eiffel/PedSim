General loop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Extrapolation
We described here how the general loop of the algorithm is organized. To compute the global density at each step time, we compute the density of each layer, that is to say the density in each cell of the layer's mesh. We compute the density in each cell for the three step of the TVD Runge Kutta (to see more about time discretization).
    We compute them for the two step of the dimensionnal splitting (in x direction, then in y direction). (to see more about space discretization and dimensionnal splitting).
      Extrapolation with WENO scheme and Lax Friedrich flux two times to get flux moins flux prev and then the density.
  

mettrelien pour fonctions, schémas numériques et directions

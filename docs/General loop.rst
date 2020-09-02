General loop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We described here how the general loop of the algorithm is organized. 

At each step time, we compute the global density. We compute indeed the density of each layer, that is to say the density in each cell of the layer's mesh. Then We add each layer's density to get the global density.

    We compute the density in each cell for the three step of the TVD Runge Kutta (to see more about time discretization).
        
        For each step, we compute the (global and local) direction vectors (to see more about). Then we apply the dimensional splitting (to see more about).
        
            For each dimension (x direction and y direction), we compute flux in each cell thank to Lax Friedrich flux and Weno extrapolation to compute the density (to see more about). 
    
 
 See more in functions

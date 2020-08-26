Global variables and parameters ued
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Global variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

rho_j = 2.4 ped/m^2
rho_c = 1.2 ped/m^2
vmax = 1.34 m/s
w = rho_c * vmax / (rho_j - rho_c)  m/s
largeur_porte = 1 m

Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Crowdedness model parameters
------------------------------

crwd = 1  # include crowdedness model
alpha_d = 1  # weight on crowdedness in direction computation
B = 0.5  # rate at which interaction reduces as function of distance
lmbda = 0.2  # anisotropy parameter [0,1]
W = 1  # radius of influence of other pedestrians >= 0
alpha_0 = vmax / rho_j
beta_0 = 2 * B * ((1 + lmbda) / (1 - lmbda)) * alpha_0


Weno parameters
---------------------------
nghost_nodes = 3
weno_k = 3

drL = np.array([0.1, 0.6, 0.3]).reshape(-1, 1)
drR = np.array([0.3, 0.6, 0.1]).reshape(-1, 1)

coeff = np.array([[1.8333, -1.1667, 0.3333],
                  [0.3333, 0.8333, -0.1667],
                  [-0.1667, 0.8333, 0.3333],
                  [0.3333, -1.1667, 1.8333]])

epsilon = 10 ** -6

Others
-----------------
dx = 0.5
dy = dx

cfl = 0.5



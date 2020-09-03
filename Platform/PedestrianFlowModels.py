# -*- coding: utf-8 -*-
__author__ = 'eleonore/mahendra'

import numpy as np
import matplotlib.pyplot as plt
import math
import skfmm


## to the user


# network's length and width
# the network is represented by a rectangle
# divided in smaller rectangles
# some of them could represented obstacles

geo_case = 1
test_case = 1

dx = 0.5
dy = dx

cfl = 0.5

# FMM
fmm = 1

# Weno parameters
nghost_nodes = 3
weno_k = 3

drL = np.array([0.1, 0.6, 0.3]).reshape(-1, 1)
drR = np.array([0.3, 0.6, 0.1]).reshape(-1, 1)

coeff = np.array([[1.8333, -1.1667, 0.3333],
                  [0.3333, 0.8333, -0.1667],
                  [-0.1667, 0.8333, 0.3333],
                  [0.3333, -1.1667, 1.8333]])

epsilon = 10 ** -6

# RK3 coefficients
tvdRK = [[0, 1], [3 / 4, 1 / 4], [1 / 3, 2 / 3]]

# global variables
rho_j = 2.4  # ped/m^2
rho_c = 1.2  # ped/m^2
vmax = 1.34  # m/s
w = rho_c * vmax / (rho_j - rho_c)  # m/s
largeur_porte = 1  # m

# crowdedness model parameters
crwd = 1  # include crowdedness model
alpha_d = 0.75  # weight on crowdedness in direction computation
B = 0.5  # rate at which interaction reduces as function of distance
lmbda = 0.2  # anisotropy parameter [0,1]
W = 1  # radius of influence of other pedestrians >= 0
alpha_0 = vmax / rho_j
beta_0 = 2 * B * ((1 + lmbda) / (1 - lmbda)) * alpha_0

# Final time
Tmax = 40.0

## Functions
# define test cases here
def test_cases():
    if test_case == 1:

        demand = [[0.5 * rho_c * vmax * largeur_porte, 0.5* rho_c * vmax * largeur_porte,0.5 * rho_c * vmax * largeur_porte],[0.5 * rho_c * vmax * largeur_porte, 0.5 * rho_c * vmax * largeur_porte,0.5 * rho_c * vmax * largeur_porte]] # ped/s

        # inflow
        num_entrance_doors = 2
        entrance_doors_coord = [[[[0, 0], [18, 22]]], [[[8, 12], [0, 0]]]]

        # outflow
        num_exit_doors = 2
        exit_doors_coord = [[[[20, 20], [18, 22]]], [[[8, 12], [40, 40]]]]

        # directions
        num_directions = 2
        list_direction = [[0], [math.pi * 0.5]]

        # number of layers
        num_layers = 2

    elif test_case == 2:

        demand = [[0.1 * rho_c * vmax * largeur_porte, 0.8* rho_c * vmax * largeur_porte,0.5 * rho_c * vmax * largeur_porte],[0.1 * rho_c * vmax * largeur_porte, 0.8 * rho_c * vmax * largeur_porte,0.5 * rho_c * vmax * largeur_porte]] # ped/s

        # inflow
        num_entrance_doors = 2
        entrance_doors_coord = [[[[0, 0], [18, 22]]], [[[8, 12], [0, 0]]]]

        # outflow
        num_exit_doors = 2
        exit_doors_coord = [[[[20, 20], [18, 22]]], [[[8, 12], [40, 40]]]]

        # directions
        num_directions = 2
        list_direction = [[0], [math.pi * 0.5]]

        # number of layers
        num_layers = 2

    elif test_case == 3:

        demand = [[0.5 * rho_c * vmax * largeur_porte, 0.5* rho_c * vmax * largeur_porte,0.5 * rho_c * vmax * largeur_porte],[0.5 * rho_c * vmax * largeur_porte, 0.5 * rho_c * vmax * largeur_porte,0.5 * rho_c * vmax * largeur_porte]] # ped/s

        # inflow
        num_entrance_doors = 2
        entrance_doors_coord = [[[[0, 0], [0, 4]]], [[[20, 20], [0, 4]]]]

        # outflow
        num_exit_doors = 2
        exit_doors_coord = [[[[20, 20], [36, 40]]], [[[0, 0], [36, 40]]]]

        # directions
        num_directions = 2
        list_direction = [[0], [math.pi * 0.5]]

        # number of layers
        num_layers = 2

    elif test_case == 4:

        demand = [[0.5 * rho_c * vmax * largeur_porte, 0.5* rho_c * vmax * largeur_porte,0.5 * rho_c * vmax * largeur_porte],[0.5 * rho_c * vmax * largeur_porte, 0.5 * rho_c * vmax * largeur_porte,0.5 * rho_c * vmax * largeur_porte]] # ped/s

        # inflow
        num_entrance_doors = 2
        entrance_doors_coord = [[[[20, 20], [18, 22]]], [[[0, 0], [18, 22]]]]

        # outflow
        num_exit_doors = 2
        exit_doors_coord = [[[[0, 0], [18, 22]]], [[[20, 20], [18, 22]]]]

        num_mix_doors = 0

        # directions
        num_directions = 2
        list_direction = [[- math.pi], [0]]

        # number of layers
        num_layers = 2


    elif test_case == 5:

        demand = [[0.5 * rho_c * vmax * largeur_porte, 0.5* rho_c * vmax * largeur_porte,0.5 * rho_c * vmax * largeur_porte],[0.5 * rho_c * vmax * largeur_porte, 0.5 * rho_c * vmax * largeur_porte,0.5 * rho_c * vmax * largeur_porte],[0.5 * rho_c * vmax * largeur_porte, 0.5* rho_c * vmax * largeur_porte,0.5 * rho_c * vmax * largeur_porte],[0.5 * rho_c * vmax * largeur_porte, 0.5 * rho_c * vmax * largeur_porte,0.5 * rho_c * vmax * largeur_porte]]  # ped/s

        # inflow
        num_entrance_doors = 4
        entrance_doors_coord = [[[[20, 20], [18, 22]]], [[[8, 12], [0, 0]]], [[[0, 0], [18, 22]]], [[[8, 12], [40, 40]]]]

        # outflow
        num_exit_doors = 4
        exit_doors_coord = [[[[0, 0], [18, 22]]], [[[8, 12], [40, 40]]], [[[20, 20], [18, 22]]],
                            [[[8, 12], [0, 0]]]]


        # directions
        num_directions = 4
        list_direction = [[- math.pi], [math.pi * 0.5], [0], [- math.pi * 0.5]]

        # number of layers
        num_layers = 4

    else:
        return None

    return entrance_doors_coord, exit_doors_coord, list_direction, demand, num_layers


# define geometry of domain here
def create_geo():

    if geo_case == 1:

        # [[x0, x1], [y0, y1]]
        domain = [[0, 20], [0, 40]]

        # give coordinates of [x0, xn] and [y0, yn]
        obstacles = []

    elif geo_case == 2:

        # [[x0, x1], [y0, y1]]
        domain = [[0, 20], [0, 40]]

        # give coordinates of [x0, xn] and [y0, yn]
        obstacles = [[[8, 12], [18, 22]]]

    elif geo_case == 3:

        # [[x0, x1], [y0, y1]]
        domain = [[0, 20], [0, 40]]

        # give coordinates of [x0, xn] and [y0, yn]
        obstacles = [[[0, 8], [0, 18]],[[12,20],[0,18]],[[0, 8], [22, 40]],[[12,20],[22,40]]]

    else:
        return None

    return domain, obstacles


# generate a rectangular finite volume grid

def generate_mesh(domain, inflows, outflows, obstacles, nlayers):

    [[x0, xn], [y0, yn]] = domain

    lenX = (xn + nghost_nodes * dx) - (x0 - nghost_nodes * dx)
    lenY = (yn + nghost_nodes * dx) - (y0 - nghost_nodes * dx)

    nx = int(lenX / dx)
    ny = int(lenY / dy)

    x = np.linspace(x0 - nghost_nodes * dx, xn + nghost_nodes * dx, nx + 1)
    y = np.linspace(y0 - nghost_nodes * dx, yn + nghost_nodes * dx, ny + 1)

    xmid = 0.5 * (x[:-1] + x[1:])
    ymid = 0.5 * (y[:-1] + y[1:])

    xe, ye = np.meshgrid(x, y, indexing='xy')
    edges = [xe, ye]

    xc, yc = np.meshgrid(xmid, ymid, indexing='xy')
    centers = [xc, yc]

    leftX = np.arange(weno_k - 1, nx - weno_k)
    rightX = leftX + 1

    leftY = np.arange(weno_k - 1, ny - weno_k)
    rightY = leftY + 1

    intX = np.arange(weno_k, nx - weno_k)
    intY = np.arange(weno_k, ny - weno_k)

    internal = np.zeros(xc.shape, dtype=int)
    internal[np.ix_(intY, intX)] = 1

    domain = np.zeros((xe.shape[0], xe.shape[1], nlayers), dtype=int)
    obsFX = []
    obsFY = []

    for i in range(np.size(xe, 0)):
        for j in range(np.size(ye, 1)):
            for layer in range(nlayers):
                for ninf, inflow in enumerate(inflows[layer]):
                    [[x1, x2], [y1, y2]] = inflow
                    if x1 <= xe[i, j] <= x2 and y1 <= ye[i, j] <= y2:
                        if x1 == x2:
                            domain[i, j, layer] = 1
                        elif y1 == y2:
                            domain[i, j, layer] = 2
                for noutf, outflow in enumerate(outflows[layer]):
                    [[x1, x2], [y1, y2]] = outflow
                    if x1 <= xe[i, j] <= x2 and y1 <= ye[i, j] <= y2:
                        if x1 == x2:
                            domain[i, j, layer] = 3
                        elif y1 == y2:
                            domain[i, j, layer] = 4

                for obstacle in obstacles:
                    [[x1, x2], [y1, y2]] = obstacle
                    if x1 <= xe[i, j] <= x2 and y1 <= ye[i, j] <= y2:
                        obsFX.append(j - weno_k)
                        obsFY.append(i - weno_k)
                        domain[i, j, layer] = 5

    obsFX = np.array(sorted(set(obsFX)))
    obsFY = np.array(sorted(set(obsFY)))
    intObsX = obsFX[:-1]
    intObsY = obsFY[:-1]

    if obsFX.size > 0:
        internal[np.ix_(intObsY + weno_k, intObsX + weno_k)] = -1

    mesh = dict()
    mesh['nx'] = nx
    mesh['ny'] = ny

    mesh['faces'] = edges
    mesh['cells'] = centers

    mesh['leftX'] = leftX
    mesh['rightX'] = rightX

    mesh['leftY'] = leftY
    mesh['rightY'] = rightY

    mesh['intX'] = intX
    mesh['intY'] = intY

    mesh['interior'] = internal
    mesh['domain'] = domain

    mesh['obsFX'] = obsFX
    mesh['obsFY'] = obsFY

    mesh['intObsX'] = intObsX
    mesh['intObsY'] = intObsY

    mesh['intXintY'] = np.ix_(intY, intX)

    mesh['intYleftX'] = np.ix_(intY, leftX)
    mesh['intYrightX'] = np.ix_(intY, rightX)

    mesh['leftYintX'] = np.ix_(leftY, intX)
    mesh['rightYintX'] = np.ix_(rightY, intX)

    return mesh


# time derivates of boundary condition
# 1st, 2nd, 3rd and 4th derivatives are needed for densities correspoding to demand in both x and y
def time_derivative_bc(t, direction):

    if test_case in [1, 2, 3, 4, 5]:
        if direction == 'x':
            time_der = [0, 0, 0, 0]
        elif direction == 'y':
            time_der = [0, 0, 0, 0]
    else:
        return None

    return time_der


# compute density values in ghost cells
def extrapolate_ghostcells(t, dt, rkstep, domain, density, demand, mesh, direction, layer):

    [[x0, xn], [y0, yn]] = domain
    dent, dentt, denttt, dentttt = time_derivative_bc(t, direction)

    if rkstep == 0:
        denbc = demand / vmax
    elif rkstep == 1:
        denbc = demand / vmax + dt * dent
    elif rkstep == 2:
        denbc = demand / vmax + 0.5 * dt * dent + 0.25 * dt ** 2 * dentt

    nx = mesh['nx']
    ny = mesh['ny']

    faces = mesh['faces']
    cells = mesh['cells']

    domain = mesh['domain'][:, :, layer]

    if direction == 'x':

        xfaces = faces[0]
        xcells = cells[0]

        inflowbound = np.argwhere(domain == 1)

        if inflowbound.size > 0:

            densityfaces = denbc

            for ix, iy in inflowbound:
                if iy == weno_k:
                    xc = x0
                    wenoiter = range(-weno_k, 0)
                elif iy == nx - weno_k:
                    xc = xn
                    wenoiter = range(0, weno_k)
                for j in wenoiter:
                    ghostcell_x = xcells[ix, j + iy]
                    denghost = densityfaces + (ghostcell_x - xc) * (- dent / vmax) + ((ghostcell_x - xc) ** 2 / 2) * (
                                dentt / vmax ** 2) + ((ghostcell_x - xc) ** 3 / 6) * (- denttt / vmax ** 3) + (
                                           (ghostcell_x - xc) ** 4 / 24) * (dentttt / vmax ** 4)
                    density[ix, j + iy] = denghost

            outflowbound = np.argwhere(domain == 3)

            for ix, iy in outflowbound:
                if iy == weno_k:
                    for j in range(weno_k):
                        den = density[ix, :]

                        # 2nd order Lagrangian interpolation
                        denghost = - den[iy - j + 1] + 2 * den[iy - j]
                        density[ix, iy - j - 1] = np.maximum(denghost, 0)
                elif iy == nx - weno_k:
                    for j in range(weno_k):
                        den = density[ix, :]

                        # 2nd order Lagrangian interpolation
                        denghost = - den[iy + j - 2] + 2 * den[iy + j - 1]
                        density[ix, iy + j] = np.maximum(denghost, 0)

    elif direction == 'y':

        yfaces = faces[1]
        ycells = cells[1]

        inflowbound = np.argwhere(domain == 2)

        if inflowbound.size > 0:

            densityfaces = denbc

            for ix, iy in inflowbound:
                if ix == weno_k:
                    yc = y0
                    wenoiter = range(-weno_k, 0)
                elif ix == ny - weno_k:
                    yc = yn
                    wenoiter = range(0, weno_k)
                for j in wenoiter:
                    ghostcell_y = ycells[j + ix, iy]
                    denghost = densityfaces + (ghostcell_y - yc) * (- dent / vmax) + ((ghostcell_y - yc) ** 2 / 2) * (
                                dentt / vmax ** 2) + ((ghostcell_y - yc) ** 3 / 6) * (- denttt / vmax ** 3) + (
                                           (ghostcell_y - yc) ** 4 / 24) * (dentttt / vmax ** 4)
                    density[j + ix, iy] = denghost

            outflowbound = np.argwhere(domain == 4)

            for ix, iy in outflowbound:
                if ix == weno_k:
                    for j in range(weno_k):
                        den = density[:, iy]

                        # 2nd order Lagrangian interpolation
                        denghost = - den[ix - j + 1] + 2 * den[ix - j]
                        density[ix - j - 1, iy] = np.maximum(denghost, 0)
                elif ix == ny - weno_k:
                    for j in range(weno_k):
                        den = density[:, iy]

                        # 2nd order Lagrangian interpolation
                        denghost = - den[ix + j - 2] + 2 * den[ix + j - 1]
                        density[ix + j, iy] = np.maximum(denghost, 0)

    return density


# speed from fundamental diagram
def estimate_speed(rho):

    v_d = vmax * np.ones(rho.shape)
    v_d[np.logical_and(rho <= rho_j, rho > 0)] = vmax * (1 - rho[np.logical_and(rho <= rho_j, rho > 0)] / rho_j)

    return v_d


# compute flux
def compute_flux(rho):

    f = np.zeros(rho.shape)
    f[np.logical_and(rho <= rho_j, rho > 0)] = estimate_speed(rho[np.logical_and(rho <= rho_j, rho > 0)]) \
                                               * rho[np.logical_and(rho <= rho_j, rho > 0)] * largeur_porte

    return f


# compute smoothness indicators for WENO
def smoothness_indicator(den):

    ncells = np.size(den)
    r = np.arange(weno_k - 1, ncells - weno_k + 1)
    beta = np.array([(13 / 12) * (den[r] - 2 * den[r + 1] + den[r + 2]) ** 2 + (1 / 4) * (
            3 * den[r] - 4 * den[r + 1] + den[r + 2]) ** 2,
                     (13 / 12) * (den[r - 1] - 2 * den[r] + den[r + 1]) ** 2 + (1 / 4) * (den[r - 1] - den[r + 1]) ** 2,
                     (13 / 12) * (den[r - 2] - 2 * den[r - 1] + den[r]) ** 2 + (1 / 4) * (
                             3 * den[r] - 4 * den[r - 1] + den[r - 2]) ** 2])

    return beta

# build stencils for WENO
def construct_stencils(nx, ny):

    nxintcells = nx - 2 * (weno_k - 1)
    nyintcells = ny - 2 * (weno_k - 1)

    xstencils = (weno_k - 1) * np.ones((weno_k, nx), dtype=int)
    ystencils = (weno_k - 1) * np.ones((weno_k, ny), dtype=int)

    for m in range(nxintcells):
        l = m + weno_k - 1
        xstencils[:, l] = np.arange(l, l + weno_k)

    for m in range(nyintcells):
        l = m + weno_k - 1
        ystencils[:, l] = np.arange(l, l + weno_k)

    return xstencils, ystencils

# WENO reconstruction
def WENO_scheme(density, stencils):

    ncells = np.size(density)

    beta = smoothness_indicator(density)

    weightL = np.zeros((weno_k, ncells))
    weightR = np.zeros((weno_k, ncells))

    deno = (epsilon + beta) ** 2

    alphaL = drL / deno
    alphaR = drR / deno

    weightL[:, weno_k - 1:ncells - weno_k + 1] = alphaL / np.sum(alphaL, axis=0)
    weightR[:, weno_k - 1:ncells - weno_k + 1] = alphaR / np.sum(alphaR, axis=0)

    denlAll = np.zeros((weno_k, ncells))
    denrAll = np.zeros((weno_k, ncells))

    for r in range(weno_k):
        denlAll[r, :] = np.matmul(coeff[r, :], density[stencils - r])

        denrAll[r, :] = np.matmul(coeff[r + 1, :], density[stencils - r])

    return np.sum(denlAll * weightL, axis=0), np.sum(denrAll * weightR, axis=0)


# Lax-Friedrich scheme
def lax_friedrich_flux(density, mesh, direction, phi_x, phi_y, xstencils, ystencils):

    density_l = np.zeros(density.shape)
    density_r = np.zeros(density.shape)

    phi_l = np.zeros(density.shape)
    phi_r = np.zeros(density.shape)

    obsFX = mesh['obsFX']
    obsFY = mesh['obsFY']

    intYleftX = mesh['intYleftX']
    intYrightX = mesh['intYrightX']

    leftYintX = mesh['leftYintX']
    rightYintX = mesh['rightYintX']

    if direction == 'x':
        for i in range(np.size(density, 0)):
            den = density[i, :]
            denl, denr = WENO_scheme(den, xstencils)

            density_l[i, :] = denl
            density_r[i, :] = denr

            phi = phi_x[i, :]
            phil, phir = WENO_scheme(phi, xstencils)
            phi_l[i, :] = phil
            phi_r[i, :] = phir

        denl = density_r[intYleftX]
        denr = density_l[intYrightX]

        phil = phi_r[intYleftX]
        phir = phi_l[intYrightX]

        phimax = np.max(np.abs(phil), axis=1).reshape(-1, 1)

        fij = (1 / 2) * (compute_flux(denl) * phil + compute_flux(denr) * phir - vmax * phimax * (denr - denl))

        # apply zero flux for obstruction boundaries
        if obsFX.size > 0:
            fij[np.ix_(obsFY[:-1], obsFX)] = 0

    elif direction == 'y':
        for i in range(np.size(density, 1)):
            den = density[:, i]
            denl, denr = WENO_scheme(den, ystencils)
            density_l[:, i] = denl
            density_r[:, i] = denr

            phi = phi_y[:, i]
            phil, phir = WENO_scheme(phi, ystencils)
            phi_l[:, i] = phil
            phi_r[:, i] = phir

        denl = density_r[leftYintX]
        denr = density_l[rightYintX]

        phil = phi_r[leftYintX]
        phir = phi_l[rightYintX]

        phimax = np.max(np.abs(phil), axis=0).reshape(1, -1)

        fij = (1 / 2) * (compute_flux(denl) * phil + compute_flux(denr) * phir - vmax * phimax * (denr - denl))

        # apply zero flux for obstruction boundaries
        if obsFX.size > 0:
            fij[np.ix_(obsFY, obsFX[:-1])] = 0

    return fij

def crowdedness_direction(nlayers, densities, layer):

    beta_0u = 0.8 * beta_0  # avoidance parameter for own class
    beta_0o = 2 * beta_0 - beta_0u  # avoidance parameter for other class (average of beta0u and beta0o is beta0)

    gradpsi = [np.zeros(densities[:, :, 0].shape), np.zeros(densities[:, :, 0].shape)]

    for layer_bis in range(nlayers):

        if layer_bis == layer:
            beta = beta_0u
        else:
            beta = beta_0o

        gradpsil = np.gradient(densities[:, :, layer_bis], edge_order=2)

        for i in range(len(gradpsi)):
            gradpsi[i] += beta * gradpsil[i]

    return gradpsi

# fast marching scheme
def fast_marching_scheme(density, mesh, layer, nlayers, densities):

    nx = mesh['nx']
    ny = mesh['ny']

    domain = mesh['domain'][:, :, layer]
    interior = mesh['interior']

    phi = np.ones(density.shape)
    mask = np.zeros(density.shape, dtype=bool)

    xexits = np.argwhere(domain == 3)
    yexits = np.argwhere(domain == 4)

    mask[interior == -1] = True

    if xexits.size > 0:
        if xexits[0, 1] == weno_k:
            phi[xexits[:, 0], 0] = 0
        elif xexits[0, 1] == nx - weno_k:
            phi[xexits[:, 0], -1] = 0
    if yexits.size > 0:
        if yexits[0, 0] == weno_k:
            phi[0, yexits[:, 1]] = 0
        elif yexits[0, 0] == ny - weno_k:
            phi[-1, yexits[:, 1]] = 0

    phi = np.ma.MaskedArray(phi, mask)

    speed = estimate_speed(density)

    travel_time = skfmm.travel_time(phi, speed, dx=dx, order=2)
    travel_time = np.ma.filled(travel_time, fill_value=1e10)

    gradphi = np.gradient(travel_time, edge_order=2)

    if crwd == 1 and nlayers > 1:
        gradpsi = crowdedness_direction(nlayers, densities, layer)
        for i in range(len(gradpsi)):
            gradphi[i] = alpha_d * gradphi[i] + gradpsi[i]

    normgradphi = np.sqrt((gradphi[0] ** 2 + gradphi[1] ** 2))

    for id in range(len(gradphi)):
        gradphi[id][normgradphi > 0] = gradphi[id][normgradphi > 0] / normgradphi[normgradphi > 0]

    # X, Y = np.meshgrid(range(np.size(gradphi, 2)), range(np.size(gradphi, 1)))
    # plt.quiver(X, Y, -gradphi[1], -gradphi[0])
    # plt.show()

    return -gradphi[1], -gradphi[0]

def compute_direction_vectors(density, mesh, theta, layer, nlayers, densities):

    if fmm == 1:
        phi_x, phi_y = fast_marching_scheme(density, mesh, layer, nlayers, densities)
    else:
        phi_x = np.cos(theta) * np.ones(density.shape)
        phi_y = np.sin(theta) * np.ones(density.shape)

    return phi_x, phi_y

# dimensional splitting
def dimensional_splitting(density, F_i_j, dt, mesh, direction):

    interior = mesh['interior']
    intXintY = mesh['intXintY']

    if direction == 'x':
        density[intXintY] += (dt / dx) * (F_i_j[:, :-1] - F_i_j[:, 1:])
    elif direction == 'y':
        density[intXintY] += (dt / dx) * (F_i_j[:-1, :] - F_i_j[1:, :])

    # density inside obstacles cells imposed as maximum density
    density[interior == -1] = 0  # rho_j

    return density

# time integration loop
def time_integration(domain, mesh, demands, directions, nlayers):

    t = 0
    dt = cfl * dx / vmax

    nx = mesh['nx']
    ny = mesh['ny']

    intX = mesh['intX']
    intY = mesh['intY']

    # Initialisation
    densities = np.zeros((ny, nx, nlayers))
    alldensities = [[t, densities[np.ix_(intY, intX, np.arange(nlayers))]]]

    # construct stencils
    xstencils, ystencils = construct_stencils(nx, ny)

    while t <= Tmax:
        for layer in range(nlayers):
            theta = directions[layer]
            #print('demands', demands, demands [0])
            if t <= Tmax/3:

                demand = demands[layer][0]
                #print('ok1', demand, 'layer', layer)

            elif Tmax/3 < t <= 2*Tmax/3:
                demand = demands[layer][1]
                #print('ok2', demand, 'layer', layer)

            else:
                demand = demands[layer][2]
                #print('ok3', demand, 'layer', layer)

            density = densities[:, :, layer].copy()
            sumdensitiesremlayers = np.sum(densities, axis=2) - density
            for rkstep, (c1, c2) in enumerate(tvdRK):
                # your Eikonal Fast marching scheme here
                sumdensities = sumdensitiesremlayers + density
                phi_x, phi_y = compute_direction_vectors(sumdensities, mesh, theta, layer, nlayers, densities)
                for dimension in ['x', 'y']:
                    density = extrapolate_ghostcells(t, dt, rkstep, domain, density, demand, mesh, dimension, layer)
                    fij = lax_friedrich_flux(density, mesh, dimension, phi_x, phi_y, xstencils, ystencils)
                    density = dimensional_splitting(density, fij, dt, mesh, dimension)
                density = c1 * densities[:, :, layer] + c2 * density
            densities[:, :, layer] = density
        alldensities.append([t, densities[np.ix_(intY, intX, np.arange(nlayers))]])
        t += dt
        print("Time elapsed: ", round(t, 2))

    return alldensities


# plot snapshots of solution
def plot_solution(domain, solution, nlayers):

    [[x0, xn], [y0, yn]] = domain

    nrows = 2
    ncols = int(np.ceil((nlayers + 1) / nrows))

    for istep, (t, densities) in enumerate(solution):

        if istep % 10 == 0:
            fig, ax = plt.subplots(nrows, ncols, figsize=(12, 8))
            ilayer = 0
            for i in range(nrows):
                for j in range(ncols):
                    if ilayer < nlayers:
                        im = ax[i, j].imshow(densities[:, :, ilayer], extent=[x0, xn, y0, yn])
                        ax[i, j].set_xlabel('x')
                        ax[i, j].set_ylabel('y')
                        ax[i, j].set_title("Layer " + str(ilayer + 1))
                        plt.colorbar(im, ax=ax[i, j])
                    elif ilayer == nlayers:
                        im = ax[i, j].imshow(np.sum(densities, axis=2), extent=[x0, xn, y0, yn])
                        ax[i, j].set_xlabel('x')
                        ax[i, j].set_ylabel('y')
                        ax[i, j].set_title("Total Density")
                        plt.colorbar(im, ax=ax[i, j])
                    else:
                        ax[i, j].set_visible(False)
                    ilayer += 1
            fig.suptitle('Time t = ' + str(round(t, 2)), x=0.95, y=0.05)
            plt.show()




def main():
    # # main solver

    inflows, outflows, directions, demand, num_layers = test_cases()

    domain, obstacles = create_geo()

    mesh = generate_mesh(domain, inflows, outflows, obstacles, num_layers)

    solution = time_integration(domain, mesh, demand, directions, num_layers)

    plot_solution(domain, solution, num_layers)


if __name__ == '__main__':
    main()

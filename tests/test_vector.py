# -*- coding: utf-8 -*-
"""
Test for vector at continuum_mechanics package

"""
from __future__ import division, print_function
import sympy as sym
from sympy import symbols, sin, cos, Abs
from sympy import Matrix, simplify
from continuum_mechanics.vector import (scale_coeff, levi_civita, dual_tensor,
                                        dual_vector, grad, grad_vec, div,
                                        curl, lap, lap_vec)

x, y, z = sym.symbols("x y z")

def test_scale_coeff():
    r, theta, phi = sym.symbols("r theta phi", positive=True)
    r_vec = [r*sin(theta)*cos(phi), r*sin(theta)*sin(phi), r*cos(theta)]
    coords = [r, theta, phi]
    h_vec = scale_coeff(r_vec, coords)
    assert h_vec == (1, r, r*Abs(sin(theta)))

#%%
def test_levi_civita():
    assert levi_civita(1, 2, 3) == 1
    assert levi_civita(1, 3, 2) == -1
    assert levi_civita(1, 1, 2) == 0


def test_dual_tensor():
    vector = Matrix([1, 2, 3])
    tensor = Matrix([
            [ 0,  3, -2],
            [-3,  0,  1],
            [ 2, -1,  0]])
    assert dual_tensor(vector) == tensor
    assert dual_vector(tensor) == vector


def test_dual_vector():
    tensor = Matrix([
            [ 0,  3, -2],
            [-3,  0,  1],
            [ 2, -1,  0]])
    vector = Matrix([1, 2, 3])
    assert dual_vector(tensor) == vector
    assert dual_tensor(vector) == tensor


#%%
def test_grad():
    gradient = grad(-(cos(x)**2 + cos(y)**2)**2)
    expected_gradient = Matrix([
            [4*(cos(x)**2 + cos(y)**2)*sin(x)*cos(x)],
            [4*(cos(x)**2 + cos(y)**2)*sin(y)*cos(y)],
            [0]])
    assert gradient.equals(expected_gradient)


def test_grad_vec():
    gradient = grad_vec([x*y*z, x*y*z, x*y*z])
    expected_gradient = Matrix([
            [y*z, x*z, x*y],
            [y*z, x*z, x*y],
            [y*z, x*z, x*y]])
    assert gradient == expected_gradient


def test_div():
    divergence = div([x**2 + y*z, y**2+x*z, z**2 + x*y])
    expected_divergence = 2*x + 2*y + 2*z
    assert divergence == expected_divergence


def test_curl():
    rot = curl([0, -x**2, 0])
    expected_rot = Matrix([[0], [0], [-2*x]])
    assert rot == expected_rot


def test_lap():
    laplacian = lap(x**2 +  y**2 + z**2)
    expected_laplacian = 6
    assert laplacian == expected_laplacian


def test_lap_vec():
    laplacian = lap_vec([x**2, y**2, z**2])
    expected_laplacian = Matrix([[2], [2], [2]])
    assert laplacian == expected_laplacian

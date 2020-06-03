# DiamondSquareTest.py
# Written by Hailey K Buckingham
# On github, buckinha/DiamondSquare

import unittest
import numpy as np
from hkb_diamondsquare import DiamondSquare


class TestDiamondSquare(unittest.TestCase):

    def setUp(self) -> None:
        self.shape = (11, 31)
        self.roughness = 0.05
        self.seed = 1
        self.min_height = 20
        self.max_height = 35
        self.default_landscape = DiamondSquare.diamond_square(
            shape=self.shape,
            min_height=self.min_height,
            max_height=self.max_height,
            roughness=self.roughness,
            random_seed=self.seed,
            as_ndarray=True)

    def test_final_shape(self):
        self.assertEqual(self.default_landscape.shape, self.shape)

    def test_min_and_max_heights(self):
        self.assertTrue(np.max(self.default_landscape) <= self.max_height)
        self.assertTrue(np.min(self.default_landscape) >= self.min_height)

    def test_seed_values_produce_identical_maps(self):

        seed = 123
        shape = (250, 250)
        t1 = DiamondSquare.diamond_square(
            shape=shape,
            min_height=self.min_height,
            max_height=self.max_height,
            roughness=self.roughness,
            random_seed=seed,
            as_ndarray=True)

        t2 = DiamondSquare.diamond_square(
            shape=shape,
            min_height=self.min_height,
            max_height=self.max_height,
            roughness=self.roughness,
            random_seed=seed,
            as_ndarray=True)

        self.assertTrue(np.allclose(t1, t2))

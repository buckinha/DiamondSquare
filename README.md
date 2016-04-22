This is a python implementation of the classic diamond-square algorithm for 2-D height maps,
which are often used for terrain generation and random map creation. 


Feel free to post questions or requests, and I'll see what I can do.

If you use it for something interesting, I'd love to hear about it. 

Best,
-HKB-



Using it in a python project is easy:
------------------------------------------------------
```python
import DiamondSquare as DS

#make a height map of size 16x20, with values ranging from 1 to 100, with moderate roughness
map1 = DS.diamond_square((16,20),1,100,0.75)

#make a square height map with sides of length 120, that are VERY rough
map2 = DS.diamond_square(120,1,100,0.99)

#make a VERY smooth map with values from -10 to 10
map3 = DS.diamond_square((10,10), -10, 10, 0.05)

#return a large, moderately rough map as a numpy array
import numpy as np
ndarray_map = DS.diamond_square((800,600), 1, 100, 0.8, AS_NP_ARRAY=True)

#use a specific random seed to ensure absolute replicability
same_map_1 = DS.diamond_square((15,15), 1, 100, 0.8, random_seed=1.234, AS_NP_ARRAY=True)
same_map_2 = DS.diamond_square((15,15), 1, 100, 0.8, random_seed=1.234, AS_NP_ARRAY=True)
np.array_equal(same_map_1, same_map_2)
different_map = DS.diamond_square((15,15), 1, 100, 0.8, random_seed=1.2341, AS_NP_ARRAY=True)
np.array_equal(same_map_1, different_map)
```
------------------------------------------------------

FUNCTION SIGNATURE
diamond_square(size, min_height, max_height, roughness, random_seed=None, AS_NP_ARRAY=False)

PARAMETERS
----------

size
    The size of the grid to be returned. If an integer is passed, the return grid will
    have sides of this length. If an array-like is passed, the first two values will be 
    used as the array shape.

min_height
    The minimum height allowed on the landscape

max_height
    The maximum height allowed on the landscape

roughness
    A float with value between 0 and 1, reflecting how bumpy the landscape should be. 
    Values near 1 will result in landscapes that are extremly rough, and have almost no
    cell-to-cell smoothness. Values near zero will result in landscapes that are almost
    perfectly smooth.

random_seed
    defaults to None. If a value is given, the algorithm will use it to seed the random
    number generator, ensuring replicability.

AS_NP_ARRAY
    A boolean reflecting whether the landscape should be returned as a numpy array. If set
    to False, the method will return a 2-dimensional list.


RETURNS
-------
A 2-D list or 2-D numpy array with a diamond-square "height-map"





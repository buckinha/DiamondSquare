#DiamondSquare.py
This is a python implementation of the classic diamond-square algorithm for 2-D height maps,
which are often used for terrain generation and random map creation. 


Feel free to post questions or requests, and I'll see what I can do.

If you use it for something interesting, I'd love to hear about it. 

Best,
-HKB-



### Using it in a python project is easy:
------------------------------------------------------
```python

from hkb_diamondsquare import DiamondSquare as DS

#make a height map of size 16x20, with values ranging from 1 to 100, with moderate roughness
map1 = DS.diamond_square(shape=(16,20), 
                         min_height=1, 
                         max_height=100,
                         roughness=0.75)

#make a square height map with sides of length 120, that are VERY rough
map2 = DS.diamond_square(shape=(120,120),
                         min_height=1,
                         max_height=100,
                         roughness=0.99)

#make a VERY smooth map with values from -10 to 10
map3 = DS.diamond_square(shape=(10,10), 
                         min_height=-10, 
                         max_height=10, 
                         roughness=0.05)

#use a specific random seed to ensure replicability
same_map_1 = DS.diamond_square((15,15), 1, 100, 0.8, random_seed=1.234)
same_map_2 = DS.diamond_square((15,15), 1, 100, 0.8, random_seed=1.234)
import numpy as np
np.allclose(same_map_1, same_map_2)
# prints True

different_map = DS.diamond_square((15,15), 1, 100, 0.8, random_seed=1.2341, as_ndarray=True)
np.allclose(same_map_1, different_map)
# prints False
```

You can also vizualize your landscape using Seaborn (not included by default) as shown:
```python
from hkb_diamondsquare import DiamondSquare
import seaborn

def show_terrain_2D(terrain_array):

    seaborn.set()
    ax = seaborn.heatmap(terrain_array)

map = DiamondSquare.diamond_square(shape=(50,50), min_height=0, max_height=10, roughness=0.3)
show_terrain_2D(map)
```





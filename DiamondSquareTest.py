#DiamondSquareTest.py
#Written by Hailey K Buckingham
#On github, buckinha/DiamondSquare
#

import DiamondSquare

def test_that_seed_values_produce_identical_maps():

    print("Testing that identical seeds produce identical maps, ceteris parabis")
    print("")
    t1 = DiamondSquare.diamond_square(desired_size=257, min_height=0, max_height=1, roughness=0.05, random_seed=0, AS_NP_ARRAY=False, USE_NEW_SQUARE_STEP=False)
    t2 = DiamondSquare.diamond_square(desired_size=257, min_height=0, max_height=1, roughness=0.05, random_seed=0, AS_NP_ARRAY=False, USE_NEW_SQUARE_STEP=False)
    if not test_that_terrain_maps_are_the_same(t1, t2):
        print("Fail: Testing_square_step_improvement() with older square step")
        print("map1:")
        print_map_subsection(t1, 0,5,0,5)
        print("map2:")
        print_map_subsection(t2, 0,5,0,5)

    print("")
    t1 = DiamondSquare.diamond_square(desired_size=257, min_height=0, max_height=1, roughness=0.05, random_seed=0, AS_NP_ARRAY=False, USE_NEW_SQUARE_STEP=True)
    t2 = DiamondSquare.diamond_square(desired_size=257, min_height=0, max_height=1, roughness=0.05, random_seed=0, AS_NP_ARRAY=False, USE_NEW_SQUARE_STEP=True)
    if not test_that_terrain_maps_are_the_same(t1, t2):
        print("Fail: Testing_square_step_improvement() with newer square step")
        print("map1:")
        print_map_subsection(t1, 0,5,0,5)
        print("map2:")
        print_map_subsection(t2, 0,5,0,5)

def test_that_terrain_maps_are_the_same(t1, t2):

    if not ( len(t1) == len(t2) ):
        return False

    if not ( len(t1[0]) ==  len(t2[0]) ):
        return False

    for i in range(len(t1)):
        for j in range(len(t1[0])):
            if not t1[i][j] == t2[i][j]:
                return False

    return True

def print_map_subsection(map, x1,x2,y1,y2):
    for j in range(y1,y2):
        for i in range(x1,x2):
            print(round(map[i][j], 2)),
        print("")

def main():
    test_that_seed_values_produce_identical_maps()
    print("All tests complete")


if __name__ == '__main__':
    main()
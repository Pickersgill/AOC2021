import sys
import re
import numpy as np
import decode

from matplotlib import pyplot as plt

'''

Looks like a clustering problem.

1.) Find congruent/similar set of points in two different
    scanners. Call this a constellation.

2.) Validate the constellation (distances aren't coincidence)

3.) Transform dimensions of second scanner so axis are the same.

4.) Triangulate position of second scanner.

5.) Offset and rotate all points in second scanner.

6.) Merge transformed scanner 2 and 1 together... repeat...

'''


def find_matches(ds1, ds2):

    matches = []
    
    for i, d1 in enumerate(ds1):
        for j, d2 in enumerate(ds2):
            if d1 == d2 and d1 != 0 and d2 != 0:
                matches.append([i, j])

    return matches
        

# find some point in s1 and s2 and _assume_ they are the same beacon.
# Find the distance from this assumed beacon (AB) to all other points
# in both scanner. Find the pair of indexes which create the largest
# set of points which are exactly the same distance from AB.

def get_constellation(s1, s2):

    b1 = s1.beacons
    b2 = s2.beacons

    for i in range(len(b1)):
        point1 = b1[i]
        dists_1 = s1.get_dists(i)
        for j in range(len(b2)):
            point2 = b2[j]
            dists_2 = s2.get_dists(j)
    
            m = find_matches(dists_1, dists_2)
            if len(m) > 1:
                return m + [[i, j]]
     

if __name__ == "__main__":
    ss = decode.build_input(sys.argv[1])

    first = ss[0]
    second = ss[24]

    theta = np.radians(90)
    c, s = np.cos(theta), np.sin(theta)
    Rx = np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
    Ry = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    Rz = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])

    m = np.array(get_constellation(first, second))
    
    points1 = first.beacons[m[..., 0]]
    points1 = points1 - np.mean(points1, axis=0)
    points2 = second.beacons[m[..., 1]]
    points2 = points2 - np.mean(points2, axis=0)
    #points2 = points2.dot(Ry).dot(Rx).dot(Rx).dot(Rx)

    ax = plt.axes(projection='3d')

    ax.scatter3D(points1[..., 0], points1[..., 1], points1[..., 2], \
        color="red", alpha=0.5, label="points 1")
    ax.scatter3D(points2[..., 0], points2[..., 1], points2[..., 2], \
        color="blue", alpha=0.5, label="points 2")

    plt.legend()
    plt.show()
    #for s in ss[1:]:
     #   print(str(s))
      #  get_constellation(ss[0], s)



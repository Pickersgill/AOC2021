import re
import numpy as np

class Scanner:
    def __init__(self, beacons=None, name="Just another scanner..."):
        self.beacons = beacons
        self.name = name

    def copy(self):
        return Scanner(self.beacons)    
    
    def add_beacon_from_text(self, txt):
        txt = re.sub("\n", "", txt)
        new_b = np.array([int(x) for x in txt.split(",")])
        self.add_beacon(new_b)
    
    def add_beacon(self, new_b):
        if self.beacons is not None:
            self.beacons = np.append(self.beacons, [new_b], axis=0)
        else:
            self.beacons = np.array([new_b])
    
    def get_dists(self, ind):
        all_d = self.beacons
        d1 = all_d[ind]
        dists = np.linalg.norm(all_d - d1, axis=1)
        return dists

    def __str__(self):
        return "%s seeing %d beacons..." % \
            (self.name, len(self.beacons))

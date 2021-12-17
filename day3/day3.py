import numpy as np
import re

src = open("./input")

rows = [np.array([int(x) for x in re.sub("\n", "", r)]) for r in src]

binary = np.array(rows)
bin_t = np.transpose(binary)

means = np.round(np.mean(bin_t, 1))
gamma = "".join([str(int(x)) for x in means])
eps = "".join(['0' if bit == '1' else '1' for bit in gamma])

print(gamma)
print(int(gamma, 2))

print(eps)
print(int(eps, 2))

print("Part 1:")
print(int(gamma, 2) * int(eps, 2))


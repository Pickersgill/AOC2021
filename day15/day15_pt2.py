import re
import sys
import numpy as np

# step 1
sys.setrecursionlimit(2500)
TEST_SIZE = 10

risk_mat = None
if len(sys.argv) > 1:
    src = sys.argv[1]
else:
    src = None

if src:
    inp = open(src, newline="")
    inp_arr = []

    for i in inp:
        arr = [int(x) for x in re.sub("\n", "", i)]
        inp_arr.append(arr)

    base_risk_mat = np.array(inp_arr)
else:
    base_risk_mat = np.random.randint(1, 10, (TEST_SIZE, TEST_SIZE))
    
# Build the whole matrix with "spillage"
risk_mat = np.concatenate([(base_risk_mat + i) for i in range(5)], 1)
risk_mat = np.concatenate([(risk_mat + i) for i in range(5)], 0)

# Implement the wrap around accounting for extra +1 on wrap
risk_mat = (risk_mat + risk_mat // 10) % 10

print(risk_mat)
print(risk_mat.shape)
# step 2
# methods defining adjacent nodes

def up(pos):
    u = (pos[0], pos[1]-1) if pos[1] > 0 else None
    return u
    
def right(pos):
    r = (pos[0] + 1, pos[1]) if pos[0] < DIM - 1 else None
    return r

def down(pos):
    d = (pos[0], pos[1]+1) if pos[1] < DIM - 1 else None
    return d

def get_risk(pos):
    if pos is None:
        return None
    return risk_mat[pos[1]][pos[0]]
    
DIM = len(risk_mat)
MAX = (DIM ** 2) * 9
# This definition for the minimum is starting off way to large, lets bound it a bit tighter with a trivial initial
# solution

MIN = 0
min_matrix = np.zeros(risk_mat.shape)
initial_pos = (0, 0)
initial_risk = 0

path = None

def search(risk, pos, visited):
    global path, min_matrix, MIN
    # make sure we're using the right min, max
    x = pos[0]
    y = pos[1]
    
    if min_matrix[y][x] == 0 or min_matrix[y][x] > risk:
        min_matrix[y][x] = risk
        if y == DIM - 1 and x == DIM - 1:
            path = visited + [pos]
            MIN = risk
    else:
        return
    
    # recursive cases
    u = up(pos)
    r = right(pos)
    d = down(pos)
    for new in [u, r, d]:
        if new is not None and new not in visited:
            search(risk + get_risk(new), new, visited + [pos])
            
search(initial_risk, initial_pos, [])
print(min_matrix[DIM-1][DIM-1])
print("Via following path: ")
p_mat = np.array([[("x" if (i, j) in path else " ") for i in range(DIM)] for j in range(DIM)])
print(p_mat)



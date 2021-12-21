import decode
import sys

key, grid = decode.decode(sys.argv[1])

print(grid.number_of_on())
grid = grid.get_transformation(key)
grid = grid.get_transformation(key)
print(grid.number_of_on())


# TODO
# Bug caused by poor handling of 0s in field.




src = open("./input")

depth = 0
hoz = 0
rows = [r for r in src]

for row in rows:
    terms = row.split()
    instr = terms[0]
    val = int(terms[1])
    if instr == "forward":
        hoz += int(val)
    elif instr == "down":
        depth += int(val)
    elif instr == "up":
        depth -= int(val)

print("Part 1:")
print(hoz * depth)

aim = 0
hoz = 0
dep = 0

for row in rows:
    terms = row.split()
    instr = terms[0]
    val = int(terms[1])
    if instr == "forward":
        hoz += val
        dep += aim * val
    elif instr == "down":
        aim += val
    elif instr == "up":
        aim -= val

print("Part 2:")
print(hoz * dep)

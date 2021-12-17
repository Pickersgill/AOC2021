import numpy as np

def get_incs(series):
    prev = None
    inc = 0

    for row in series:
        if prev is not None and row > prev:
            inc+=1
        prev = row

    return inc

with open("./day1_input") as data:
    data = [int(x) for x in data]
    inc = get_incs(data)
    print("Part 1: ")
    print(inc)
    
    windows = []
    for i in range(len(data) - 2):
        windows.append(sum(data[i:i+3]))
        
    print(windows[0])
    print(len(windows))
    inc2 = get_incs(windows)
    print("Part 2: ")
    print(inc2)

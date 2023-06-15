

# print(list(range(0, -10, -1)))
def range_re(end:int, start:int = 0, step:int = 1): 
    if start > end and step > 0:
        raise ValueError("Invalid start end")
    
    if start < end and step < 0:
        raise ValueError("Invalid start end")
    
    if not type(end) == type(step) == type(start) == int:
            raise TypeError("TypeError")
    
    e = abs(end)

    s = start

    while e:
        if end > start:
            e -= abs(step)
            yield s

            s -= step

        if end < start:
            e -= abs(step)
            yield s

            s += step

for i in range_re(2, 10, 3):
     print(i)
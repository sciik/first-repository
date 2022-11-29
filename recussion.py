arr = []
array = [1, [2, 3, 4],
         [3, [2, 3]]]


def recur(*args):
    for i in args:    
        if type(i) is list:
            recur(*i)
        else:
            arr.append(i)


recur(*array)
print(arr)

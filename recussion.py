def recur(arr, ans):
    for i in arr:    
        if type(i) is list:
            recur(i, ans)
        else:
            ans.append(i)

array = []
arr = [1, [2, 3, 4],
         [3, [2, 3]]]

recur(arr, array)
print(array)

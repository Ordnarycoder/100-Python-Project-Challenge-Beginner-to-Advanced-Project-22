def binary_search(arr, low, high, x):

    if high >= low:
        mid = (low + high) // 2

        if arr[mid] == x:
            print(f"Index of x: {mid}")

        elif arr[mid] > x:
            return binary_search(x, low, mid-1,x)
        
        else:
            return binary_search(arr, mid + 1, high, x)
        
    
    else:
        print("Element isn't in array")


arr = [ 2, 3, 4, 10, 40 ]
x = 9
 
result = binary_search(arr, 0, len(arr)-1, x)
    
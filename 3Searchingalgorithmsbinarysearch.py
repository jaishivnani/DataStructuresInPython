pos = -1

def binarysearch(list,n):
    low = 0
    high = len(list)- 1

    while low <= high:
        mid = (low+high)//2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                low = mid+1
            else:
                high = mid-1
    return False

list = [4,7,8,12,45,99,102,702,10987,56666]
n = 45

if binarysearch(list,n):
    print('Found at ',pos+1)
else:
    print('Not Found')




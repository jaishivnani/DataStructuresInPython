pos = -1

def binarysearch(list,n,low,high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                return binarysearch(list,n,mid+1,high)
            else:
                return binarysearch(list,n,low,mid-1)
    return False

list = [4,7,8,12,45,99]
n = int(input('Enter a number:-'))

found = binarysearch(list,n,0,5)

if binarysearch(list,n,0,5):
    print('Found at ',pos+1)
else:
    print('Not Found')




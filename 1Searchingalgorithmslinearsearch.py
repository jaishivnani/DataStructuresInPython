# In python set of elements are represented using lists.
# The approach of Linear search algorithm is to visit each element and match the key(Index i) with the element.
# If Found return True and Position(pos) else Not Found.

# ---------------------------Using While Loop----------------------------------------#
# pos = -1                       # To find position pos is global
#
# def linearsearch(list,n):      # Creating method which will take list and no which need to search as input.
#     i = 0
#     while i<len(list):           # To traverse the list.
#         if list[i]==n:           # To check if index value i is equal to value we are searching.
#             globals()['pos']= i  # Defining global variable pos locally and assigning the value of i to it.
#             return True
#         i = i + 1
#     return False

# ---------------------------Using For Loop----------------------------------------#
pos = -1
def linearsearch(list,n):      # Creating method which will take list and no which need to search as input.

   for i in range (len(list)):           # To traverse the list.
        if list[i]==n:           # To check if index value i is equal to value we are searching.
            globals()['pos']= i  # Defining global variable pos locally and assigning the value of i to it.
            return True

list = [5,8,4,6,9,2]

n = int(input("Enter the number which you need to search:- "))  # Taking user input for value which needs to be searched.

found = linearsearch(list,n)  # Calling method or function and storing the value returned in found variable.

if linearsearch(list,n):
    print(found,'Found at',pos+1)
else:
    print('Not Found')


###############################################################################
# Given an unsorted list of values (you do not know the datatype).
# Only two values appear in the list but they appear many times and
# are not sorted. Without using any significant additional space
# (i.e. you cannot copy the list) sort the elements in linear time
# going through the list only once.
# 
# For example:
# Given the list [‘a’, ‘a’, ‘b’, ‘a’, ‘a’, ‘b’, ‘b’, ‘a’] after the
# function, the list is [‘a’, ‘a’, ‘a’, ‘a’, ‘a’, ‘b’, ‘b’, ‘b’] Given
# the list [1, 0, 1, 0, 1, 1] after the function, the list is [0,0,1,1,1,1]
###############################################################################


def sorter(L):

    v1 = L[0]
    len_L = len(L)
    count = 0
    track = 0

    for i in range(len_L):
        if L[track] == v1:
            L.insert(-1, L.pop(track))
            print(L)
        else:
            L.insert(0, L.pop(track))
            track += 1
            print(L)

    return(L)


before = ['a', 'a', 'b', 'a', 'a', 'b', 'b', 'a']
print(before)

after = sorter(L)
print(after)

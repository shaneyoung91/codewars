# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]



# My Solution
def move_zeros(lst):
    # iterate through the list
    # if elem == '0', remove and append to the end
    # return list
    
    for elem in lst:
        if elem == 0:
            lst.remove(elem)
            lst.append(elem)
    
    return lst
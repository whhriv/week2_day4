# Looks like some hoodlum plumber and his brother has been running around and damaging your stages again.

# The pipes connecting your level's stages together need to be fixed before you receive any more complaints.

# Pipes list is correct when each pipe after the first index is greater (+1) than the previous one, and that there is no duplicates.

# Task
# Given the a list of numbers, return a fixed list so that the values increment by 1 for each index from the minimum value up to the maximum value (both included).

# Example
# Input:  1,3,5,6,7,8 Output: 1,2,3,4,5,6,7,8


#param will be a list of POS numbers or 0
#output list of ordered number from smallest to largest
#first and last always smallest and largest - ordered
#first array len not always the same as last array
#get the array
#get first and last value
#create new array
#smart from smallest and increment until we reach largest/last by 1
#append value to array

def solution(array):
    result = []
    smallest = min(array)
    # result.append(smallest)
    largest = max(array)
    for i in range(smallest, largest+1):
        result.append(smallest)
        smallest+=1
    return result



def solution(pipes):
    return [num for num in range(pipes[0], pipes[-1] +1)]

# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

# Method 1 in while loop
def find_element(p,t):
    i = 0
    while i < len(p):
	    if p[i] == t:
		    return i
		i = i + 1
	return -1
	

# Method 2 in for loop
def find_element(p,t):
    i = 0
	for e in p:
	    if e == t:
		    return t
		return -1
		

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1
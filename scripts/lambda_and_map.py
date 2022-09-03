nums = [1, 2,3,4,5,6,7]

# Test map without assigning the result to a list
sum_1 = map(lambda x: x + 1, nums)

print(sum_1)

# It only prints a python object, but 
# no results. 

# Now let's add the list
sum_1 = list(map(lambda x: x + 1, nums))

print(sum_1)

# Now it worked. The values appeared. 

# Lets try with a tuple
sum_1 = tuple(map(lambda x: x + 1, nums))

print(sum_1)

# Works too!

# And dictionary
sum_1 = dict(map(lambda x: x + 1, nums))

print(sum_1)

# dict do not work bc we dont have keys

sum_dict = dict(map(lambda x: [str(x): x+1]))

print(sum_dict)

# This also do not work. 




set1 = {1, 2, 3, 4} #set when returned sorts itself in ascending order
set2 = {3, 4, "Python", "JS" }
set3 = {"Python", "JS", "Java", "C++"}

print(set1 | set2 | set3) #returns only the definite value no duplication is allowed
print(set1.union(set2).union(set3)) #.union() function is the same as above no duplicate vlalues allowed

print(set1 & set2) # returns only the commanly shared values
print(set1.intersection(set2)) #this function works the same as above returns common value

print(set1 & set2 & set3) # returns empty dictionary since they dont share a common value
print(set1.intersection(set2).intersection(set3)) # same as above value is empty dictionary. since they dont share the same value

print(set1 - set2) #removes the common values and return the remaining values
# in difference note that the values in the 1st set is returned
print(set3.difference(set2).difference(set1)) #returns the remaning value of the 1st given set

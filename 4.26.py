from collections import namedtuple
City = namedtuple("city","loc")
to = City(201)
print(to.loc)
ls = [[2]]
l1 = ls * 5
print(l1)
l1[2][0] = 1
print(l1)
l = [2]
print(id(l))
print(hash([1,2]))
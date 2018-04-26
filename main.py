#every element in a set must be unique (as defined by wikipedia)
def intersect (a, b) :
    if (len(a) > len(b)):
        return intersect(b, a)
    else:
        #a < b
        return [i for i in a if i in b]



        
l1 = [12,5,7,9,23,785]
l2 = [785,4,36,2,5,9,21]

print intersect(l1,l2)
print intersect(l2,l1)


def union (a, b):
    return a + [i for i in b if i not in a]

print union(l1, l2)

def set_difference(a, b):
    return [i for i in a if i not in b]


print set_difference(l1, l2)

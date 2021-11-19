car_parts = {"wheels", "doors", "exhaust"}
print(car_parts, type(car_parts))

car_parts.add("seats")
print(car_parts)

car_parts.discard("doors")
print(car_parts)


# sets can only contain unique items
l = [3,2,5,3,2,4,5,6,7,8,5,4,3,2,2,3,3,3,3]
print(l)
print(set(l))



# Frozen set - immutable version of a set
f = frozenset((1,2,3,4,5))
print(f)


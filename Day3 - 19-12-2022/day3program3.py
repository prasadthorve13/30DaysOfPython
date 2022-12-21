# Comparison operator
x = 5
y = 3
print(x==y)
print(x!=y)
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)
print('-------------------------------------------------------')
print(len('mango') == len('avacado'))
print(len('mango') != len('avacado'))
print(len('mango') < len('avacado'))
print(len('mango') > len('avacado'))
print('-------------------------------------------------------')

# is, is not, in, not in
# is checks for identity whereas == checks for equality
print('1 is 1', 1 is 1)
print('1 is not 2', 1 is not 2)
print('A in ABC', 'A' in 'ABC')
print('D not in ABC', 'D' not in 'ABC')
print('-------------------------------------------------------')

# and, or, not
print(3>2 and 4>5)
print(3<2 and 4<5)
print(3>2 and 4<5)
print(3<2 and 4>5)

print(3>2 or 4>5)
print(3<2 or 4<5)
print(3>2 or 4<5)
print(3<2 or 4>5)

print(not True)
print(not not True)
print(not False)
print(not not False)
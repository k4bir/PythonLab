N=int(input('enter the number of student:'))
K=int(input('enter the number of apples:'))

remaining=K%N
distrubuted=K//N

print(f'Each students will get {distrubuted} apples')
print(f'The apples remaining in the basket are {remaining}')
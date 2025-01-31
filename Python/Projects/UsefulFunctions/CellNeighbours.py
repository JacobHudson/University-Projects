from itertools import product   

gridSize = 6

def neighbours(cell):
    for c in product(*(range(n-1, n+2) for n in cell)):
        if c != cell and all(0 <= n < gridSize for n in c):
            yield c

print(list(neighbours((3,4))))


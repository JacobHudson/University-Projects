def fibonacci_loop(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci_loop(10)
print("Hello World!")

#0,1,1,2,3,5,8,13,21,34
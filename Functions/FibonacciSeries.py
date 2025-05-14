#1.
def fib(n):
    while n > 0:

        a = 0
        b = 1

        if n == 1:
            print(a)
        else:


            for i in range(2, n):

                c = a + b
                a = b
                b = c
                print(c if c < n else exit())
            break
    else:
        print("Number must be greater than 0")

fib(100)


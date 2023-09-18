def fib (elem3):
    if elem3 == 1:
        return 0
    elif elem3 == 2:
        return [0,2]
    else:
        fib = [0,1]
        for i in range(2,elem3):
            n_elem = fib [-1] + fib [-2]
            fib.append(n_elem)
        return fib
    
print(fib(int(input('Digite um Número: '))))
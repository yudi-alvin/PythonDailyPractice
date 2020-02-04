def fib(n,mem={}):
    if n in mem:
        return mem[n]
    if n ==0 or n ==1:
        mem[n]= n
    else:
        mem[n]= fib(n-1) + fib(n-2)
    return mem[n]

print(fib(140))

#java way
def fib(n,iode=[-1]*141):

    if n == 0 or n == 1:
        return n
    if iode[n] == -1:
        iode[n] = fib(n-1,iode)+ fib(n-2,iode)

    return iode[n]

print(fib(140))


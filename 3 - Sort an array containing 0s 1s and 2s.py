#take an array and pass it for processing
def main():
    arr = [0,1,2,2,1,0,0,2,0,1,1,0]
    print(proc(arr))

#process the array
def proc(a):
    #count 0s and 1s, index at 0
    z = a.count(0)
    o = a.count(1)
    i = 0

    #while we have elements
    while i < len(a):
        #set their value according to how many of each we should have
        a[i] = 0 if (i < z) else 1 if (i<(z+o)) else 2
        i += 1
    #return the new array
    return a

main()

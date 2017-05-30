#create an array and pass for processing
def main():
    arr = [1,0,1,0,1,0,0,1]
    print(proc(arr))

#process the array
def proc(a):
    #number of zeros
    zero = a.count(0)

    #0 to number of zeros - 1, make them all 0
    for x in range(zero):
        a[x] = 0
    #make the rest 1
    for x in range(zero+1, len(a)-1):
        a[x] = 1
    #return the processed array
    return a

main()

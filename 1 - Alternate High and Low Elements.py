#take a list of numbers and pass them for processing
def main():
    nums = [int(x) for x in input("Enter a list of integers: ").split(',')]
    print(proc(nums))

#process the list
def proc(n):
    #essentially a do...while
    while True:
        #flag for swaps, and a counter
        flag = 0
        count = 1
        #while we've got elements to compare...
        while count < (len(n)-1):
            #look behind and ahead, swap if the current index is the lesser and flag it
            if n[count] < n[count-1]:
                n[count],n[count-1] = n[count-1], n[count]
                flag += 1
            elif n[count] < n[count+1]:
                n[count],n[count+1] = n[count+1], n[count]
                flag += 1
            #increment our index
            count += 2
        #stop if we never swapped
        if flag == 0:
            break
    #pass the new list back
    return n

main()

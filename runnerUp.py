#Each of these finds the second largest number in a list of size n
# In HackerRank, it was called the "Runner-Up"

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    m1 = max(arr)                            # This model uses the "max()"
    m2 = -9999999999                         # function to find the largest
    for i in range(n):
        if arr[i] != m1 and arr[i] > m2:     # Where it then loops the entire list
            m2 = arr[i]                      # to find the "next largest"
    print (m2)


from collections import Counter
if __name__ == '__main__':
    n = int(input())                                   # This model uses collections.Counter
    arr = Counter(map(int, input().split())).keys()    # to first find the Counter.keys()
    arr.sort()                                         # Then sort into a simple (#, #, ... , second, largest)
    print (arr[-2])                                    # allowing arr[-2] to find our second largest no problem.


if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))         # This model follows the same
    arr.sort()                                         # thought as the previous
    print (arr[-2])                                    # But it uses list() instead of Counter.keys()

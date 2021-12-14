#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        j = i+1
        smallest = arr[i]
        k = i
        
        while j < n:
            if smallest > arr[j]:
                smallest = arr[j]
                k = j
            j += 1
        return k
    
    def selectionSort(self, arr, n):
        #code here
        for i in range(0, n-1):
            k = self.select(arr, i)
            if i != k:
                arr[i], arr[k] = arr[k], arr[i]
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends

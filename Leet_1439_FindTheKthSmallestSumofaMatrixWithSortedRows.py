"""
: 1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows
: You are given an m * n matrix, mat, and an integer k, which has its rows sorted in non-decreasing order.
: You are allowed to choose exactly 1 element from each row to form an array. Return the Kth smallest array sum among all possible arrays.

: Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 7
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.

: Input: mat = [[1,3,11],[2,4,6]], k = 9
Output: 17

: Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
Output: 9
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.

: Input: mat = [[1,1,10],[2,2,9]], k = 7
Output: 12
"""
"""
: Solution:
: => Consider two Sorted (ascending) Arrays, find the min sum from both array with K=1:
:    A0=[a00, a01, ... a0n-1]
:    A1=[a10, a11, ... a1n-1]
: -> k=1 -> min is a00+a10  (candidate is from A0[a01], A1[a02] combination

: => when K=2 
: -> candidate is from A0=[a01, a02], A1=[a10, a11]

: => when K=k
: -> candidate is from A0=[a01, a02, ... , a0k], A1=[a10, a11, ..., a1k]
: -> you don't have to worry about anything after k 

: => Consider m Sorted (ascending) Arrays
: -> Candidates for the combinaitno is:
:    A0 = [a00, a01, ..., a0k-1]
:    A1 = [a10, a11, ..., a1k-1]
:    ...
:    Am-1 = [am-10, am-11, ..., am-1k-1]

: => Pseudo code:
:    1. find the smallest top-k sum from row0, row1 into a min_heap
:       put all combination btn A0[:] and A1[0] into heap
"""

import heapq


class Solution:
    def kthSmallest(self, mat, k: int) -> int:

        def findKSmallestSumFromTwoArr(arr1, arr2, k):
            min_heap = []
            result = []
            for ii in range(min(len(arr1), k)): #find all combination btn the two array
                for jj in range(min(len(arr2), k)):
                    heapq.heappush(min_heap, arr1[ii] + arr2[jj])
                    # print(" ii: ", ii, " jj: ", jj, " min_heap: ", min_heap)

            #print(" heap size: ", len(min_heap))
            for _ in range(k):
                if min_heap:
                    result.append(heapq.heappop(min_heap))

            return result

        if len(mat) >= 2: # find the kth smallest in a new array and use it to iterate with the rest of the array
            res = findKSmallestSumFromTwoArr(mat[0], mat[1], k)  # row0 and row1
        else:
            res = findKSmallestSumFromTwoArr(mat[0], [0], k)  # row0 and row1; in case you only have 1 row

        for ii in range(2, len(mat)):
            res = findKSmallestSumFromTwoArr(res, mat[ii], k)  # row0 and row1

        return res[-1]

s=Solution()
o=s.kthSmallest([[14,15,21]], 3)
print("o: ", o)

"""
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:

        res = mat[0][:k] #we only care about the 1st k elements (candidates for combination)
        for row in mat[1:]: #from 2nd row (row0 is already coped to res above
            heap = [(n + row[0], 0) for n in res]#initialize min_heap from all elements of row0 with row1[0] combination
            res = [] #reset res as all elements are added min_heap
            for _ in range(k): # now calculate sum from row0 to curr_row, only care about 1st K cols(for loop)
                if not heap:
                    break
                s, i = heap[0] #output the current min to res
                res.append(s) #min is with next row, 1st element for sure
                if i == len(mat[0]) - 1:  #remove min from heap, if all members on this row is consumed, we just pop
                    heapq.heappop(heap)
                else:
                    heapq.heapreplace(heap, (s + row[i + 1] - row[i], i + 1)) # otherwise, we need to add the next
                                                                              # candidate from next element on same row
        return res[-1] #this is the Kth's min sum


"""
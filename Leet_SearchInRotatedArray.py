from timeit import default_timer as timer

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # find the turning point


        def bsearch(nums, ll, rr, key):
            print(f" bsearch ll={ll}, rr={rr}")
            if ll > rr:
                return -1


            while ll <= rr:
                mm = ll + (rr-ll)//2

                if nums[mm] > key:
                    rr=mm-1
                elif nums[mm] == key:
                    return mm
                else:
                    ll = mm+1

            return -1



        def tPoint(ll, rr):

            if nums[rr] > nums[ll]:
                return 0

            while ll <= rr:
                mm=ll+(rr-ll)//2

                if nums[rr] > nums[ll]:
                    return ll
                if nums[mm] == nums[ll]:
                    return rr
                elif nums[mm] > nums[ll]:
                    ll = mm+1
                elif mm > 1 and nums[mm] < nums[mm-1] and mm < n-1 and nums[mm] < nums[mm+1]:
                    return mm #found the lowest point
                else:
                    rr = mm-1

            return -1

        n = len(nums)
        ll = 0
        rr = n - 1

        if n == 0:
            return -1

        if n == 1:
            return 0 if nums[0] == target else -1

        tP = tPoint(ll, rr)

        print(f"tp={tP}, ll={ll}, rr={rr}")

        # find the partition
        # binary search the key
        if nums[n-1] >= target:
            oo = bsearch(nums, tP, n-1, target)
        else:
            oo = bsearch(nums, 0, tP, target)



        return oo

s=Solution()

start=timer()
#o=s.search([4,5,6,7,0,1,2], 2)
o=s.search([3, 1], 1)
end=timer()
print(end-start)
print("output:", o)
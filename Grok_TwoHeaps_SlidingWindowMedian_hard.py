from timeit import default_timer as timer
import heapq

class SlidingWindowMedian:

  def find_sliding_window_median(self, nums, k):
    result = []
    # set up min heap
    # set up max heap
    min_heap=[]
    max_heap=[]

    heapq.heapify(min_heap)
    heapq.heapify(max_heap)

    n = len(nums)

    """
    : * window size is K
    : * if max_heap is empty -> heappush to max_heap
    : * if next is greater than max_heap.top -> push to min_heap.  
    :   if len(min_heap) > len(max_heap) => pop max and push min
    : * if next is less than or equal to max_heap.top => push to in_heap.  
    :   if len(min_heap) > len(max_heap)+1 => pop min_heap and push to max_heap
    """
    def rebalance():
      if len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -1 * heapq.heappop(min_heap))
        return

      if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -1 * heapq.heappop(max_heap))
        return


    # traversing with the window and output to result
    for ii in range(n):
      if len(max_heap) == 0:
        heapq.heappush(max_heap, -1*nums[ii])
        continue

      if nums[ii] > -1*max_heap[0]:
        heapq.heappush(min_heap, nums[ii])
      else:
        heapq.heappush(max_heap, -1 * nums[ii])
      rebalance()

      if ii >= k-1:
        print("ii: ", ii)
        print("min_heap: ", min_heap)
        print("max_heap: ", max_heap)

        # remove the old one
        # add new node
        # re-heapify
        # output medium

        if len(max_heap) > len(min_heap):
          result.append(max_heap[0]*-1)
        else:
          result.append((min_heap[0]+ -1 * max_heap[0])/2)

        be_removed = nums[ii - k + 1]
        print("result: ", result)
        print(f"ii={ii}, k={k}, be_removed={be_removed}")

        if be_removed > -1 * max_heap[0]:  # remove from min_heap
          idx = min_heap.index(be_removed)
          min_heap[idx] = min_heap[-1]
          del min_heap[-1]
          heapq.heapify(min_heap)
        else:  # remove from max_heap
          idx = max_heap.index(-1 * be_removed)
          max_heap[idx] = max_heap[-1]
          del max_heap[-1]

        rebalance()

    return result

def main():
  """
  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))
  """
  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()

s = SlidingWindowMedian()

start = timer()

nums=[1, 2, -1, 3, 5]
k = 2

s.find_sliding_window_median(nums, k)
end = timer()




print("Time: ", end-start)
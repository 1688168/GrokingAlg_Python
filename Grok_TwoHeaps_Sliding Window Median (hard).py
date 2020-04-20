from timit import default_timer as timer


class SlidingWindowMedian:

  def find_sliding_window_median(self, nums, k):
    result = []
    # TODO: Write your code here
    return result

def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()

s = SlidingWindowMedian()

start = timer()

nums=[1, 2, -1, 3, 5]
k = 3

s.find_sliding_window_median(nums, k)
end = timer()




print("Time: ", end-start)
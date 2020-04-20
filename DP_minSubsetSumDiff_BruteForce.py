def can_partition(num):
  s = sum(num)

  return can_partition_recursive(num, 0, 0, 0)


def can_partition_recursive(num, idx, s1, s2):
    if idx >= len(num):
        return abs(s1-s2)

    diff1=can_partition_recursive(num, idx+1, s1+num[idx], s2)

    diff2=can_partition_recursive(num, idx+1, s1, s2+num[idx])



    return min(diff1, diff2)


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
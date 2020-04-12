def can_partition(num, sum):

    return can_partition_rec(num, sum, 0)

def can_partition_rec(num, ss, idx):
    if ss==0:
        return True

    if idx >= len(num) or idx < 0:
        return False

    can1=False
    if num[idx] <= ss:
        can1=can_partition_rec(num, ss-num[idx], idx+1)

    can2=can_partition_rec(num, ss, idx+1)

    return can1 or can2

def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()
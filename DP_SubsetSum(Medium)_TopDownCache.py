def can_partition(num, sum):
    dp=[[None for x in range(sum+1)] for y in range(len(num))]

    return can_partition_rec(num, sum, 0, dp)

def can_partition_rec(num, ss, idx, dp):
    if ss==0:
        return True

    if idx >= len(num) or idx < 0:
        return False

    if dp[idx][ss] is not None:
        return dp[idx][ss]

    can1=False
    if num[idx] <= ss:
        can1=can_partition_rec(num, ss-num[idx], idx+1, dp)

    can2=can_partition_rec(num, ss, idx+1, dp)

    dp[idx][ss]=can1 or can2

    return dp[idx][ss]

def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()
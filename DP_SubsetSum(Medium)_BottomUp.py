from pprint import pprint as pp

def can_partition(num, sum):
    dp=[[None for x in range(sum+1)] for y in range(len(num))]

    for ii in range(len(num)):
        dp[ii][0] = True


    for ii in  range(1,sum+1): #populate first row
        dp[0][ii] = num[0] == ii


    for ii in range(1, len(num)):
        for jj in range(1, sum+1):
            o1=False
            if num[ii] <= jj:
                o1 = dp[ii-1][jj-num[ii]]
            o2 = dp[ii-1][jj]
            dp[ii][jj] = o1 or o2

    pp(dp)

    return dp[len(num)-1][sum]



def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()
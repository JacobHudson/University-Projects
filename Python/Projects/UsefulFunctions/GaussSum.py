def PairSum(nums):
    r_nums = nums[::-1]
    sum  = 0
    for n in range(int(len(nums) / 2)):
        sum += nums[n] + r_nums[n]
    return sum

def GaussSum(nums):
    n = max(nums)
    #(number of pairs * sum of pairs)/2
    return (n*(n+1)) / 2

nums = [1,2,3,4,5,6,7,8,9,10,11,12]
print(PairSum(nums))
print(GaussSum(nums))
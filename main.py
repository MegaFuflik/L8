def kbig(nums, k):
    if (len(nums) == 0 or k <= 0 or k > len(nums)):
        return 0
    return(sorted(nums, reverse =True)[k-1])

if __name__ == "__main__":
    print(kbig([], 2))
    print(kbig([3,5,2], 2))
    print(kbig([3,5,2], 0))
    print(kbig([1,2,5,9], 1))
    print(kbig([3,2,1,5,6,4], 2))
    print(kbig([3,2,3,1,2,4,5,5,6], 4))
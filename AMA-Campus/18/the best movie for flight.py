import sys
def movie(nums, target):

    sum = sys.maxsize
    long_movie = 0
    maxvalue = 0
    for start in range(len(nums)):
        for end in range(1, len(nums)):
            value = nums[start] + nums[end]
            if value > target:
                continue
            else:
                diff = target - value
                if diff <= sum:
                    sum = diff
                    maxvalue = value
    # print(maxvalue)
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == maxvalue:
                print(i, j)
                if nums[i] > long_movie or nums[j] > long_movie:
                    if nums[i] > nums[j]:
                        long_movie = nums[i]
                        print(long_movie)
                    else:
                        long_movie = nums[j]
                        print(long_movie)
                    x = i
                    y = j
    return x+1, y+1


nums = [50, 25, 20, 40, 120, 95, 108, 128, 125, 105]
target = int(145)
print(movie(nums, target))



import sys
def movie(nums, target):
    sum = sys.maxsize
    result = []
    twoMovie = 0
    long_movie = 0
    for movie1 in range(len(nums)):
        for movie2 in range(len(nums)):
            if movie1 != movie2:
                if nums[movie1] + nums[movie2] <= target:
                    twoMovie = max(twoMovie, nums[movie1]+nums[movie2])

    for movie1 in range(len(nums)):
        for movie2 in range(len(nums)):
            if movie1 != movie2 and nums[movie1] + nums[movie2] == twoMovie:
                if nums[movie1] > long_movie or nums[movie2] > long_movie:
                    if nums[movie1] > nums[movie2]:
                        long_movie = nums[movie1]
                        print(long_movie)
                    else:
                        long_movie = nums[movie2]
                        print(long_movie)
                    x = movie1
                    y = movie2
    if nums[x] < nums[y]:
        nums[x], nums[y] = nums[y], nums[x]
        # result.append([nums[x], nums[y]])
    return nums[x], nums[y]
    # return nums[x], nums[y]

nums = [50, 25, 20, 40, 120, 95, 108, 128, 125, 105]
target = int(145)
print(movie(nums, target))

def two_sum(num1s,target):
    seen = {}
    for i, num in enumerate(num1s):
     complement = target - num
    if complement in seen:
        return [seen[complement],i]
    seen[num] = i
#def is the name of the function Two_sum with the parameters nums1(numbers) and target
#two_sum can be used to find sum of price product which are as per target
#seen creates a empty dictionary to store numbers we have already seen


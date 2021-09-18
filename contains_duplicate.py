def containsduplicate(nums):

    # 解法一
    #dic = {}
    # for i in nums:
    #    if i in dic:
    #        return True
    #    else:
    #        dic[i] = 1
    # return False

    # 解法二
    if len(set(nums)) == len(nums):
        return False
    return True


def main():
    print(containsduplicate([1, 2, 3, 1]))
    print(containsduplicate([1, 2, 3, 4]))
    print(containsduplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == "__main__":
    main()

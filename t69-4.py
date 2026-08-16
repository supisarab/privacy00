def find_pair_with_product(nums: list, targer: int) -> list:
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):  # แก้ระยะ
            if nums[i] * nums[j] == targer:  # แก้ระยะย่อหน้าตรงนี้
                result.append([nums[i], nums[j]])
    return result

print(find_pair_with_product([1, 2, 3, 4, 5, 6], 6))
print(find_pair_with_product([2, 4, 5, 7], 14))
print(find_pair_with_product([3, 5, 9, 10], 25))
print(find_pair_with_product([1, 2, 3, 4, 5], 20))
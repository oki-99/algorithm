"""
整数の配列 nums が与えられます。この配列から任意の3つの要素を選んで、その積を最大化するプログラムを作成してください。

入力:
整数配列 nums（要素数は3以上）
出力:
3つの要素の積の最大値
"""

def maximumProduct(nums):
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

# テストケース
nums = [-20, -10, 1, 2]
print(maximumProduct(nums))
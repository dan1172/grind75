class Solution:
    def containsDuplicate(self, nums):
        table = set()
        for num in nums:
            if num in table: return True
            table.add(num)
        return False
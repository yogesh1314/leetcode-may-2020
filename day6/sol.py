class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)//2
        x=Counter(nums)
        for i in x.items():
            if i[1]>n:
                return i[0]

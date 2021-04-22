class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = sorted(nums)
        a_pointer = 0
        b_pointer = len(n)-1
        res = []
        for i in range(len(n)-2):
            two_sum = self.twoSum(n,0-n[i],i+1)
            if two_sum:
                new_l = sorted([n[i]]+two_sum)
                if new_l not in res:
                    res.append(new_l)
        return res
    def twoSum(self,arr,x,a):
        b = len(arr)-1
        while a<b:
            if arr[a]+arr[b] < x:
                a+=1
            elif arr[a]+arr[b] > x:
                b-=1
            else:
                return [arr[a],arr[b]]
        return False

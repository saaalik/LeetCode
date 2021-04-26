class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = sorted(nums)
        a_pointer = 0
        b_pointer = len(n)-1
        res = []
        for i in range(len(n)-2):
            two_sum = self.twoSum(n,0-n[i],i+1)
            for triplet in two_sum:
                if triplet not in res:
                    res.append(triplet)
        return res
    def twoSum(self,arr,x,a):
        b = len(arr)-1
        temp_arr = []
        while a<b:
            if arr[a]+arr[b] < x:
                a+=1
            elif arr[a]+arr[b] > x:
                b-=1
            else:
                temp_arr.append([0-x,arr[a],arr[b]])
                a+=1
                b-=1
        if temp_arr:
            return temp_arr
        return temp_arr

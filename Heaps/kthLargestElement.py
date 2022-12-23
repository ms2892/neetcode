import heapq
class KthLargest:

    def __init__(self, k, nums):
        # self.heap=nums
        if len(nums)>=k:
            self.heap = nums[len(nums)-k:]
            print(len(self.heap))
        self.f=k        

    def add(self, val: int) -> int:
        pass

m = KthLargest(3, [4, 5, 8, 2])
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
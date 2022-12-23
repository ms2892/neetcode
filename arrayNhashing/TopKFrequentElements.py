from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k):
        dct=defaultdict(int)

        for i in nums:
            dct[i]+=1
        res=[]
        for i in dct:
            res.append([i,dct[i]])
        res.sort(key=lambda x:x[1],reverse=True)
        ans=[]
        for i in range(k):
            ans.append(res[i][0])

        return ans
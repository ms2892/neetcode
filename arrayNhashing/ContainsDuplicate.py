from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums):
        dct=defaultdict(int)
        flg_dup=0
        for i in nums:
            if dct[i]==0:
                dct[i]=1
            else:
                flg_dup=1
                break
        if flg_dup==1:
            return True
        else:
            return False
class Solution:
    def longestConsecutive(self, nums):
        # Function
        # Returns the length of the longest consecutive numbers present in the list of numbers
        # Input
        # nums  (list)  List of Numbers
        # Output
        # (int)     Length of the longest consecutive numbers
        
        # If the list is empty then return 0 as the answer
        if not nums:
            return 0
        
        # Remove Duplicate numbers in the list
        nums = list(set(nums))
        
        # Sort the numbers
        nums.sort()
        
        # Place Holder variables that will change in the while loop
        
        # Maximum length of the longest consecutive numbers it has come across
        mxm_so_far=1
        
        # Current length of the longest consecutive numbers it has come across
        curr_len = 1
        
        # Pointer variable pointing to the indices of the list
        ptr=0
        
        # Lenght of the list
        n=len(nums)
        
        # Approach based on the sliding window where after coming across consecutive numbers you start a new window
        while(ptr<n):
             
            # Length of the current element
            curr_len=1
            
            # Check how many consecutive numbers you can find
            while(ptr+1<n and nums[ptr+1]-nums[ptr]==1):
                ptr+=1
                curr_len+=1
                
            # Check if the length of these consecutives numbers is larger than the already existent maximum length found
            mxm_so_far = max(curr_len,mxm_so_far)
            
            # Move the pointer ahead and start a new window
            ptr+=1
        
        # Return the maximum Element Found
        return mxm_so_far

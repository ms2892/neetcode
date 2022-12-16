class Solution:
    def twoSum(self, nums, target) :
        # Function
        # Returns a pair of indices whose values add up to a given target number
        # Input
        #   nums    (list)  List of Numbers from which we have to find a pair
        #   target  (int)   target number that the pair have to add up to
        # Output
        #   (list)  Pair of Indices that signify the pair who's addition will lead to the target number
        
        # Blank Dictionary to act as our HashMap.
        dct={}

        # Go through the list of numbers one by one
        for i in range(len(nums)):

            # If we have come across a number that was equal to target - nums[i] then we return the pair of indices
            if target-nums[i] in dct.keys():
                return [dct[target-nums[i]],i]
            
            # If not then we save the indices of the current number
            dct[nums[i]]=i
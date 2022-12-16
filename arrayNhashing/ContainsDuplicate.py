from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums):
        # The Function that calculates if any duplicates are present in the list of numbers
        # Input:
        #   nums:   (list)  List of numbers
        # Output:
        #   (bool):         Returns True if there is a duplicate present else returns False
        
        
        # Initialize a special type of dictionary that can initialize a new key-value pair by setting its value to a default value.
        dct=defaultdict(int)
        
        # Flag to check if there are any duplicates present in the list. (Flag==0 means no Duplicates and Flag==1 means Duplicate present)
        flg_dup=0
        
        # Loop over every element in the list
        for i in nums:
            
            # Check if the number in consideration has been occurred before by checking its value in the dictionary.
            # If the value is zero then the number wasn't considered before
            if dct[i]==0:
                
                # Change the value of the key-value pair to signify it has occurred before
                dct[i]=1
            
            # If the number has occured before
            else:
                
                # Change the value of the flag
                flg_dup=1
                break
            
        # Based on the value of flag return True or False.
        if flg_dup==1:
            return True
        else:
            return False
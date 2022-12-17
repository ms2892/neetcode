class Solution:
    def productExceptSelf(self, nums):
        # Function
        # Returns a list of products that correspond to products of each element in the array except for the number at that position
        # Input
        #   nums    (list)  List of Numbers
        # Output
        #   (list)  List of products
        
        # Set a prefix_product
        prefix_prod=1
        
        # Counter for the number of zeroes in the array
        flg_zero=0
        
        # Check each and every element in the list
        for i in range(len(nums)):
            
            # If the number is not zero then simply multiply it to the prefix_product
            if nums[i]!=0:
                prefix_prod=nums[i]*prefix_prod
            else:
                # If the number is zero then simply increment the counter 
                flg_zero+=1
                
                # (Optional Optimization) : If the count of zeroes exceeds 1 then the product for every position would be zero 
                #                           and hence this loop can be exited prior to that
                #                           and a list of zeroes can be returned
        
        # Initialize the list of products
        res=[]
        
        # For every position
        for i in range(len(nums)):
            
            # If the number of zeroes is greater than 1 then keep on adding zeroes to the list
            if flg_zero>1:
                res.append(0)
            
            # If there is only 1 zero and the element at the position is zero then add the prefix_product 
            elif flg_zero==1 and nums[i]==0:
                res.append(prefix_prod)
            
            # If there is only 1 zero and the element at the position is not zero then add zero to the list
            elif flg_zero==1 and nums[i]!=0:
                res.append(0)
                
            # If there are no zeroes then add the prefix_product divided by the element at that position
            elif nums[i]!=0 and flg_zero==0:
                res.append(prefix_prod//nums[i])
                
        # Return the list of products
        return res
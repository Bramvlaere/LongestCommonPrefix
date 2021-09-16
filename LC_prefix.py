List=[]
class Solution:
    def longestCommonPrefix(self, strs: List=['flight','flow','fly']) -> str:
        
        #lets save the length of the string
        length_Array = len(strs)
        
        #if the length of array is zero there is no prefix 
        if length_Array == 0:
            return('')
        #then if the length of the array is only 1 then that 1 is the longest prefix
        if length_Array == 1:
            return f'{strs[0]}'
        
        #to start finding the prefix in multiple items we will start by making the prefix the first item in the list
        LC_prefix = strs[0]
        
        #we will also need to store the length of the prefix to determine how many letters of the first word are part of it
        #to start il take the length of the first word
        
        LCP_lenght =len(strs[0])
        
        for word in strs[1:]: #looping through the other strings but skipping the first one 
            
            while LC_prefix != word[0:LCP_lenght]: #in every word we compare the current lcprefix with the word we have
                LC_prefix = LC_prefix[0:LCP_lenght-1] #if the word doesn't match it will deduct one letter based on the length
                LCP_lenght-=1 #then we shorten the length
                
                if LCP_lenght == 0: #if the length of the prefix becomes 0 meaning nothing matches we return nothing
                    return('')
                
        #if that is done succesful we return the prefix
        return(LC_prefix) 

print(Solution.longestCommonPrefix(List))


      
        
        
                          
    
                          
                          
           
                          
        
            
                          
                               
        
        
            
        
        
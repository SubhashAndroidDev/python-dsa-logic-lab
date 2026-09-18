class Solution:
    def divide(self,dividend:int,divisor:int) ->int:
        
        #Spaecial overflow case
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        #deteemining wheter the answer should be negative 
        negative= (dividend<0) ^ (divisor<0)
        
        #work with positive numbers
        dividend=abs(dividend)
        divisor=abs(divisor)
        
        quotient=0
        while dividend >= divisor:
              temp=divisor
              multiple=1
              
              #find the largest doubled divisor
              while dividend >= (temp << 1):
                  temp <<= 1
                  multiple <<= 1
                  
               #subtract it
              dividend -= temp
              
              #add corresponding multiple
              quotient += multiple
              
            #apply the sign
        if negative:
            quotient = -quotient
        
        return quotient

print(Solution().divide(10,3))          
                  
              
              
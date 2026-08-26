class Solution:
    def myAtoi(self,s:str) -> int:
        i=0
        n=len(s)
        # 32 bit integer limits
        INT_MIN=-2**31
        INT_MAX=2**31 - 1
        #STEP 1: skip leading space
        while i< n and s[i]== '':
            i+=1

            # step2 check sign
            
            sign=1
            if i < n and s[i] == '-':
                sign=-1
                i+=1
            elif i<n and s[i] == '+':
                i+=1

            # step 3: convert digits
            num=0

            while i < n and s[i].isdigit():
                digit=int(s[i])

                num=num * 10 + digit

                i += 1

            # apply sign
            num=num*sign

            if num  < INT_MIN:
                return INT_MIN

            if num > INT_MAX:
                return INT_MAX

            return num

solution = Solution()

print(solution.myAtoi("42"))
print(solution.myAtoi(" -042"))
print(solution.myAtoi("1337c0d3"))
print(solution.myAtoi("0-1"))
print(solution.myAtoi("words and 987"))        



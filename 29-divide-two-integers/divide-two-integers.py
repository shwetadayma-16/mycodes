class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == 0:
            return 0
            
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
            
        negative = (dividend < 0) != (divisor < 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        count = 0
        a = 0
        
        while a + divisor <= dividend:
            temp = divisor
            multiple = 1
            
            while a + (temp << 1) <= dividend:
                temp = temp << 1
                multiple = multiple << 1
                
            a += temp
            count += multiple
            
        return -count if negative else count
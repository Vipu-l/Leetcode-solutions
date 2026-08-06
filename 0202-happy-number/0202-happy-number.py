class Solution:
    def isHappy(self, n: int) -> bool:
        def fun(n: int) -> int:
            sum = 0
            while(n > 0):
                d = n%10
                n = n//10
                sum = sum + d*d
            return sum
        
        slow = n
        fast = n
        while(fast != 1):
            slow = fun(slow)
            fast = fun(fast)
            fast = fun(fast)
            if(slow == fast and slow != 1):
                return False
        return True
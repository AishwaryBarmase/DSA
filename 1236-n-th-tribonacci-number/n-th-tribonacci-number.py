class Solution:
    def tribonacci(self, n: int) -> int:

        if n==0 or n==1:
            return n
        elif n==2:
            return 1
        
        answer = [0,1,1]
        for _ in range(3, n):
            answer.append(answer[-1] + answer[-2] + answer[-3])
        return answer[-1] + answer[-2] + answer[-3]
class Solution:
    def fib(self, n: int) -> int:
        answer = [0,1]
        if  n == 0:
            return 0
        elif n == 1:
            return 1

        else:

            for i in range(2, n):
                answer.append(answer[-1] + answer[-2])

        return (answer[-1] + answer[-2])

                
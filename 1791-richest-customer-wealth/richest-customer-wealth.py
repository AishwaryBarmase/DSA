class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        current_richest = sum(accounts[0])
        for i in range(1, (len(accounts))):
            if sum(accounts[i]) > current_richest:
                current_richest = sum(accounts[i])
        return current_richest
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        records = []
        for ops in operations:
            if ops == "+":
                item =records[-1] + records[-2]
                records.append(item)
            elif ops == "C":
                records.pop()
            elif ops == "D":
                total = records[-1] * 2 
                records.append(total)
            else:
                records.append(int(ops))
        
        return sum(records)


        
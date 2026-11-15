class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        TargetAchieved_Count= 0
        for emp_hours in hours:
            if emp_hours >= target:
                TargetAchieved_Count += 1
        return TargetAchieved_Count
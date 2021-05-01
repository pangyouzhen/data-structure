# Definition for Employee.
from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees_dict = {employee.id: employee for employee in employees}

        def dfs(employee_id):
            employee = employees_dict[employee_id]
            return employee.importance + sum(dfs(emp_id) for emp_id in employee.subordinates)

        return dfs(id)


if __name__ == '__main__':
    a = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
    employees = [Employee(i[0], i[1], i[2]) for i in a]
    sol = Solution()
    print(sol.getImportance(employees, 1))

# Write your MySQL query statement below
select E1.Name As "Employee"
from Employee as E1,Employee as E2
where E2.Id = E1.ManagerId and E1.Salary>E2.Salary

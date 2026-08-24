# Write your MySQL query statement below
select email as Email 
FROM Person 
GROUP BY email
having count(email)>1;
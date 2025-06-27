/* 
Link: https://leetcode.com/problems/combine-two-tables/description/?envType=problem-list-v2&envId=database
Problem 175: Combine Two Tables 
*/

-- Selects columns we want in output table
SELECT 
Person.firstName, 
Person.lastName, 
Address.city, 
Address.state

-- Joining tables from Person
FROM 
Person
  
--Left join to match all personId values with a corresponding name, city, and state
--Returns null if no personId can be matched from Person table
LEFT JOIN
Address ON Person.personId = Address.personId;


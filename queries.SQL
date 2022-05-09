-- Find all customers in Berlin
SELECT * FROM Customers
WHERE City="Berlin";

-- Find all customers in Mexico City
SELECT * FROM Customers
WHERE City="México D.F."

-- Find avg price of all products
SELECT AVG(Price) FROM Products 

-- Find number of products that have price=18
SELECT COUNT(ProductID)
FROM Products
WHERE Price=18;

-- Find orders between 1996-08-01 and 1996-09-06
SELECT orderID
FROM Orders
WHERE orderDate BETWEEN "1996-08-01" AND "1996-09-06";

-- Find customers with more than 3 orders
SELECT CustomerID, COUNT(CustomerID)
FROM Orders
GROUP BY CustomerID
HAVING COUNT(CustomerID) > 3

-- Find all customers that are from the same city
SELECT CustomerName, City FROM Customers 
WHERE City IN (SELECT City FROM Customers 
GROUP BY City HAVING COUNT(City) > 1)
ORDER BY City;
# Difference between below two queries.
#
#
# select s.name as salesperson, c.cust_name, s.city as salesman_city, c.city as customer_city
# from salesman s JOIN customer c
# on s.salesman_id = c.salesman_id
# where s.city = c.city;
#
#
# select s.name as salesperson, c.cust_name, s.city as salesman_city, c.city as customer_city
# from salesman s , customer c
# where s.city = c.city;
#

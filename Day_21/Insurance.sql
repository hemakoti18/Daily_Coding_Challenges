# create database
create database Insurance;
# use database
use Insurance;
# create table claims
CREATE TABLE claims ( 
claim_id INT, 
policy_holder VARCHAR(50), 
policy_type VARCHAR(50), 
claim_amount INT, 
claim_date DATE, 
status VARCHAR(20) 
); 
# insert values
INSERT INTO claims VALUES 
(1, 'Ravi', 'Health', 50000, '2024-01-10', 'Approved'), 
(2, 'Anita', 'Vehicle', 20000, '2024-01-12', 'Rejected'), 
(3, 'Ravi', 'Health', 30000, '2024-01-20', 'Approved'), 
(4, 'Suresh', 'Life', 100000, '2024-01-25', 'Approved'), 
(5, 'Anita', 'Vehicle', 15000, '2024-02-01', 'Approved'), 
(6, 'Kiran', 'Health', 40000, '2024-02-10', 'Rejected'), 
(7, 'Ravi', 'Health', 70000, '2024-02-15', 'Approved'), 
(8, 'Suresh', 'Life', 50000, '2024-02-20', 'Rejected'); 

# Task 1:  
# Find claims where claim amount is greater than average claim amount
# Individual per person Average ( middle Subquery + inner_Most subquery )
# subquery in where + subquery in from 
select 
    claim_id,
    claim_amount
from claims 
where claim_amount > ( select Avg(amount) from 
                           (select policy_holder,sum(claim_amount) as amount from claims group by policy_holder  ) as t   )  ;

# Individual per person Average ( With CTE + MainQuery_where - Subquery )
WITH Holder_Totals AS (
    SELECT policy_holder, SUM(claim_amount) AS total_amount 
    FROM claims 
    GROUP BY policy_holder
)
SELECT claim_id, claim_amount 
FROM claims 
WHERE claim_amount > (SELECT AVG(total_amount) FROM Holder_Totals);
                           

# Overall Avg Claim
select claim_id, policy_holder, claim_amount from claims 
where claim_amount > (select round(avg(claim_amount),0) as Avg_amount from claims ) ;

# Task 2:  
# Find policy holders who have at least one approved claim 
select 
	   distinct policy_holder,
       count(*) as count 
from claims s
where status = 'Approved' 
group by  policy_holder
having count(*) = 1 ;

# Task 3:  
# Find claims where claim amount is greater than that policy holder’s average claim
#  with CTE + main query - subquery
with holders_total as (
                        select c.policy_holder, Avg(c.claim_amount) as avg_amount 
							from Claims c
						    group by c.policy_holder )
select c.* from claims c
join holders_total h on h.policy_holder = c.policy_holder
where c.claim_amount > h.avg_amount ;
# another Approach
with holders_total as (
                        select c.policy_holder, sum(c.claim_amount) as total_amount 
							from Claims c
						    group by c.policy_holder )
select c.* from claims c
# join holders_total h on h.policy_holder = c.policy_holder
where c.claim_amount > ( select Avg(total_amount) from holders_total );

# Task 4:  
# Display each claim along with overall average claim amount 
select c.*, avg(c.claim_amount) over (partition by policy_holder) as avg_claim_amount
     from claims c ;
  
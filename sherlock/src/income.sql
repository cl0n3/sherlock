  SELECT rg.name as grp, to_char(date, 'YYYY-MM') as month, sum(amount) as total
    FROM transaction t, transaction_category tc, category_group cg, reporting_group rg
   WHERE t.category = tc.id
     AND tc.category_group = cg.id
     AND cg.reporting_group = rg.id
GROUP BY grp, month 
ORDER BY grp, month

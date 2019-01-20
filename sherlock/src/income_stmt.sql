  select rg.name as group, to_char(date, 'YYYY-MM') as month, sum(amount) as total
    from transaction t, transaction_group tg, spending_group sg, reporting_group rg
   where t.transaction_group = tg.id 
     and tg.spending_group = sg.id
	 and sg.reporting_group = rg.id
group by rg.name, month
order by rg.name, month

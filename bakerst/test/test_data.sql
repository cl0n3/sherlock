insert into reporting_group(name) values ('income');
insert into reporting_group(name) values ('mandatory');
insert into reporting_group(name) values ('discretionary');

insert into spending_group(name, reporting_group) values ('income', (select id from reporting_group where name = 'income'));
insert into spending_group(name, reporting_group) values ('transport', (select id from reporting_group where name = 'mandatory'));
insert into spending_group(name, reporting_group) values ('shopping', (select id from reporting_group where name = 'discretionary'));
insert into spending_group(name, reporting_group) values ('alcohol', (select id from reporting_group where name = 'discretionary'));

insert into transaction_group(name, spending_group) values ('taxis', (select id from spending_group where name = 'transport'));
insert into transaction_group(name, spending_group) values ('clothing', (select id from spending_group where name = 'shopping'));
insert into transaction_group(name, spending_group) values ('alcohol', (select id from spending_group where name = 'alcohol'));
insert into transaction_group(name, spending_group) values ('salary', (select id from spending_group where name = 'income'));

insert into transaction(amount, description, date, transaction_group) values (-59, 'industrie', '2017-07-15', (select id from transaction_group where name = 'clothing'));
insert into transaction(amount, description, date, transaction_group) values (-437, 'vintage cellars', '2018-04-10', (select id from transaction_group where name = 'alcohol'));
insert into transaction(amount, description, date, transaction_group) values (6437, 'optiver', '2018-01-23', (select id from transaction_group where name = 'salary'));

insert into account(bsb, account_no, name) values (1, 2744381, 'Trust');
insert into account(bsb, account_no, name) values (1, 2740488, 'Super');

--#insert into trade(account, price, volume, symbol, brokerage, side, time, exchange_trade_id) values ((select id from account where name = 'Trust'), 10.0, 100, 'FBR', 0.0, 'B', current_timestamp, '1');
--#insert into trade(account, price, volume, symbol, brokerage, side, time, exchange_trade_id) values ((select id from account where name = 'Trust'), 10.0, 100, 'ATC', 0.0, 'B', current_timestamp, '2');
--#insert into trade(account, price, volume, symbol, brokerage, side, time, exchange_trade_id) values ((select id from account where name = 'Trust'), 10.0, 100, 'XRO', 0.0, 'B', current_timestamp, '3');

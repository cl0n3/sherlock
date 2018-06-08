insert into reporting_group(name) values ('income');
insert into reporting_group(name) values ('mandatory');
insert into reporting_group(name) values ('discretionary');

insert into spending_category(name, reporting_group) values ('income', (select id from reporting_group where name = 'income'));
insert into spending_category(name, reporting_group) values ('transport', (select id from reporting_group where name = 'mandatory'));
insert into spending_category(name, reporting_group) values ('shopping', (select id from reporting_group where name = 'discretionary'));
insert into spending_category(name, reporting_group) values ('alcohol', (select id from reporting_group where name = 'discretionary'));

insert into transaction_type(name, spending_category) values ('taxis', (select id from spending_category where name = 'transport'));
insert into transaction_type(name, spending_category) values ('clothing', (select id from spending_category where name = 'shopping'));
insert into transaction_type(name, spending_category) values ('alcohol', (select id from spending_category where name = 'alcohol'));
insert into transaction_type(name, spending_category) values ('salary', (select id from spending_category where name = 'income'));

insert into transaction(amount, description, transaction_type) values (-59, 'industrie', (select id from transaction_type where name = 'clothing'))
insert into transaction(amount, description, transaction_type) values (-437, 'vintage cellars', (select id from transaction_type where name = 'alcohol'))
insert into transaction(amount, description, transaction_type) values (6437, 'optiver', (select id from transaction_type where name = 'salary'))

insert into trade(price, volume, symbol, brokerage, time) values (10.0, 100, 'FBR', 0.0, current_timestamp);
insert into trade(price, volume, symbol, brokerage, time) values (10.0, 100, 'ATC', 0.0, current_timestamp);
insert into trade(price, volume, symbol, brokerage, time) values (10.0, 100, 'XRO', 0.0, current_timestamp);




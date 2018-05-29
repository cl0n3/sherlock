drop table trade;
drop table price_snapshot;
drop table transaction;
drop table account;


create table trade (
	trade_id serial PRIMARY KEY,
	price numeric NOT NULL,
	volume integer NOT NULL,
	symbol char(3) NOT NULL,
	brokerage numeric NOT NULL,
	time timestamp NOT NULL
);

create table price_snapshot (
	id serial PRIMARY KEY,
	date date not null,
	symbol char(3) not null,
	open numeric not null, 
	high numeric not null,
	low numeric not null,
	close numeric not null,
	turnover integer not null,
	unique(date, symbol)
);

create table transaction (
	id serial primary key, 
	amount numeric not null,
	description text not null
);

create table account (
	id serial not null,
	bsb integer not null,
	account_no integer not null,
	name text not null
);

insert into trade(price, volume, symbol, brokerage, time) values (10.0, 100, 'FBR', 0.0, current_timestamp);
insert into trade(price, volume, symbol, brokerage, time) values (10.0, 100, 'ATC', 0.0, current_timestamp);
insert into trade(price, volume, symbol, brokerage, time) values (10.0, 100, 'XRO', 0.0, current_timestamp);




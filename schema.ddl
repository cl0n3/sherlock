drop table trade;
drop table price_snapshot;
drop table account;
drop table transaction;
drop table transaction_group;
drop table spending_group;
drop table reporting_group;

create table trade (
	trade_id serial primary key,
	price numeric not null,
	volume integer not null,
	symbol char(3) not null,
	brokerage numeric not null,
	time timestamp not null
);

create table price_snapshot (
	id serial primary key,
	date date not null,
	symbol char(3) not null,
	open numeric not null, 
	high numeric not null,
	low numeric not null,
	close numeric not null,
	turnover integer not null,
	unique(date, symbol)
);

create table account (
	id serial primary key,
	bsb integer not null,
	account_no integer not null,
	name text not null
);

create table reporting_group (
	id serial primary key,
	name text not null,
	unique(name)
);

create table spending_group (
	id serial primary key,
	name text not null,
	reporting_group integer references reporting_group(id),
	unique(name, reporting_group)
);

create table transaction_group (
	id serial primary key,
	name text not null,
	spending_group integer references spending_group(id)
);

create table transaction (
	id serial primary key, 
	amount numeric not null,
	description text not null,
	date date not null,
	transaction_group integer references transaction_group(id)
);

schema:
	psql -f schema.ddl

testdata:
	psql -f test_data.sql

db: schema testdata

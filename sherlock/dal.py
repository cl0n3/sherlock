import datetime from datetime
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String, DateTime, ForeignKey, Boolean, create_engine)


class DataAccessLayer:

    connection = None
    engine = None
    conn_string = None
    metadata = MetaData()
   
    def db_init(self, conn_string): 
        self.engine = create_engine(conn_string or self.conn_string)
        self.metadata.create_all(self.engine)
        self.connection = self.engine.connect()

dal = DataAccessLayer() 


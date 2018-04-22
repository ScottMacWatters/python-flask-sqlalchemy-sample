import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# This initailizes the Base class to extend all of our objects from
Base = declarative_base()

# Define a new Viewer object, which structures the viewers we will have
class Viewer(Base): 
    # The table name
    __tablename__ = 'viewer'
    # A primary key column named ID. This will auto-increment in most databases
    id = Column('id', Integer, primary_key=True)
    # A String column to store the IP address
    ip = Column('ip', String)


# A convenience method to save an instance to the database
def save(model):
    session = Session()
    session.add(model)
    session.commit()
    session.close()

# A convenience method to get the count of a specific model's rows in the databse
def count(model):
    session = Session()
    count=session.query(model).count()
    session.close()
    return count

# This URL will build a sqlite database in memory. 
# If this is used, nothing needs to be installed
# but nothing will be saved when the file stops running 
inMemoryDatabaseUrl='sqlite:///:memory:'

# Similar to how we get a port, this gets a Databse URL from the environment. 
# Many services may inject a DATABASE_URL to use instead. 
# With our list of requirements, only sqlite and postgresql will work
# but we can easily add more dialects using pip later if we need them
databaseUrl=os.environ.get("DATABASE_URL", inMemoryDatabaseUrl)

# This creates a database engine to access the database url provided. 
# Using the echo=True param, we can see the raw SQL output executed for us
engine = create_engine(databaseUrl, echo=True)

# This will create any tables for all objects defined using Base (see Viewer above)
Base.metadata.create_all(bind=engine)

# This defines a sessionmaker for our engine, allowing us to perform statements
# against the database as part of a session. 
Session = sessionmaker(bind=engine)

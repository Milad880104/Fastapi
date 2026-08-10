from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

SQLALCHEMY_DATABASE_URL="sqlite:///./sqlite.db"

engin=create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}

)

sessionlocal=sessionmaker(autoflush=False, autocommit=False, bind=engin)
C1=declarative_base()

class user(C1):
    __tablename__="user"
    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(30))
    def __repr__(slef):
        return f"user(id={slef.id},name={slef.first_name})"

C1.metadata.create_all(engin)

def get_DB():
    DB=sessionlocal()

    try:
        yield DB
    finally:
        DB.close()
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL="sqlite:///./sqlite.db"

engin=create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}

)

sessionlocal=sessionmaker(autoflush=False, autocommit=False, bind=engin)

C1=declarative_base()

class user(C1):
    __tablename__="user"
    id=Column(Integer, primary_key=True)
    first_name=Column(String(30))
    age=Column(Integer)
    def __repr__(slef):
        return f"user(id={slef.id},name={slef.first_name})"

C1.metadata.create_all(engin)

session=sessionlocal()
Eli=user(first_name="Eli", age=26)
Milad=user(first_name="milad", age=28)
Amir=user(first_name="amir", age=24)
uesrs=[Milad, Eli, Amir]
session.add_all(uesrs)
C3=session.query(user).filter_by(first_name="milad", id=13).first()
session.delete(C3)
session.commit()

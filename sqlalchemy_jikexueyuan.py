import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker

print(sqlalchemy.__version__)

engine=create_engine('sqlite:///foo.db',echo=True)
Base=declarative_base()

class User(Base):
    __tablename__='users'

    id1=Column(Integer,primary_key=True)
    name=Column(String)
    fullname=Column(String)
    password=Column(String)

    def __repr__(self):
        return "<User(name={},fullname={},password={})>".format\
            (self.name,self.fullname,self.password)

# Base.metadata.create_all(engine)
ed_user=User(name='ed',fullname='Ed Jones',password='edpassword')
# print('ed_user=',ed_user)

Session=sessionmaker(bind=engine)
session=Session()
print(session.query(User).count())
print(chr(19)*8)
# for i in session.query(User).filter(User.name .in_(['ed','n0'])).order_by(User.password):
#     print(i)
# session.add(ed_user)
# session.commit()
# u=set()
# for i in range(3):
#     u.add(User(name='n{}'.format(i),fullname='name{}'.format(i),password='pw{}'.format(i),))
# session.add_all(u)
# session.commit()
# our_user=session.query(User).filter_by(name='ed').first()

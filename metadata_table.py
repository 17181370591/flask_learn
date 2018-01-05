from sqlalchemy import Column,Integer,String,MetaData,Table,create_engine

engine=create_engine('sqlite:///foo.db',echo=True)
metadata=MetaData()

users=Table('users',metadata,
            Column('id',Integer,primary_key=True),
            Column('name',String,unique=True),
            Column('fullname',String),
            Column('password',String))

addresses=Table('addresses',metadata,
                Column('id',Integer,primary_key=True),
                Column('email',String,nullable=False),
                Column('user_id',Integer))

metadata.create_all(engine)
conn=engine.connect()
# conn.execute(users.insert(),[dict(name='jack',fullname='jack 1'),
#                             dict(name = 'wendy', fullname='wendy 1')])
add_l=(dict(user_id=1,email='email1'),dict(user_id=2,email='email2'),
       dict(user_id=1,email='email3'),dict(user_id=2,email='email4'))
# conn.execute(addresses.insert(),add_l)

s1='delete from addresses where email="p2"'
conn.execute(s1)
# for i in add_l:
#     conn.execute(s1.format(i['email'],i['user_id']))
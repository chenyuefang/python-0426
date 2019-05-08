from sqlalchemy import Column, INTEGER, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    """ Object - Relationship Mapping"""

    __tablename__ = 'user'

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    # toString()
    def __str__(self):
        print(self.id, self.email, self.password)
        return ''


engine = create_engine('mysql+mysqlconnector://root:system@localhost:3306/db_python')

DBSession = sessionmaker(bind=engine)

spike = User(email='spike@tom.com', password='123')

session = DBSession()

# session.add(spike)  # sql

# select * from db_python.user where id = 1
user = session.query(User).filter(User.id == 1).one()

# print(user.id)
# print(user.email)
# print(user.password)

print(user)

session.commit()

session.close()
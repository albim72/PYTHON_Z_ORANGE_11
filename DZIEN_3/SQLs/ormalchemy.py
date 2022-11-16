import mysql.connector
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:abc123@localhost:3306/dbtestowa',echo=True)

Base = declarative_base()
class User(Base):
    __tablename__='users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=50))
    fullname = sqlalchemy.Column(sqlalchemy.String(length=50))
    nickname = sqlalchemy.Column(sqlalchemy.String(length=50))

    def __repr__(self):
        return f"<User(name={self.name}, fullname:{self.fullname}, nickname:  {self.nickname}>"


Base.metadata.create_all(engine)
#Tworzenie sesji
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

#dodaj użytkownika do tabeli
j_user = User(name="Marcin",fullname="Marcin Albiniak", nickname="albim")
session.add(j_user)

k_user = User(name="Olga",fullname="Olga Kot", nickname="okot")
session.add(k_user)

session.commit()
Session = sessionmaker(bind=engine)
session = Session()
for s in session.query(User).all():
    print(s.fullname)

for s in session.query(User).filter(User.nickname == "okot"):
    print(s.fullname)


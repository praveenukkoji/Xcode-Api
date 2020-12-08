from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, JSON, Numeric, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(String, primary_key=True)
    usn = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    mobile_number = Column(String)
    gender = Column(String)
    image_url = Column(String)
    score = Column(Integer)
    date_of_birth = Column(DateTime)
    created_by = Column(String)
    created_on = Column(DateTime)
    modified_by = Column(String)
    modified_on = Column(DateTime)

    def __init__(self, user_id, usn, first_name, last_name, name, email, password, mobile_number, gender, image_url, score,
                 date_of_birth, created_by, created_on, modified_by, modified_on):
        self.user_id = user_id
        self.usn = usn
        self.first_name = first_name
        self.last_name = last_name
        self.name = name
        self.email = email
        self.password = password
        self.mobile_number = mobile_number
        self.gender = gender
        self.image_url = image_url
        self.score = score
        self.date_of_birth = date_of_birth
        self.created_by = created_by
        self.created_on = created_on
        self.modified_by = modified_by
        self.modified_on = modified_on


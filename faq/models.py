from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, JSON, Numeric, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FaqQuestion(Base):
    __tablename__ = 'faq_questions'

    question_id = Column(String, primary_key=True)
    user_id = Column(String)
    question_statement = Column(String)
    created_by = Column(String)
    created_on = Column(DateTime)
    modified_by = Column(String)
    modified_on = Column(DateTime)

    def __init__(self, question_id, user_id, question_statement, created_by, created_on, modified_by, modified_on):
        self.question_id = question_id
        self.user_id = user_id
        self.question_statement = question_statement
        self.created_by = created_by
        self.created_on = created_on
        self.modified_by = modified_by
        self.modified_on = modified_on


class FaqAnswer(Base):
    __tablename__ = 'faq_answers'

    answer_id = Column(String, primary_key=True)
    question_id = Column(String)
    user_id = Column(String)
    answer_statement = Column(String)
    created_by = Column(String)
    created_on = Column(DateTime)
    modified_by = Column(String)
    modified_on = Column(DateTime)

    def __init__(self, answer_id, question_id, user_id, answer_statement, created_by, created_on, modified_by, modified_on):
        self.answer_id = answer_id
        self.question_id = question_id
        self.user_id = user_id
        self.answer_statement = answer_statement
        self.created_by = created_by
        self.created_on = created_on
        self.modified_by = modified_by
        self.modified_on = modified_on

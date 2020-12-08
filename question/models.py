from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, JSON, Numeric, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Questions(Base):
    __tablename__ = 'questions'

    question_id = Column(String, primary_key=True)
    problem_title = Column(String)
    problem_statement = Column(String)
    difficulty_level = Column(String)
    category_id = Column(String)
    score = Column(Integer)
    input = Column(String)
    output = Column(String)
    constraints = Column(String)
    created_by = Column(String)
    created_on = Column(DateTime)
    modified_by = Column(String)
    modified_on = Column(DateTime)

    def __init__(self, question_id, problem_title, problem_statement, difficulty_level, category_id, score, input, output,
                 constraints, created_by, created_on, modified_by, modified_on):
        self.question_id = question_id
        self.problem_title = problem_title
        self.problem_statement = problem_statement
        self.difficulty_level = difficulty_level
        self.category_id = category_id
        self.score = score
        self.input = input
        self.output = output
        self.constraints = constraints
        self.created_by = created_by
        self.created_on = created_on
        self.modified_by = modified_by
        self.modified_on = modified_on


class TestCase(Base):
    __tablename__ = 'testcases'

    testcase_id = Column(String, primary_key=True)
    question_id = Column(String)
    input = Column(String)
    output = Column(String)
    created_by = Column(String)
    created_on = Column(DateTime)
    modified_by = Column(String)
    modified_on = Column(DateTime)

    def __init__(self, testcase_id, question_id, input, output, created_by, created_on, modified_by, modified_on):
        self.testcase_id = testcase_id
        self.question_id = question_id
        self.input = input
        self.output = output
        self.created_by = created_by
        self.created_on = created_on
        self.modified_by = modified_by
        self.modified_on = modified_on


class QuestionCategory(Base):
    __tablename__ = 'question_category'

    category_id = Column(String, primary_key=True)
    category = Column(String)
    created_by = Column(String)
    created_on = Column(DateTime)
    modified_by = Column(String)
    modified_on = Column(DateTime)

    def __init__(self, category_id, category, created_by, created_on, modified_by, modified_on):
        self.category_id = category_id
        self.category = category
        self.created_by = created_by
        self.created_on = created_on
        self.modified_by = modified_by
        self.modified_on = modified_on


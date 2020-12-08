from XcodeApi.connection import DBConnection
from question.models import QuestionCategory, Questions
from user.models import Users
from sqlalchemy.exc import SQLAlchemyError
import uuid
from datetime import datetime

from question.utils import get_category_payload, get_question_payload


# Question
class QuestionImplementation:
    def __init__(self, requests):
        self.requests = requests

    def get_question(self):
        payload = []
        count = 0
        try:
            questions = self.requests.get("question", None)
            with DBConnection() as session:
                if len(questions):
                    for question in questions:
                        query = session.query(Questions).filter(Questions.question_id == question)
                        data = query.all()
                        if data:
                            payload1, message, count = get_question_payload(data, count)
                            payload.append(payload1[0])
                        else:
                            payload.append({"question_id": question, "message": "Question doesn't exists."})
                    message = str(count) + " question fetched."
                else:
                    query = session.query(Questions)
                    data = query.all()
                    payload, message, count = get_question_payload(data, count)
            payload = sorted(payload, key=lambda k: k['created_on'], reverse=True)
        except Exception as e:
            print(e)
            raise e
        return payload, message

    def add_question(self):
        payload = []
        count = 0
        try:
            question_to_add = self.requests.get("question", None)
            with DBConnection() as session:
                for question in question_to_add:
                    _id = str(uuid.uuid4())
                    try:
                        query = session.query(QuestionCategory.category).\
                            filter(QuestionCategory.category_id == question['category_id'])
                        data = query.all()
                        if data:
                            new_question = Questions(
                                question_id=_id,
                                problem_title=question['problem_title'],
                                problem_statement=question['problem_statement'],
                                difficulty_level=question['difficulty'],
                                category_id=question['category_id'],
                                score=question['score'],
                                input=question['input'],
                                output=question['output'],
                                constraints=question['constraints'],
                                created_by=question['user_id'],
                                created_on=datetime.now(),
                                modified_by=question['user_id'],
                                modified_on=datetime.now()
                            )
                            query = session.query(Users).filter(Users.user_id == question['user_id'])
                            data1 = query.all()
                            if data1:
                                session.add(new_question)
                                session.commit()
                                payload.append({"question_id": _id, "message": "Added Successfully"})
                                count += 1
                            else:
                                payload.append(
                                    {"question_id": _id, "message": "User doesn't exists."})
                        else:
                            payload.append(
                                {"question_id": _id, "message": "Category doesn't exists."})
                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"question_id": _id, "message": str(e._message).split("Key (")[1].split(")")[0]
                                                                   + " already exists."})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        finally:
            return payload, str(count) + " question added."


    #TODO: update and delete question func


# Category
class CategoryImplementation:
    def __init__(self, requests):
        self.requests = requests

    def get_category(self):
        payload = []
        count = 0
        try:
            categories = self.requests.get("category", None)
            with DBConnection() as session:
                if len(categories):
                    for category in categories:
                        query = session.query(QuestionCategory).filter(QuestionCategory.category_id == category)
                        data = query.all()
                        if data:
                            payload1, message, count = get_category_payload(data, count)
                            payload.append(payload1[0])
                        else:
                            payload.append({"category_id": category, "message": "Category doesn't exists."})
                    message = str(count) + " category fetched."
                else:
                    query = session.query(QuestionCategory)
                    data = query.all()
                    payload, message, count = get_category_payload(data, count)
        except Exception as e:
            print(e)
            raise e
        return payload, message

    def add_category(self):
        payload = []
        count = 0
        try:
            category_to_add = self.requests.get("category", None)
            with DBConnection() as session:
                for category in category_to_add:
                    _id = str(uuid.uuid4())
                    try:
                        new_category = QuestionCategory(
                            category_id=_id,
                            category=category['name'],
                            created_by=category['user_id'],
                            created_on=datetime.now(),
                            modified_by=category['user_id'],
                            modified_on=datetime.now()
                        )
                        session.add(new_category)
                        session.commit()
                        payload.append({"category_id": _id, "category_name": category['name']})
                        count += 1
                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"message": str(e._message).split("Key (")[1].split(")")[0]
                                                                   + " already exists."})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        finally:
            return payload, str(count) + " category added."

    #TODO: update and delete category func

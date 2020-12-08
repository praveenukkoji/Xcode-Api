from faq.models import FaqQuestion, FaqAnswer
from user.models import Users
from faq.utils import get_question_payload, get_answer_payload
from XcodeApi.connection import DBConnection
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from sqlalchemy import func , asc, desc
from faq.utils import faq_question_columns
import uuid


# question
class FaqQuestionImplementation:
    def __init__(self, requests):
        self.requests = requests

    def get_faq_questions(self):
        payload = []
        count = 0
        try:
            faq_questions_to_find = self.requests.get("questions", None)
            with DBConnection() as session:
                if len(faq_questions_to_find):
                    for faq_question in faq_questions_to_find:
                        query = session.query(FaqQuestion).filter(FaqQuestion.question_id == faq_question)
                        data = query.all()
                        if data:
                            payload1, message, count = get_question_payload(data, count)
                            payload.append(payload1[0])
                        else:
                            payload.append({"question_id": faq_question, "message": "Question doesn't exists."})
                    message = str(count) + " questions fetched."
                else:
                    query = session.query(FaqQuestion)
                    data = query.all()
                    payload, message, count = get_question_payload(data, count)
            payload = sorted(payload, key=lambda k: k['question_added_date'], reverse=True)
        except Exception as e:
            print(e)
            raise e
        return payload, message

    def add_faq_questions(self):
        payload = []
        count = 0
        try:
            faq_questions_to_add = self.requests.get("questions", None)
            with DBConnection() as session:
                for faq_question in faq_questions_to_add:
                    _id = str(uuid.uuid4())
                    try:
                        new_faq_question = FaqQuestion(
                            question_id=_id,
                            user_id=faq_question['user_id'],
                            question_statement=faq_question['question_statement'],
                            created_by=faq_question['user_id'],
                            created_on=datetime.now(),
                            modified_by=faq_question['user_id'],
                            modified_on=datetime.now(),
                        )

                        session.query(Users).filter(Users.user_id == faq_question['user_id'])

                        if faq_question['question_statement']:
                            session.add(new_faq_question)
                            session.commit()
                            payload.append({"question_id": _id, "message": "added successfully."})
                            count += 1
                        else:
                            payload.append({"question_id": _id,
                                            "message": "question statement cannot be empty."})
                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"question_id": _id,
                                        "message": str(e._message).split("Key (")[1].split("_")[0] + " doesn't exists."})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        finally:
            return payload, str(count) + " questions added."

    def update_faq_questions(self):
        payload = []
        count = 0
        try:
            questions_to_update = self.requests.get("questions", None)
            with DBConnection() as session:
                for question in questions_to_update:
                    columns_to_update = {}
                    columns_to_update[FaqQuestion.question_statement] = question['question_statement']
                    columns_to_update[FaqQuestion.modified_by] = question['user_id']
                    columns_to_update[FaqQuestion.modified_on] = datetime.now()

                    try:
                        query = session.query(FaqQuestion).filter(FaqQuestion.question_id == question['question_id']) \
                            .update(columns_to_update, synchronize_session=False)
                        session.commit()
                        if query:
                            count += 1
                            payload.append({"question_id": question['question_id'], "message": "updated successfully."})
                        else:
                            payload.append(
                                {"question_id": question['question_id'], "message": "Question doesn't exist."})

                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"question_id": question['question_id'], "message": str(e._message)})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " questions updated."

    def delete_faq_questions(self):
        payload = []
        count = 0
        try:
            faq_question_to_delete = self.requests.get('questions', None)
            with DBConnection() as session:
                for faq_question in faq_question_to_delete:
                    query = session.query(FaqQuestion).filter(FaqQuestion.question_id == faq_question) \
                        .delete(synchronize_session=False)
                    if query:
                        count += 1
                        payload.append({"question_id": faq_question, "message": "Deleted successfully."})
                        session.commit()
                    else:
                        payload.append({"question_id": faq_question, "message": "Question doesn't exists."})
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " questions deleted."


# answers
class FaqAnswerImplementation:
    def __init__(self, requests):
        self.requests = requests

    def get_faq_answers(self):
        payload = []
        count = 0
        try:
            faq_answers_to_find = self.requests.get("answers", None)
            with DBConnection() as session:
                if len(faq_answers_to_find):
                    for faq_answer in faq_answers_to_find:
                        query = session.query(FaqAnswer).filter(FaqAnswer.answer_id == faq_answer)
                        data = query.all()
                        if data:
                            payload1, message, count = get_answer_payload(data, count)
                            payload.append(payload1[0])
                        else:
                            payload.append({"answer_id": faq_answer, "message": "Answer doesn't exists."})
                    message = str(count) + " answers fetched."
                else:
                    query = session.query(FaqAnswer)
                    data = query.all()
                    payload, message, count = get_answer_payload(data, count)
            payload = sorted(payload, key=lambda k: k['answer_added_date'], reverse=True)
        except Exception as e:
            print(e)
            raise e
        return payload, message

    def add_faq_answers(self):
        payload = []
        count = 0
        try:
            faq_answers_to_add = self.requests.get("answers", None)
            with DBConnection() as session:
                for faq_answer in faq_answers_to_add:
                    _id = str(uuid.uuid4())
                    try:
                        new_faq_answer = FaqAnswer(
                            answer_id=_id,
                            question_id=faq_answer["question_id"],
                            user_id=faq_answer['user_id'],
                            answer_statement=faq_answer['answer_statement'],
                            created_by=faq_answer['user_id'],
                            created_on=datetime.now(),
                            modified_by=faq_answer['user_id'],
                            modified_on=datetime.now(),
                        )

                        session.query(Users).filter(Users.user_id == faq_answer['user_id'])

                        if faq_answer['answer_statement']:
                            session.add(new_faq_answer)
                            session.commit()
                            payload.append({"answer_id": _id, "message": "added successfully."})
                            count += 1
                        else:
                            payload.append({"answer_id": _id,
                                            "message": "answer statement cannot be empty."})
                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"answer_id": _id,
                                        "message": str(e._message).split("Key (")[1].split("_")[0] + " doesn't exists."})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        finally:
            return payload, str(count) + " answers added."

    # Update
    def update_faq_answers(self):
        payload = []
        count = 0
        try:
            answers_to_update = self.requests.get("answers", None)
            with DBConnection() as session:
                for answer in answers_to_update:
                    columns_to_update = {}
                    columns_to_update[FaqAnswer.answer_statement] = answer['answer_statement']
                    columns_to_update[FaqAnswer.modified_by] = answer['user_id']
                    columns_to_update[FaqAnswer.modified_on] = datetime.now()

                    try:
                        query = session.query(FaqAnswer).filter(FaqAnswer.answer_id == answer['answer_id'])\
                            .update(columns_to_update, synchronize_session=False)
                        session.commit()
                        if query:
                            count += 1
                            payload.append({"answer_id": answer['answer_id'], "message": "updated successfully."})
                        else:
                            payload.append({"answer_id": answer['answer_id'], "message": "Answer doesn't exist."})

                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"answer_id": answer['answer_id'], "message": str(e._message)})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " answer updated."

    def delete_faq_answers(self):
        payload = []
        count = 0
        try:
            faq_answers_to_delete = self.requests.get('answers', None)
            with DBConnection() as session:
                for faq_answer in faq_answers_to_delete:
                    query = session.query(FaqAnswer).filter(FaqAnswer.answer_id == faq_answer) \
                        .delete(synchronize_session=False)
                    if query:
                        count += 1
                        payload.append({"answer_id": faq_answer, "message": "Deleted successfully."})
                        session.commit()
                    else:
                        payload.append({"answer_id": faq_answer, "message": "Answer doesn't exists."})
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " answers deleted."

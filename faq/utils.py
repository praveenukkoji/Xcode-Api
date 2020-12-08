from faq.models import FaqQuestion, FaqAnswer
from user.models import Users
from XcodeApi.connection import DBConnection
from sqlalchemy.exc import SQLAlchemyError

# question
def get_question_payload(data, count):
    try:
        payload = []
        for faq_question in data:
            with DBConnection() as session:
                try:
                    query = session.query(Users).filter(Users.user_id == faq_question.user_id)
                    data1 = query.all()
                    query = session.query(FaqAnswer).filter(faq_question.question_id == FaqAnswer.question_id)
                    data2 = query.count()
                    if data1:
                        for user in data1:
                            date = str(faq_question.modified_on).split("T")[0].split(".")[0]
                            new_faq_question = {
                                "question_id": faq_question.question_id,
                                "user_id": faq_question.user_id,
                                "user_name": user.name,
                                "user_pic": user.image_url,
                                "question_statement": faq_question.question_statement,
                                "question_added_date": date,
                                "count_of_answers": data2
                            }
                            payload.append(new_faq_question)
                            count += 1
                except SQLAlchemyError as e:
                    print(e)
                    payload.append({"message": str(e._message).split("Key (")[1].split("_")[0] + " doesn't exists."})
                    session.rollback()
    except Exception as e:
        print(e)
        raise e
    return payload, str(count) + " questions fetched.", count

faq_question_columns = {
    "question_id": FaqQuestion.question_id,
    "user_id": FaqQuestion.user_id,
    "question_statement": FaqQuestion.question_statement
}

# answer
def get_answer_payload(data, count):
    try:
        payload = []
        for faq_answer in data:
            with DBConnection() as session:
                try:
                    query = session.query(Users).filter(Users.user_id == faq_answer.user_id)
                    data1 = query.all()
                    if data1:
                        for user in data1:
                            date = str(faq_answer.modified_on).split("T")[0].split(".")[0]
                            new_faq_answer = {
                                "answer_id": faq_answer.answer_id,
                                "question_id": faq_answer.question_id,
                                "user_id": faq_answer.user_id,
                                "user_name": user.name,
                                "user_pic": user.image_url,
                                "answer_statement": faq_answer.answer_statement,
                                "answer_added_date": date
                            }
                            payload.append(new_faq_answer)
                            count += 1
                except SQLAlchemyError as e:
                    print(e)
                    payload.append({"message": str(e._message).split("Key (")[1].split("_")[0] + " doesn't exists."})
                    session.rollback()
    except Exception as e:
        print(e)
        raise e
    return payload, str(count) + " answers fetched.", count
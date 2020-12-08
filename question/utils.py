# from question.models import QuestionCategory
from question.models import QuestionCategory
from XcodeApi.connection import DBConnection

# category
def get_category_payload(data, count):
    try:
        payload = []
        for category in data:
            new_category = {
                "category_id": category.category_id,
                "category_name": category.category
            }
            payload.append(new_category)
            count += 1
    except Exception as e:
        print(e)
        raise e
    return payload, str(count) + " category fetched.", count

# question
def get_question_payload(data, count):
    try:
        payload = []
        for question in data:
            with DBConnection() as session:
                query = session.query(QuestionCategory).filter(QuestionCategory.category_id == question.category_id)
                data1 = query.all()
                new_question = {
                    "question_id": question.question_id,
                    "title": question.problem_title,
                    "statement": question.problem_statement,
                    "difficulty": question.difficulty_level,
                    "category": str(data1[0].category),
                    "score": question.score,
                    "input": question.input,
                    "output": question.output,
                    "constraint": question.constraints,
                    "created_on": question.created_on
                }
                payload.append(new_question)
                count += 1
    except Exception as e:
        print(e)
        raise e
    return payload, str(count) + " question fetched.", count

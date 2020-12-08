from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
import json
from question.implementations.implementations import CategoryImplementation, QuestionImplementation

# Question


class GetQuestionController(GenericAPIView):
    def post(self, request):
        try:
            response = {"status": 200, "payload": "", "message": "", "error": ""}
            requests = json.load(request)
            question_implementation = QuestionImplementation(requests)
            payload, message = question_implementation.get_question()
            if payload:
                response['payload'] = payload
                response['message'] = message
            else:
                response['message'] = ""
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class AddQuestionController(GenericAPIView):
    def post(self, request):
        try:
            response = {"status": 200, "payload": "", "message": "", "error": ""}
            requests = json.load(request)
            question_implementation = QuestionImplementation(requests)
            payload, message = question_implementation.add_question()
            if payload:
                response['payload'] = payload
                response['message'] = message
            else:
                response['message'] = ""
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)

# Category


class GetCategoryController(GenericAPIView):
    def post(self, request):
        try:
            response = {"status": 200, "payload": "", "message": "", "error": ""}
            requests = json.load(request)
            category_implementation = CategoryImplementation(requests)
            payload, message = category_implementation.get_category()
            if payload:
                response['payload'] = payload
                response['message'] = message
            else:
                response['message'] = ""
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class AddCategoryController(GenericAPIView):
    def post(self, request):
        try:
            response = {"status": 200, "payload": "", "message": "", "error": ""}
            requests = json.load(request)
            category_implementation = CategoryImplementation(requests)
            payload, message = category_implementation.add_category()
            if payload:
                response['payload'] = payload
                response['message'] = message
            else:
                response['message'] = ""
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
import json
from faq.implementations.implementations import FaqQuestionImplementation, FaqAnswerImplementation

# question
class GetFaqQuestionController(GenericAPIView):
    def post(self, request):
        try:
            response = {"status": 200, "payload": "", "message": "", "error": ""}
            requests = json.load(request)
            faq_question_implementation = FaqQuestionImplementation(requests)
            payload, message = faq_question_implementation.get_faq_questions()
            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class AddFaqQuestionController(GenericAPIView):
    def post(self, request):
        try:
            response = {"status": 200, "payload": "", "message": "", "error": ""}
            requests = json.load(request)
            faq_question_implementation = FaqQuestionImplementation(requests)
            payload, message = faq_question_implementation.add_faq_questions()
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


class UpdateFaqQuestionController(GenericAPIView):
    def post(self, request):
        try:
            response = {"status": 200, "payload": "", "message": "", "error": ""}
            requests = json.load(request)
            faq_question_implementation = FaqQuestionImplementation(requests)
            payload, message = faq_question_implementation.update_faq_questions()
            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class DeleteFaqQuestionController(GenericAPIView):
    def post(self, request):
        try:
            response = {"status": 200, "payload": "", "message": "", "error": ""}
            requests = json.load(request)
            faq_question_implementation = FaqQuestionImplementation(requests)
            payload, message = faq_question_implementation.delete_faq_questions()
            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


# answer
class GetFaqAnswerController(GenericAPIView):
    def post(self, request):
        try:
            response = {"status": 200, "payload": "", "message": "", "error": ""}
            requests = json.load(request)
            faq_answer_implementation = FaqAnswerImplementation(requests)
            payload, message = faq_answer_implementation.get_faq_answers()
            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class AddFaqAnswerController(GenericAPIView):
    def post(self, request):
        try:
            response = {"status": 200, "payload": "", "message": "", "error": ""}
            requests = json.load(request)
            faq_answer_implementation = FaqAnswerImplementation(requests)
            payload, message = faq_answer_implementation.add_faq_answers()
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


class UpdateFaqAnswerController(GenericAPIView):
    def post(self, request):
        try:
            response = {"status": 200, "payload": "", "message": "", "error": ""}
            requests = json.load(request)
            faq_answer_implementation = FaqAnswerImplementation(requests)
            payload, message = faq_answer_implementation.update_faq_answers()
            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class DeleteFaqAnswerController(GenericAPIView):
    def post(self, request):
        try:
            response = {"status": 200, "payload": "", "message": "", "error": ""}
            requests = json.load(request)
            faq_answer_implementation = FaqAnswerImplementation(requests)
            payload, message = faq_answer_implementation.delete_faq_answers()
            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)
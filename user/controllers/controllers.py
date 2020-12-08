from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
import json
from user.implementations.implementations import UserImplementation


class LoginUserController(GenericAPIView):
    def post(self, request):
        try:
            response = {"status": 200, "payload": "", "message": "", "error": ""}
            requests = json.load(request)
            user_implmentation = UserImplementation(requests)
            payload, message = user_implmentation.login_user()
            if payload:
                response['payload'] = payload
                response['message'] = message
            else:
                response['message'] = "Invalid Crendentials."
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class GetUserController(GenericAPIView):
    def post(self, request):
        try:
            response = {"status": 200, "payload": "", "message": "", "error": ""}
            requests = json.load(request)
            user_implmentation = UserImplementation(requests)
            payload, message = user_implmentation.get_users()
            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class CreateUserController(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = json.load(requests)
            user_implmentation = UserImplementation(requests)
            payload, message = user_implmentation.create_users()

            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class UpdateUserController(GenericAPIView):
    def post(self, request):
        try:
            response = {"status": 200, "payload": "", "message": "", "error": ""}
            requests = json.load(request)
            user_implmentation = UserImplementation(requests)
            payload, message = user_implmentation.update_users()
            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class DeleteUserController(GenericAPIView):
    def post(self, request):
        try:
            response = {"status": 200, "payload": "", "message": "no message", "error": ""}
            requests = json.load(request)
            user_implmentation = UserImplementation(requests)
            payload, message = user_implmentation.delete_users()
            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)


class TopPerformerUserController(GenericAPIView):
    def post(self, request):
        try:
            response = {"status": 200, "payload": "", "message": "", "error": ""}
            requests = json.load(request)
            user_implmentation = UserImplementation(requests)
            payload, message = user_implmentation.top_performer_users()
            if payload:
                response['payload'] = payload
                response['message'] = message
        except Exception as e:
            print(e)
            response['error'] = str(e)
        finally:
            return JsonResponse(response)
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from execute.implementation.implementation import OnlineCompiler
import json


class ExecuteIde(GenericAPIView):
    def post(self, request, **kwargs):
        try:
            response = {
                'status': 200,
                'payload': "",
                'message': "",
                'error': ""
            }
            request = json.load(request)

            online_compiler_obj = OnlineCompiler(request)
            payload, message = online_compiler_obj.getOutput()

            if payload:
                response['payload'] = payload
            response['message'] = message

        except Exception as e:
            print(e)
            response['message'] = "Some error occured"
            response['error'] = e

        return JsonResponse(response)


class ExecuteFile(GenericAPIView):
    def post(self, request, *kwargs):
        try:
            response = {
                'status': 200,
                'payload': "",
                'message': "",
                'error': ""
            }

            online_compiler_obj = OnlineCompiler(request)
            payload = ""

            if payload:
                response['payload'] = payload

        except Exception as e:
            print(e)
            response['message'] = "Some error occured"
            response['error'] = e

        return JsonResponse(response)
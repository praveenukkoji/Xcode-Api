from django.urls import path

from question.controllers.controllers import GetCategoryController, AddCategoryController, \
    GetQuestionController, AddQuestionController

urlpatterns = [
    # category
    path('get_category/', GetCategoryController.as_view()),
    path('add_category/', AddCategoryController.as_view()),

    # question
    path('add_question/', AddQuestionController.as_view()),
    path('get_question/', GetQuestionController.as_view())
]
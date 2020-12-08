from django.urls import path

from faq.controllers.controllers import \
    GetFaqQuestionController,\
    AddFaqQuestionController,\
    UpdateFaqQuestionController,\
    DeleteFaqQuestionController,\
    GetFaqAnswerController,\
    AddFaqAnswerController,\
    UpdateFaqAnswerController,\
    DeleteFaqAnswerController

urlpatterns = [
    # question
    path('get_faq-questions/', GetFaqQuestionController.as_view()),
    path('add_faq-questions/', AddFaqQuestionController.as_view()),
    path('update_faq-questions/', UpdateFaqQuestionController.as_view()),
    path('delete_faq-questions/', DeleteFaqQuestionController.as_view()),
    # answer
    path('get_faq-answers/', GetFaqAnswerController.as_view()),
    path('add_faq-answers/', AddFaqAnswerController.as_view()),
    path('update_faq-answers/', UpdateFaqAnswerController.as_view()),
    path('delete_faq-answers/', DeleteFaqAnswerController.as_view())
]
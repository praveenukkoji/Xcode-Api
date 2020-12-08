from django.urls import path, include
from execute.controller.controller import ExecuteIde, ExecuteFile

urlpatterns = [
    path('executeidecode/', ExecuteIde.as_view())
    # path('executefilecode/', ExecuteFile.as_view())
]
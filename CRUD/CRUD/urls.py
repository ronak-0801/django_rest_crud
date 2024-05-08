
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_api/', views.List_Create_api.as_view()),
    path('student_api/<int:pk>',views.Retrieve_Update_Delete_api.as_view())
]

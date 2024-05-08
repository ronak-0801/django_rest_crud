
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()

router.register('crud_api',views.Crudapi,basename='crud')
router.register('readonly_api',views.Read_only_api,basename='read_only')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]

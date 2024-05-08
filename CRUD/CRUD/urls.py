
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter 
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router = DefaultRouter()

router.register('crud_api', views.Crudapi,basename='crud')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),

    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(),name='refresh_token'),
    path('verifytoken/',TokenVerifyView.as_view(),name='Verify_token'),
]

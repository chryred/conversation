from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='login'),
    path("token/", TokenObtainPairView.as_view(), name='token'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("token/verify/", TokenVerifyView.as_view(), name='token_verify'),
]

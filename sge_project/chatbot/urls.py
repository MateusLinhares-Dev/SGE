from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/chatbot/', views.ChatbotAPIView.as_view(), name="chatbot_view")
]

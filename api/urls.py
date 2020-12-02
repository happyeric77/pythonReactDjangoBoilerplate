from django.urls import path, include
from .views import DemoView


urlpatterns = [
    path('demo/', DemoView.as_view()),
]
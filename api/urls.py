from django.urls import path
from .views import PenziMessageView

urlpatterns = [
    path('receive-message/', PenziMessageView.as_view(), name='receive_message'),
]

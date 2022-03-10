from django.urls import path
from .views import MyView

app_name = 'main'

urlpatterns = [
    path('', MyView.as_view(), name='index')
]

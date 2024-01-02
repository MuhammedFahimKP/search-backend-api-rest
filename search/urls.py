from django.urls import path
from . import views


urlpatterns = [
    path('',views.SearchListNewApiView.as_view())
]

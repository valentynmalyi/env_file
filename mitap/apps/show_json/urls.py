from django.urls import path
from mitap.apps.show_json import views

urlpatterns = [
    path("", views.ShowJson.as_view()),
]

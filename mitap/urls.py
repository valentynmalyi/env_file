from django.urls import include, path

urlpatterns = [
    path("", include("mitap.apps.show_json.urls")),
]

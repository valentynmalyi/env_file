from django.http import JsonResponse
from django.views import View


class ShowJson(View):
    # noinspection PyMethodMayBeStatic
    def get(self, request, *args, **kwargs):
        show_json = {"hello": "world"}
        return JsonResponse(show_json)


from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def my_view(request):
    car_list = [
        {"title": "BMW"},
        {"title":"FIAT"}
    ]
    context = {
        "car_list": car_list
    }
    return render(request,"my_first_app/car_list.html", context)

class CarlistView(TemplateView): 
    template_name = "my_first_app/car_list.html"

    def get_context_data(self):
       car_list = [
            {"title": "BMW"},
            {"title":"FIAT"}
        ]
       return {
            "car_list": car_list
        }


def my_test_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")
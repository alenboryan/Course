from django.shortcuts import render
from .models import Course
from django.shortcuts import HttpResponse


def index(request):
    all_title = Course.objects.order_by
    context = {"all_title":all_title}
    return render(request, "polls/all_courses.html", context)


def all_info(request):
    all_info = Course.objects.all()
    context = {'all_info': all_info}
    return render(request, "polls/all_info.html", context)




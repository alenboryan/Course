from django.shortcuts import render
from .models import Course
from django.shortcuts import HttpResponse


def index(request):
    all_title = Course.objects.order_by
    context = {"all_title":all_title}
    return render(request, "polls/all_courses.html", context)

def rate(request):
    courses_ordered_by_rating = Course.objects.order_by('-rating')

    context = {"courses_ordered_by_rating": courses_ordered_by_rating}
    return render(request, 'index.html', context)


def all_info(request):
    all_courses = Course.objects.all()
    context = {'all_courses': all_courses}
    return render(request, 'all_courses.html', context)



    
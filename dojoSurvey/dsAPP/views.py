from django.shortcuts import render, HttpResponse
def index(request):
    return render(request, "index.html")


def result(request):
    context = {
        "student": request.POST["student_name"],
        "location": request.POST["dojo_location"],
        "language": request.POST["favorite_language"],
        "comment": request.POST["comment"]
    }
    return render(request, "result.html", context)

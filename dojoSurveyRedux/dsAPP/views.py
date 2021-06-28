from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, "index.html")


def result(request):
    request.session["student"] = request.POST["student_name"]
    request.session["location"] = request.POST["dojo_location"]
    request.session["language"] = request.POST["favorite_language"]
    request.session["comment"] = request.POST["comment"]
    return redirect("/dashboard")

def dashboard(request):
    context = {
        "student": request.session["student"],
        "location": request.session["location"],
        "language": request.session["language"],
        "comment": request.session["comment"]
    }
    return render(request, "result.html", context)

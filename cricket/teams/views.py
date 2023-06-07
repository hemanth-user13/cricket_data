from django.shortcuts import render
from .models import  *
# Create your views here.
def teams_data(request):
    if request.method == "POST":
        name = request.POST.get("team_name")
        print(name)
        if name == "india":
            data = teams.objects.filter(country="india").values()
        elif name == "england":
            data = teams.objects.filter(country="england").values()
        else:
            data = teams.objects.values()

        return render(request,"team.html",{"data":data})
    flag="home"
    return render(request,"team.html",{"home":flag})


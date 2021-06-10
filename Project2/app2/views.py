from django.shortcuts import render

def show(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        Password = request.POST.get('Password')
        if username == "maria" and Password == "kumar":
            return render(request,"login.html",{"message":"Valid"})
        else:
            return render(request,"login.html",{"message":"Invalid"})
    else:
        return render(request,"login.html")

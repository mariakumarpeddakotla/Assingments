from django.shortcuts import render

def showIndex(request):
    return render(request,"login.html")

def registercheck(request):
    user_name = request.POST.get('name')
    Password = request.POST.get('password')
    if user_name == 'maria kumar' and Password == '1234':
        return render(request,"welcome.html")
    else:
        return render(request,"error.html")

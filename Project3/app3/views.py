from django.shortcuts import render

def showIndex(request):
    username = request.POST.get('name')
    password = request.POST.get('password')
    type = request.POST.get('type')
    if request.method == 'POST':
        if username == 'Ravi' and password == 'ravi1234@' and type == 'Admin':
            return render(request,"welcome.html",{"message":"admin"})
        elif username == 'Ravi' and password == 'kumar@123' and type == 'Employee':
            return render(request,"welcome.html",{"message":"employee"})
        elif username == 'Ravi' and password == 'ravikumar@123' and type == 'Customer':
            return render(request,"welcome.html",{"message":"customer"})
        else:
            return render(request,"index.html",{"message":"Invalid"})
    else:
        return render(request,"index.html")


from django.shortcuts import render

def registerView(request):
    return render(request, 'userAuths/register.html')


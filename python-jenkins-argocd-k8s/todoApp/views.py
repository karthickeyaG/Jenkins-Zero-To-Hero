from django.shortcuts import redirect

def index(request):
    print("playing with git")
    return redirect('/todos')


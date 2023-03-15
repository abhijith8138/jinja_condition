from django.shortcuts import render

# Create your views here.
def ifcondition (request):
    d={'a':150}
    return render(request,'if.html',d)

def ifelse(request):
    c={'a':200,'b':30}
    return render(request,'ifelse.html',c)

def elifcondition (request):
    e={'a':10,'b':20,'c ':30}
    return render(request,'elif.html',e)
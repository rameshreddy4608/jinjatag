from django.shortcuts import render

# Create your views here.
def jinja_first(request):
    d={'NAME':'ramesh'}
    return render(request,'jinja_first.html',context=d)


def jinja_second(request):
    d={'NAME':'RUPESH','age':23}
    return render(request,'jinja_second.html',context=d)
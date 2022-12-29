from django.shortcuts import render

# Create your views here.
def jinja2(request):
    d={'NAME':'RAMESHREDDY'}
    return render(request,'jinja2.html',context=d)
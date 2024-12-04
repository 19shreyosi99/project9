from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'name':"shreyosi","age": 25}
    return render(request,'jinja.html',context=d)
from django.shortcuts import render

# Create your views here.

def site(request):
    """The home page for Learning Log."""
    return render(request, 'problems/site.html')

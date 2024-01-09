from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm

# Create your views here.

def review(request):      
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")
    
    form = FeedbackForm()
    
    return render(request, "feedback/review.html", {
        "form": form
    })        

def thank_you(request):
    return render(request, "feedback/thank_you.html")
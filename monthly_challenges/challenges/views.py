from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
# from django.http import HttpResponse
from django.urls import reverse
# from django.template.loader import render_to_string

monthly_challenges = {
    "january": "january challenge",
    "february": "february challenge",
    "march": "march challenge",
    "april": "apr challenge",
    "may": "mayy challenge",
    "june": "june challenge",
    "july": "july challenge",
    "august": "aug challenge",
    "september": "sept challenge",
    "october": "oct challenge",
    "november": "nov challenge",
    "december": None,
}


# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())  # 
    
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge",args=[redirect_month] ) # builds full path from both url.py files
    return HttpResponseRedirect(redirect_path) # returns a new path

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html", {
            "text":challenge_text,
            "month_name":month.capitalize(),
        })
        # response_data = f"<h1>{challenge_text}</h1>"
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        raise Http404()
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
    

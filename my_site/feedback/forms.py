from django import forms

class FeedbackForm(forms.Form):
    user_name = forms.CharField(max_length=100)
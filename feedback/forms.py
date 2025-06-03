from django import forms
from .models import StudentFeedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = StudentFeedback
        fields =  '__all__'
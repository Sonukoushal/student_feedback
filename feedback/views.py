from django.shortcuts import render,redirect
from .forms import FeedbackForm
from .models import StudentFeedback
from django.contrib import messages

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Feedback successfully submitted!")
            return redirect('feedback_list')
    else:
        form = FeedbackForm()

        return render(request, 'feedback_form.html', {'form':form})

def feedback_list(request):
    feedbacks = StudentFeedback.objects.all()
    return render(request, 'feedback_list.html', {'feedbacks':feedbacks})



        


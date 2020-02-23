from django.shortcuts import render
from .models import FeedbackData
from .forms import FeedbackForm
from django.http.response import HttpResponse
import datetime
date1 = datetime.datetime.now()

def feedback_view(request):
    if request.method == "GET":
        fform = FeedbackForm()
        feedbacks = FeedbackData.objects.all()
        return render(request,'feedback.html',{'abcd':fform,
                                               'feedbacks':feedbacks})
    else:
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            name1 = request.POST.get('name')
            rating1 = request.POST.get('rating')
            feedback1 = request.POST.get('feedback')

            data = FeedbackData(
                name=name1,
                rating=rating1,
                feedback=feedback1,
                date=date1
            )
            data.save()
            fform = FeedbackForm()
            feedbacks = FeedbackData.objects.all()
            return render(request,'feedback.html',{'abcd':fform,
                                                   'feedbacks':feedbacks})
        else:
            return HttpResponse("User Missed Data")
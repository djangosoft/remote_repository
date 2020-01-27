from django.shortcuts import render
from Institute.forms import ContactForm,FeedbackForm
from Institute.models import ContactData,FeedbackData,ServicesData
from django.http.response import HttpResponse
import datetime as dt

def home(request):
    return render(request,'home.html')
def contact(request):
    if request.method == "POST":
        cform = ContactForm(request.POST)
        if cform.is_valid():
            name1 = request.POST.get('name')
            email1 = request.POST.get('email')
            mobile1 = request.POST.get('mobile')
            location1 = request.POST.get('location')
            data = ContactData(
                name=name1,
                email=email1,
                mobile=mobile1,
                location=location1
            )
            data.save()
            cform = ContactForm()
            return render(request, 'contact.html', {'abcd': cform})
        else:
            return HttpResponse("User Missed Some Details..")
    else:
        cform = ContactForm()
        return render(request, 'contact.html', {'abcd': cform})
def services(request):
    service = ServicesData.objects.all()
    return render(request,'services.html',{'service':service})
def gallery(request):
    return render(request,'gallery.html')
date1= dt.datetime.now()
def feedback(request):
    if request.method=="POST":
        fform = FeedbackForm(request.POST)
        print(request.POST)
        if fform.is_valid():
            name1 = request.POST.get('name')
            rating1 = request.POST.get('ratings')
            feedback1= request.POST.get('feedback')
            data = FeedbackData(
                name=name1,
                ratings=rating1,
                feedback=feedback1,
                date=date1
            )
            data.save()
            feedbacks= FeedbackData.objects.all()
            fform= FeedbackForm
            return render(request,'feedback.html',{'fform':fform,'feedbacks':feedbacks})
        else:
            return HttpResponse("User Missed Some values..")
    else:
        fform= FeedbackForm()
        feedbacks=FeedbackData.objects.all()
        return render(request,'feedback.html',{'fform':fform,'feedbacks':feedbacks})


from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question

# Create your views here.
def home(request):

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list
    }
    return render(request, 'polls/index.html', context)

    

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')

    context  = {
        'question' : question
    }
    return render(request, 'polls/details.html', context )

def results(request, question_id):
    return HttpResponse('You are looking at results of question number %s' %question_id)

def vote(request, question_id):
    return HttpResponse('You are voting on question number %s' %question_id)


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse

# Create your views here.
def home(request):

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list
    }
    return render(request, 'polls/index.html', context)

    

def detail(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)

    context  = {
        'question' : question
    }
    return render(request, 'polls/detail.html', context )


def results(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    context = {
        'question' : question
    }

    return render(request, 'polls/results.html', context)

    # return HttpResponse('You are looking at results of question number %s' %question_id)

def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

        selected_choice.votes +=1

        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

    except (KeyError, Choice.DoesNotExist):

        return render(request, 'polls/detail.html', {
                'question' : question,
                'error_message' : 'You didnt select a choice'
             }
        )

    # return HttpResponse('You are voting on question number %s' %question_id)


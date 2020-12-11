from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from employee.models import Question, Choice
from django.urls import reverse

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('employee/index.html')
    context = {
        'latest_question_list':latest_question_list
    }
    # below line is currect 
    #return HttpResponse(output) 
    # below line is currect
    #return HttpResponse(template.render(context, request))
    return render(request, 'employee/index.html', context)

def add_employee(request):
    return HttpResponse("Add employee page")

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    #return HttpResponse("your're looking at question %s."%question_id)
    return render(request, 'employee/detail.html', {'question':question})
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'employee/results.html', {'question':question})
    #response = "Your're looking at the results of question %s."
    #return HttpResponse(response%question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'employee/detail.html', {'question':question, 'error_message':"You don't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('employee:results', args =(question.id,)))
    #return HttpResponse("You're voting on question %s"%question_id)
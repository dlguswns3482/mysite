#from multiprocessing import context
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, render


from.models import Question
# Create your views here.
def index(request):
   #1
    #return HttpResponse("Hello,world. You're at the polls index.")
    #2
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)

    #3
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context={
     #   'latest_question_list': latest_question_list,
    #}
    #return HttpResponse(template.render(context, request))

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context ={'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #1
    #return HttpResponse("You're looking at question %s." % question_id)

    #2
    #try:
        #question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
        #raise Http404("Question does not exist")
    #return render(request, 'polls/detail.html', {'question: question'} )

    #3
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request,  question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)




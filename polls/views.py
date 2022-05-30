from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_questions': latest_questions,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does no exist")
    question = get_object_or_404(Question, pk=question_id)
    choices = Choice.objects.all()
    choices_by_questions = []
    for choice in choices:
        if choice.question.pk == question_id:
            choices_by_questions.append(choice)

    context = {
        'question': question,
        'choices': choices_by_questions,
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("voting on question %s" % question_id)

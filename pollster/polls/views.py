from django.shortcuts import render
from .models import Question, Choice
# Create your views here.


def index(request):
    latest_questions = Question.objects.order_by('pub_date')[:5]
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)


# show specific question and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', {'question': question})


# Get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, question_id)
    return render(request, 'polls/results.html', {'question': question})

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from polls.models import Question, Choice, EyewitnessStimuli
from django.urls import reverse
from django.views import generic


# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by('-publish_date')[:5]
#     # output = ', '.join(q.question_text for q in latest_question_list)
#     # template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list' : latest_question_list
#     }
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)
#
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
#     context = {
#         'question' : question
#     }
#     # return HttpResponse("You're looking at question %s." % question_id)
#     return render(request, 'polls/detail.html', context)
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """return last five published question"""
        return Question.objects.order_by('-publish_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# userId, choices, lineups
def sample(request):
    sample_q = get_object_or_404(EyewitnessStimuli, pk = 3)

    file_path = 'polls/lineups/'
    lineup_number = sample_q.lineup_number
    if lineup_number[0] == 'W':
        file_path += 'faces_white/' + lineup_number[1] + '/'
    else:
        file_path += 'faces_black/' + lineup_number[1] + '/'

    lineup_order = sample_q.lineup_order.split(';')
    img_set_path = []
    chosen_face = ""
    for image_num in lineup_order:
        if int(image_num) == sample_q.chosen_face:
            chosen_face = file_path + image_num + '.jpg'

        img_set_path.append(file_path + image_num + '.jpg')
    stmt = sample_q.statement
    print(chosen_face)
    print(img_set_path)

    context = {
        # 'sample' : sample_q,
        # 'image_path': file_path,
        'chosen': chosen_face,
        'lineup_order1': img_set_path[:3],
        'lineup_order2': img_set_path[3:],
        'statement': stmt,
    }
    return render(request, 'polls/sample.html', context)






































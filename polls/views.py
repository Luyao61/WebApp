import random
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from polls.models import Question, Choice, EyewitnessStimuli, Users, Response
from django.urls import reverse
from django.views import generic
import uuid


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

    context = {
        # 'sample' : sample_q,
        # 'image_path': file_path,
        'chosen': chosen_face,
        'lineup_order1': img_set_path[:3],
        'lineup_order2': img_set_path[3:],
        'statement': stmt,
    }
    return render(request, 'polls/sample.html', context)


def start(request):

    return render(request, 'polls/start.html')


def create_new_user(request):
    uid = uuid.uuid4().hex[:14].upper()
    while Users.objects.filter(pk=uid).exists():
        uid = uuid.uuid4().hex[:14].upper()

    new_user = Users(userId=uid)
    new_user.save()

    generate_question(new_user)

    context = {
        'uid': uid
    }
    return HttpResponseRedirect(reverse('polls:test', args=(uid,)))


def test(request, uid):
    #q_num = Response.objects.filter(user=)
    user = get_object_or_404(Users, pk=uid)
    q_set = user.response_set.exclude(answer__isnull=True)
    q_num = len(q_set)
    print(q_num)

    if q_num == 6:
        return render(request, 'polls/thankyou.html')
    else:
        response = Response.objects.filter(user=user)[q_num]
        sample_q = response.question

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
        chosen_face = file_path + '5.jpg'

        context = {
            # 'sample' : sample_q,
            # 'image_path': file_path,
            'chosen': chosen_face,
            'lineup_order1': img_set_path[:3],
            'lineup_order2': img_set_path[3:],
            'statement': stmt,
            'uid': uid,
        }
        return render(request, 'polls/sample.html', context)


def record_answer(request, uid, a):
    ##
    print(a)
    user = get_object_or_404(Users, pk=uid)
    q_set = user.response_set.exclude(answer__isnull=True)
    q_num = len(q_set)

    response = Response.objects.filter(user=user)[q_num]
    response.answer = a
    response.save()

    return HttpResponseRedirect(reverse('polls:test', args=(uid,)))


# helper functions
def generate_question(user):
    chosen_set = []     # track lineup_number that has been used
    score_set = [60,80,100]
    race_set = ['W', 'B']

    question_set = []

    for i in range(6):
        query_set = EyewitnessStimuli.objects.filter(score=score_set[int(i/2)], lineup_race=race_set[int(i % 2)])
        for n in chosen_set:
            query_set = query_set.exclude(lineup_number=n)
        q = random.choice(query_set)
        question_set.append(q)
        chosen_set.append(q.lineup_number)

    order = [0,1,2,3,4,5]
    random.shuffle(order)
    for n in order:
        response = Response(user=user, question=question_set[n])
        response.save()































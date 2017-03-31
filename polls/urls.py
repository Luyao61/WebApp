from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    # # ex: /polls/
    # url(r'^$', views.index, name='index'),
    # # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    # sample
    url(r'^sample/$', views.sample, name='sample'),
    url(r'^start/$', views.start, name='start'),
    url(r'^test/(?P<uid>([A-Z]|[0-9]){14})/$', views.test, name='test'),

    url(r'^record/(?P<uid>([A-Z]|[0-9]){14})/(?P<a>(60|80|100))/$', views.record_answer, name='record_answer'),
    url(r'^create_new_user/$', views.create_new_user, name='create_new_user'),

]

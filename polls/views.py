
from django.template import Context, loader
from polls.models import Poll, Choice
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from account.facebook import publish_to_facebook
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	t = loader.get_template('polls/index.html')
	c = Context({
		'latest_poll_list': latest_poll_list,
	})
	return HttpResponse(t.render(c))


def detail(request, poll_id):
	a=get_object_or_404(Poll, id=poll_id)
	return render_to_response('polls/detail.html', {'poll': a}, context_instance=RequestContext(request))

@login_required
def results(request, poll_id):
	a=get_object_or_404(Poll, id=poll_id)
	return render_to_response('polls/results.html', {'poll': a})

@login_required
def vote(request, poll_id):
	p = get_object_or_404(Poll, id=poll_id)
	try:
		selected_choice = p.choice_set.get(id=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render_to_response('polls/detail.html', {
			'poll': p,
			'error_message': u"Musisz wybrać poprawną opcję.",
			}, context_instance=RequestContext(request))
	selected_choice.votes += 1
	selected_choice.save()
	publish_to_facebook(request.user, "Zkodziłam aplikację, zhakowałam internety i facebooki! Dodane przez: Django App® (produced by: Rhone)")
	return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))


# Create your views here.

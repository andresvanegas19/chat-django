from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher
pusher = Pusher(app_id=u"1056585", key=u"60a0572a0aeaf826d6db", secret=u"869623bc82f144ccb697", cluster=u"us2")



# Create your views here.
@login_required(login_url='/admin/login/')
def chat(request):
    return render(request,"chat.html");


@csrf_exempt
def broadcast(request):
    
    pusher.trigger(u'a_channel', u'an_event', {u'name': request.user.username, u'message': request.POST['message']})
    return HttpResponse("done");

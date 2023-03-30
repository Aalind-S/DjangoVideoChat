from django.shortcuts import render, redirect
from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse
import random
import time
# Create your views here.
def lobby(request):
    return render(request, 'lobby.html')

def room(request):
    return render(request, 'room.html')

def getToken(request):
    appId = '39e9c2b1c6b64dac969a4cce082d4f37'
    appCertificate = 'a879a6e128404441a66f31ceccc2b169'
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600*24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token':token, 'uid':uid}, safe=False)
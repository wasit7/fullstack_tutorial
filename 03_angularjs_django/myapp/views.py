from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.
serverdata=[{'name':'wasit','ext':'224'},{'name':'eric','ext':'154'}]

def home(request):
	return render(request,'home.html')

def getpost(request):
	global serverdata
	#request data from server
	if request.method=='GET':
		return JsonResponse( serverdata, safe=False )
	if request.method=='POST':
		serverdata = json.loads(request.body)
		#serverdata.append(clientdata)
		return JsonResponse( serverdata, safe=False)

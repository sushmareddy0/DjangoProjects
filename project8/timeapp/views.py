from django.shortcuts import render
from datetime import datetime

# Create your views here.
def display_time(request):
	server_time=datetime.now()
	print(server_time)
	data={'time':server_time}
	return render(request=request, template_name='timeapp/time.html', context=data)

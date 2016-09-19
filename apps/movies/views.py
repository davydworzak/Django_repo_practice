from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	if request.method=="GET":
		return render(request, 'movies/index.html')
	elif request.method=="POST":
		if request.POST['add'] == 'movie':
	 		Movie.objects.create(title=request.POST['title'])
			return redirect('/')	
		elif request.POST['add'] == 'actor':
	 		Actor.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'])
			return redirect('/')
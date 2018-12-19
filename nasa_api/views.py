from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.dateparse import parse_date
from nasa_api.models import NasaComment 
import requests

# Create your views here.

# Create a comment with a rating
def nasa_comment_create(request):
	# If GET, we render a form
	if(request.method == "GET"):
		api_key = "GKmUEZXkJcOrfiYATIDo6GRYG4y9bHMWyDnCdX2c"
		# We are doing a get request
		date = request.GET.get("date")
		r = requests.get(f'https://api.nasa.gov/planetary/apod?date={date}&api_key={api_key}')
		url = r.json()["url"]
		return render(request, 'create_comment.html', {"nasa_url": url, "date": date})
	
	# If POST, we need to create and direct to detail view
	elif(request.method == "POST"):
		nasa_comment = NasaComment.objects.create(
			rating = request.POST.get("rating"),
			comment = request.POST.get("comment"),
			date = parse_date(request.POST.get("date"))
		)
		return redirect('/nasa/comment/' + str(nasa_comment.id))
	
	else:
		return HttpResponse("Error")

# Display details for a single comment
def nasa_comment(request, nasa_id):
	nasa_comment = NasaComment.objects.get(id=nasa_id)
	return render(request, 'nasa_comment.html', {"nasa_comment": nasa_comment})

# Display all comments
def nasa_comment_showall(request):
	nasa_comments = NasaComment.objects.all()
	return render(request, 'nasa_comment_showall.html', {"nasa_comments": nasa_comments})

# Get the date for NASA picture
def nasa_date_picker(request):
	if(request.method == "POST"):
		date = request.POST.get("date")
		return redirect('/nasa/comment/create/?date=' + date)
	elif(request.method == "GET"):
		return render(request, 'date_picker.html', {})
	else:
		return HttpResponse("Error")
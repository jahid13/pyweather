from django.shortcuts import render


# Create your views here.
def home(request):
    import json
    import requests
    api_request = requests.get("http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=94102&date=2020-07-23&distance=25&API_KEY=445AE684-7031-4F15-96D7-F237990B9E38")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "error..."

    if api[0]['Category']['Name'] == "Good":

        category_description = "(0 to 50)Air quality is satisfactory, and air pollution poses little or no risk."

    return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})

from django.shortcuts import render


# Create your views here.
def home(request):
    import json
    import requests
    if request.method == "POST":
        zipcode = request.POST['zipcode']

        api_request = requests.get("http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=" + zipcode + "&date=2020-07-23&distance=25&API_KEY=445AE684-7031-4F15-96D7-F237990B9E38")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "error..."

        if api[0]['Category']['Name'] == "Good":
            category_color = "good"
            category_description = "(0 to 50)Air quality is satisfactory, and air pollution poses little or no risk."

        elif api[0]['Category']['Name'] == "Moderate":
            category_color = "moderate"
            category_description = "51 to 100 Air quality is acceptable.However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
        elif api[0]['Category']['Name'] == "USG":
            category_color = "usg"
            category_description = "101 to 150 Members of sensitive groups may experience health effects.The general public is less likely to be affected."
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_color = "unhealthy"
            category_description = "151 to 200 Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_color = "veryunhealthy"
            category_description = "201 to 300 Health alert: The risk of health effects is increased for everyone."

        return render(request, 'home.html', {'api': api,
                                             'category_description': category_description,
                                             'category_color': category_color})
    else:
        api_request = requests.get("http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=94102&date=2020-07-23&distance=25&API_KEY=445AE684-7031-4F15-96D7-F237990B9E38")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "error..."

        if api[0]['Category']['Name'] == "Good":
            category_color = "good"
            category_description = "(0 to 50)Air quality is satisfactory, and air pollution poses little or no risk."

        elif api[0]['Category']['Name'] == "Moderate":
            category_color = "moderate"
            category_description = "51 to 100 Air quality is acceptable.However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
        elif api[0]['Category']['Name'] == "USG":
            category_color = "usg"
            category_description = "101 to 150 Members of sensitive groups may experience health effects.The general public is less likely to be affected."
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_color = "unhealthy"
            category_description = "151 to 200 Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_color = "veryunhealthy"
            category_description = "201 to 300 Health alert: The risk of health effects is increased for everyone."

        return render(request, 'home.html', {'api': api,
                                             'category_description': category_description,
                                             'category_color': category_color})


def about(request):
    return render(request, 'about.html', {})

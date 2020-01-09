from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Plan, Continents, Countries, Cities
from . serializers import ContinentSerializer, CountriesSerializer, CitiesSerializer, PlanSerializer


@api_view(['GET'])
def add_data(request):

    # continent_name = "Africa"
    # countries_cities = [
    #     {
    #         "country_name": "Algeria",
    #         "cities": ["Algiers"	"Dzayer", "Oran Wehran", "Constantine Qsenṭina", "Annaba Ɛennaba", "Batna Batna", "Blida Blida", "Sétif Sṭif", "Chlef Clef", "Djelfa Ǧelfa","Sidi Bel Abbes"]
    #     },
    #     {
    #         "country_name": "Benin",
    #         "cities": ["Cotonou	Benin", "Abomey-Calavi", "Djougou Benin", "Porto-Novo","Parakou"]
    #     },
    #     {
    #         "country_name": "Nigeria",
    #         "cities": ["Abia State Umuahia", "Adamawa Yola", "Akwa Ibom Uyo", "Anambra Awka", "Bauchi Bauchi", "Bayelsa Yenagoa", "Benue Makurdi", "Borno Maiduguri"]
    #     },
    #     {
    #         "country_name": "Africa",
    #         "cities": ["Abia State Umuahia", "Adamawa Yola", "Akwa Ibom Uyo", "Anambra Awka", "Bauchi Bauchi",
    #                    "Bayelsa Yenagoa", "Benue Makurdi", "Borno Maiduguri"]
    #     },
    #
    # ]
    # continent_name = "ASIA"
    # countries_cities = [
    #     {
    #         "country_name": "India",
    #         "cities": ["Andhra Pradesh", "Haryana", "Punjab", "Himachal Pradesh", "Chandigarh", "Delhi",
    #                    "Mumbai", "Hyderabad", "Mohali", "Agra", "Banglore", "Noida"]
    #     },
    #     {
    #         "country_name": "Indonesia",
    #         "cities": ["Aceh ", "Bali", "Bangka Belitung", "Banten", "Bengkulu"]
    #     },
    #     {
    #         "country_name": "Iran",
    #         "cities": ["Alborz", "Ardabil", "Azerbaijan, East", "Azerbaijan, West", "Bushehr",
    #                    "Fars", "Gilan", "Golestan"]
    #     },
    #     {
    #         "country_name": "Israel",
    #         "cities": ["Afula", "Akko", "Dimona", "Dor", "Herzliyya",
    #                    "Jerusalem", "Nazareth", "Ramat Gan"]
    #     },
    #
    # ]

    # continent_name = "Europe"
    # countries_cities = [
    #     {
    #         "country_name": "Germany",
    #         "cities": [" Baden-Württemberg", " Bavaria", " Berlin", " Brandenburg", "Bremen", " Hamburg",
    #                    " Hesse", "Saarland", "Saxony", "Saxony-Anhalt", "Thuringia"]
    #     },
    #     {
    #         "country_name": "Iceland",
    #         "cities": ["Reykjavik ", "South Iceland", "Westman Islands", "West Iceland", "East Iceland", "Westfjords",
    #                    "North Iceland"]
    #     },
    #     {
    #         "country_name": "Italy",
    #         "cities": ["Agrigento", "Alessandria", "Belluno", "Bergamo", "Como", "	Enna",
    #                    "Fermo", "Genoa", "	Imperia"]
    #     },
    #     {
    #         "country_name": "Switzerland",
    #         "cities": ["Zürich", "Geneva", "Basel", "Lausanne", "Bern",
    #                    "Lucerne", "Lugano", "St Gallen"]
    #     },
    #
    # ]

    # continent_name = "North AMERICA"
    # countries_cities = [
    #     {
    #         "country_name": "North AMERICA",
    #         "cities": [" Aguascalientes", " Baja California Norte", " Baja California Sur", "Chiapas", "Mexico City", "Guerrero",
    #                    "Jalisco", "Sinaloa", "Veracruz", "Zacatecas"]
    #     },
    #     {
    #         "country_name": "United States",
    #         "cities": ["Alabama ", "Alaska", "Arizona", "California", "Florida	", "New York",
    #                    " New Jersey"]
    #     },
    #     ]

    # continent_name = "Oceania"
    # countries_cities = [
    #     {
    #         "country_name": "Australia",
    #         "cities": [" Australian Capital Territory", " New South Wales", "Northern Territory", "Queensland", "South Australia", "Tasmania    ",
    #                    "Victoria"]
    #     },
    #     {
    #         "country_name": "New Zealand",
    #         "cities": ["Northland ", "Auckland", "Waikato", "	Bay of Plenty", "Taranaki", "Wellington",
    #                    ]
    #     },
    #
    # ]

    continent_name = "South America"
    countries_cities = [
        {
            "country_name": "Brazil",
            "cities": [" Minas Gerais", "Rio de Janeiro", "Bahia", "Rio Grande do Sul"]
        },
        {
            "country_name": "New Zealand",
            "cities": ["Northland ", "Auckland", "Waikato", "	Bay of Plenty", "Taranaki", "Wellington",
                       ]
        },
        {
            "country_name": "Italy",
            "cities": ["Agrigento", "Alessandria", "Belluno", "Bergamo", "Como", "	Enna",
                       "Fermo", "Genoa", "	Imperia"]
        },
        {
            "country_name": "Switzerland",
            "cities": ["Zürich", "Geneva", "Basel", "Lausanne", "Bern",
                       "Lucerne", "Lugano", "St Gallen"]
        },
    ]

    created_continent = Continents.objects.create(name=continent_name)
    for country in range(len(countries_cities)):
        created_country = Countries.objects.create(name=countries_cities[country]["country_name"],
                                                   continent=created_continent)
        for city in countries_cities[country]["cities"]:
            Cities.objects.create(name=city, country=created_country)
    return Response({"status":True})



# @api_view(['GET'])
# def add_countries(request):
#     countries_list =["Africa","Europe","Asia","North America","Oceania","South America","Antarctica"]
#     for continent in continents_list:
#         data = {"name":continent}
#         serializer = ContinentSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response({"status":True, "msg":"Continents Added"})


@api_view(['POST'])
def add_plan(request):
    print(request.data)
    serializer = PlanSerializer(data=request.data)
    # print(request.data*100)
    if serializer.is_valid():
        serializer.save()
        return Response({"status":True, "data":serializer.data})
    return Response({"status": False, "msg": "Error "})

@api_view(['GET'])
def get_plan(request, pk):
    print(request.data)
    plan = Plan.objects.get(id=pk)
    serializer = PlanSerializer(plan)
    return Response({"status":True, "data":serializer.data})

continent_name = "Africa"
countries_cities = [
    {
        "country_name": "Algeria",
        "cities": ["Algiers"    "Dzayer", "Oran Wehran", "Constantine Qsenṭina", "Annaba Ɛennaba", "Batna Batna",
                   "Blida Blida", "Sétif Sṭif", "Chlef Clef", "Djelfa Ǧelfa", "Sidi Bel Abbes"]
    },
    {
        "country_name": "Benin",
        "cities": ["Cotonou	Benin", "Abomey-Calavi", "Djougou Benin", "Porto-Novo", "Parakou"]
    },
    {
        "country_name": "Nigeria",
        "cities": ["Abia State Umuahia", "Adamawa Yola", "Akwa Ibom Uyo", "Anambra Awka", "Bauchi Bauchi",
                   "Bayelsa Yenagoa", "Benue Makurdi", "Borno Maiduguri"]
    },
    {
        "country_name": "Africa",
        "cities": ["Abia State Umuahia", "Adamawa Yola", "Akwa Ibom Uyo", "Anambra Awka", "Bauchi Bauchi",
                   "Bayelsa Yenagoa", "Benue Makurdi", "Borno Maiduguri"]
    },

]
for country in range(len(countries_cities)):
    print(countries_cities[country]["country_name"])
    # country_data = {"name": countries_cities[country]["country_name"], continent: created_continent}
    #     for city in countries_cities[country]["cities"]:

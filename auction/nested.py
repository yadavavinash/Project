
travel_log = [
	{
	"county":"France",
	"city_visited": ["paris", "lille", "Dijon"],
	"total_Visit": 12
	},
	{
	"country":"Germany",
	"city_visited": ["berlin", "hamburg", "stutggart"],
	"total_visit": 12
	},
	]

def new_country(visited_country,visited_city, no_of_times_visites ):

	county_visited= {}
	county_visited["county"] = county_visited
	county_visited["city_visited"] = visited_city
	county_visited["total_visit"] = no_of_times_visites
	travel_log.append(county_visited)

new_country("Russia",["moscou, saint petersburg"],12)
print(travel_log)
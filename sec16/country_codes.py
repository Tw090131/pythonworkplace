from pygal.i18n import COUNTRIES
def get_country_code(country_name):
	"""根据国家返回国别码"""
	for code,name in COUNTRIES.items():
		if name == country_name:
			return code

	return None

# print(get_country_code("Andorra"))
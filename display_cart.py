def display_schedule(cartoons):
	if len(cartoons) == 0:
		return 'На сегодня ничего нет :('

	result = ''
	for cartoon in cartoons:
		output = '{0} <a href="{1}">{2}</a> ({3}) \n {4} \n\n'.format(cartoon['c_time'], cartoon['c_url'],
														cartoon['c_title'], cartoon['c_age'],cartoon['c_place'])
		result += output

	return result
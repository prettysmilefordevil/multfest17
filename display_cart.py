def display_schedule(cartoons):
	if len(cartoons) == 0:
		return 'На сегодня ничего нет :('

	result = ''
	for cartoon in cartoons:
		if cartoon['c_time'].minute==0:
			output = '{0}:0{1} <a href="{2}">{3}</a> ({4}) \n {5} \n\n'.format(cartoon['c_time'].hour,cartoon['c_time'].minute, cartoon['c_url'],
														cartoon['c_name'], cartoon['c_age'],cartoon['c_place'])
		else:
			output = '{0}:{1} <a href="{2}">{3}</a> ({4}) \n {5} \n\n'.format(cartoon['c_time'].hour,cartoon['c_time'].minute, cartoon['c_url'],
														cartoon['c_name'], cartoon['c_age'],cartoon['c_place'])
		result += output

	return result
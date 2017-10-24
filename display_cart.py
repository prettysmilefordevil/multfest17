import datetime
def display_schedule(cartoons):
	if len(cartoons) == 0:
		return 'На сегодня ничего нет :('

	result = ''
	today = datetime.datetime.now()
	if today.month==10:
		mon='октября'
	else:
		mon='ноября'
	for cartoon in cartoons:
		if cartoon['c_time'].minute==0:
			output ='{0}:0{1}  {2} ({3}) \n {4} \n'.format(cartoon['c_time'].hour,cartoon['c_time'].minute,
														cartoon['c_name'], cartoon['c_age'],cartoon['c_place'])
			if not cartoon['c_url']=='':
				output=output+'('+cartoon['c_url']+')'

		else:
			output = '{0}:{1} {2} ({3}) \n {4} \n'.format(cartoon['c_time'].hour,cartoon['c_time'].minute,
														cartoon['c_name'], cartoon['c_age'],cartoon['c_place'])
			if not cartoon['c_url']=='':
				output=output+'('+cartoon['c_url']+')'
		result += output
	result = today.strftime("%d")+' '+mon+'\n'+result

	return result
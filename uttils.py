from datetime import datetime , timedelta

#  This Function deleting microseconds of a TimeValue
def remove_microsecond(arg):
	date_string = str(arg)
	date_string = date_string[:7]
	final_date 	= datetime.strptime(date_string , '%H:%M:%S')
	delta 		= timedelta(hours=final_date.hour , minutes=final_date.minute , seconds=final_date.second)
	return delta

#  Removing extra strings from subtitles
def pulishing(string):
	if '</c.mono_sans></c.white>' in string:	
		data = string.removesuffix('</c.mono_sans></c.white>')
		data = data.removeprefix('<c.white><c.mono_sans>')
	else:
		data = string.removesuffix('</c.bg_transparent>')
		data = data.removeprefix('<c.bg_transparent>')
	return data

#  This list Will be Used for CSV Rows
def final_list_creator(list):
	final_list = []
	for i in list:
		time = str(i.start)
		final_list.append([time , pulishing(i.content)])
	return final_list

# 
def listing(arg):
	listed = []
	for i in arg:
		listed.append([f"{i.start} \n {i.content}\n"])
	return listed
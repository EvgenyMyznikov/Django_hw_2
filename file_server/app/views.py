import os
from datetime import datetime
from django.conf import settings
from django.shortcuts import render

FILES = os.listdir(settings.FILES_PATH)


# Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
# context = {
# 	'files': [
# 		{'name': 'file_name_1.txt',
# 		 'ctime': datetime(2018, 1, 1),
# 		 'mtime': datetime(2018, 1, 2)}
# 	],
def file_list(request, date=None):
	template_name = 'index.html'
	srv_list = []
	for file in FILES:
		stat = os.stat(os.path.join(settings.FILES_PATH, file))
		file_ctime = datetime.fromtimestamp(stat.st_ctime)
		file_mtime = datetime.fromtimestamp(stat.st_mtime)
		srv_list.append({
			'name': file,
			'ctime': file_ctime,
			'mtime': file_mtime
		})
	# if date:
	# 	srv_list = list(filter(lambda x: x['created_at'] == date, srv_list))
		if date and not (date == file_ctime.date() or date == file_mtime.date()):
			continue
	return render(
		request,
		template_name,
		context={'files': srv_list, 'date': date})


# Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
def file_content(request, name):
	template_name = 'file_content.html'
	file = os.path.join(settings.FILES_PATH, name)
	with open(file, 'r', encoding='utf-8') as f:
		content = f.read()
	return render(
		request,
		template_name,
		context={'file_name': name, 'file_content': content}
	)
# 	return render(
# 		request,
# 		template_name,
# 		context={'file_name': 'file_name_1.txt', 'file_content': 'File content!'}
# 	)

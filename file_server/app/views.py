import os
from datetime import datetime
from django.conf import settings
from django.shortcuts import render
from django.urls import register_converter

FILES = os.listdir(settings.FILES_PATH)


class DateConverter:
	regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
	format = '%Y-%m-%d'

	def to_python(self, value):
		return datetime.strptime(value, self.format)

	def to_url(self, value):
		return value.strftime(self.format)


register_converter(DateConverter, 'date')


# Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
# context = {
# 	'files': [
# 		{'name': 'file_name_1.txt',
# 		 'ctime': datetime(2018, 1, 1),
# 		 'mtime': datetime(2018, 1, 2)}
# 	],
def file_list(request, dt=None):
	template_name = 'index.html'
	srv_list = []
	for file in FILES:
		srv_list.append(file)
		if dt:
			srv_list = list(filter(lambda x: x['created_at'] == dt, srv_list))
	return render(
		request,
		template_name,
		context={'files': srv_list}
	)


# Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
def file_content(request, name):
	template_name = 'file_content.html'
	for file in FILES:
		name = os.path.basename(file)
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

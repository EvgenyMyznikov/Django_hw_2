from django.urls import path

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
from file_server.app.views import file_list, file_content

urlpatterns = [
	# Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
	# path(..., name='file_list'),
	# path(..., name='file_list'),    # задайте необязательный параметр "date"
	# для детальной информации смотрите HTML-шаблоны в директории templates
	# path(..., name='file_content'),
	path('file_list/', file_list, name='file_list'),
	path('file_list/<date:dt>/', file_list, name='file_list'),
	path('file_content/<str:name>', file_content, name='file_content'),
]
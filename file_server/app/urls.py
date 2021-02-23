from django.urls import path
# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
from file_server.app.converters import DateConverter
from file_server.app.views import file_list, file_content
from django.urls import register_converter

register_converter(DateConverter, 'dt')

urlpatterns = [
	path('', file_list, name='file_list'),
	path('files/<dt:date>/', file_list, name='file_list'),
	path('files/<str:name>/', file_content, name='file_content'),
]
# Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
# path(..., name='file_list'),
# path(..., name='file_list'),    # задайте необязательный параметр "date"
# для детальной информации смотрите HTML-шаблоны в директории templates
# path(..., name='file_content'),

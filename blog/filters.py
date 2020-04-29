import django_filters

from . models import Enotes

class EnotesFilter(django_filters.FilterSet):

	topic = django_filters.CharFilter(lookup_expr='icontains',label='topic' )
	# author = django_filters.CharFilter(lookup_expr='icontains',label='posted by', field_name='author')
	author_name = django_filters.CharFilter(lookup_expr='icontains',label='created by')
	desc = django_filters.CharFilter(lookup_expr='icontains',label='Desc')
 
	class Meta:
		model = Enotes
		fields = (
			#4
			'topic',
			'unit',
			'notes_author',
		 	'author_name',
		 	#2
			'academic_year',
			'sub',
			'branch',
			#1
			'desc',
			'author'	
		)















import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class TransactionFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date", lookup_expr='gte')
	end_date = DateFilter(field_name="date", lookup_expr='lte')
	name = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = Transaction
		fields = '__all__'
		exclude = ['customer', 'date_created']
import django_filters
from django_filters import DateFilter,CharFilter

from .models import Order

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created',lookup_expr='gte')
    end_date = DateFilter(field_name='date_created',lookup_expr='lte')
    note = CharFilter(field_name = 'note',lookup_err='icontainer')

    class Meta:
        model = Order 
        fields = '__all__'
        exclude = ['customer','date_created']
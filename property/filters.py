import django_filters
from . models import Room

class PropertyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Room
        fields = ['name', 'description', 'location', 'category']
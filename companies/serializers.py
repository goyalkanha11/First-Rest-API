from rest_framework import serializer
from .models import Stock

class StockSerializer(serializers.ModelSerializer):

	class Meta:
		model = Stock
		fields = '__all__'
	
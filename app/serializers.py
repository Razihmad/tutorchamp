from rest_framework import serializers
from app.models import LabOrders,Orders
class LabSerializers(serializers.ModelSerializer):
    class Meta:
        model = LabOrders
        fields = '__all__'
        
class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields = '__all__'
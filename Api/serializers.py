from rest_framework import serializers
from Api.models import CompanyModel,EmployeeModel

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model=CompanyModel
        fields="__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=EmployeeModel
        fields="__all__"
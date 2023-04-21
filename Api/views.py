from django.shortcuts import render
from Api.models import CompanyModel,EmployeeModel
from Api.serializers import EmployeeSerializer,CompanySerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class CompanyviewSet(viewsets.ModelViewSet):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer

            #detail true is for must provide Primary Key
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            company = CompanyModel.objects.get(pk=pk)
            emps=EmployeeModel.objects.filter(company=company)
            #now creating the obbjext of serializer for serialize the data means format the data in Json Form
            emps_serializer = EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'Message' : 'Company might not exist'
            })
class EmployeeviewSet(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

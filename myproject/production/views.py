from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ProductionReport, Employee, Machine, Shift, HourlyProduction, ScrapAnalysis, InjectionMolding
from .serializers import (
    ProductionReportSerializer, EmployeeSerializer, MachineSerializer, ShiftSerializer, 
    HourlyProductionSerializer, ScrapAnalysisSerializer, InjectionMoldingSerializer
)

class ProductionReportViewSet(viewsets.ModelViewSet):
    queryset = ProductionReport.objects.all()
    serializer_class = ProductionReportSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

class HourlyProductionViewSet(viewsets.ModelViewSet):
    queryset = HourlyProduction.objects.all()
    serializer_class = HourlyProductionSerializer

class ScrapAnalysisViewSet(viewsets.ModelViewSet):
    queryset = ScrapAnalysis.objects.all()
    serializer_class = ScrapAnalysisSerializer

class InjectionMoldingViewSet(viewsets.ModelViewSet):
    queryset = InjectionMolding.objects.all()
    serializer_class = InjectionMoldingSerializer


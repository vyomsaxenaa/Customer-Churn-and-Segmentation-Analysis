from rest_framework import serializers
from .models import ProductionReport, Employee, Machine, Shift, HourlyProduction, ScrapAnalysis, InjectionMolding

class ProductionReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionReport
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        
class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'

class HourlyProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HourlyProduction
        fields = '__all__'

class ScrapAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapAnalysis
        fields = '__all__'

class InjectionMoldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InjectionMolding
        fields = '__all__'

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from production.views import (
    ProductionReportViewSet, EmployeeViewSet, MachineViewSet, ShiftViewSet,
    HourlyProductionViewSet, ScrapAnalysisViewSet, InjectionMoldingViewSet
)

router = DefaultRouter()
router.register(r'production-reports', ProductionReportViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'machines', MachineViewSet)
router.register(r'shifts', ShiftViewSet)
router.register(r'hourly-productions', HourlyProductionViewSet)
router.register(r'scrap-analyses', ScrapAnalysisViewSet)
router.register(r'injection-moldings', InjectionMoldingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

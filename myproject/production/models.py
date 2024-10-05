from django.db import models

class Employee(models.Model):
    EmpID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    PhoneNo = models.CharField(max_length=15)

class Machine(models.Model):
    MachineName = models.CharField(max_length=100, primary_key=True)
    Location = models.CharField(max_length=100)

class Shift(models.Model):
    ShiftName = models.CharField(max_length=50, primary_key=True)
    StartTime = models.TimeField()
    EndTime = models.TimeField()

# Production Report Table Model
class ProductionReport(models.Model):
    ReportID = models.AutoField(primary_key=True)
    ShiftName = models.ForeignKey(Shift, on_delete=models.CASCADE)
    MachineName = models.ForeignKey(Machine, on_delete=models.CASCADE)
    Date = models.DateField()
    Operator = models.ForeignKey(Employee, on_delete=models.CASCADE)
    PartName_1 = models.CharField(max_length=100)
    MaterialName_1 = models.CharField(max_length=100)
    MaterialGrade_1 = models.CharField(max_length=100)
    RM_LotNo_1 = models.CharField(max_length=100)
    Std_CT_1 = models.IntegerField()
    Act_CT_1 = models.IntegerField()
    Std_Wt_1 = models.IntegerField()
    PartName_2 = models.CharField(max_length=100, null=True, blank=True)
    MaterialName_2 = models.CharField(max_length=100, null=True, blank=True)
    MaterialGrade_2 = models.CharField(max_length=100, null=True, blank=True)
    RM_LotNo_2 = models.CharField(max_length=100, null=True, blank=True)
    Std_CT_2 = models.IntegerField(null=True, blank=True)
    Act_CT_2 = models.IntegerField(null=True, blank=True)
    Std_Wt_2 = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f"Report {self.ReportID} - {self.Date}"

# Similarly, define the other models like HourlyProduction, ScrapAnalysis, InjectionMolding, etc.


class HourlyProduction(models.Model):
    production = models.ForeignKey(ProductionReport, on_delete=models.CASCADE)  # Update the field name here
    time_slot = models.CharField(max_length=20)
    count = models.IntegerField()
    total = models.IntegerField()
    ok = models.IntegerField()
    rejection = models.IntegerField()
    remarks = models.CharField(max_length=200, blank=True)
    downtime = models.FloatField(null=True, blank=True)
    dt_remarks = models.CharField(max_length=200, blank=True)


# Scrap Analysis Table Model
class ScrapAnalysis(models.Model):
    production = models.ForeignKey(ProductionReport, on_delete=models.CASCADE)  # Renaming ReportID to production
    rejection_quantity = models.IntegerField()  # Changed field name to snake_case for consistency
    runner_weight = models.IntegerField()
    lumps = models.IntegerField()

# Injection Molding Table Model
class InjectionMolding(models.Model):
    production = models.ForeignKey(ProductionReport, on_delete=models.CASCADE)  # Renaming ReportID to production
    actual_weight = models.IntegerField()  # Changed field name to snake_case for consistency
    standard_count = models.IntegerField()
    start_count = models.IntegerField()
    end_count = models.IntegerField()

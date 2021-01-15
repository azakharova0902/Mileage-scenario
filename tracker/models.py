from django.db import models

# Create your models here.

class Cars(models.Model):
    unit = models.CharField(max_length=20, primary_key=True)
    # mileage = models.ForeignKey('tracker.Logs', on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=50)
    status = models.CharField(max_length=50)


# STILL NEED TO FIX SELECTION SO IT UPDATES EACH CORRESPONDING ID ONLY!!!!!!!!!!


    @property
    def mileage(self):
        q = Logs.objects.order_by("-id")[0].new_mileage
        return q

    class Meta:
        db_table = "mileage_data"
        get_latest_by = 'new_mileage'



 
class Logs(models.Model):
    unit = models.ForeignKey(Cars, on_delete=models.CASCADE)
    log_date = models.DateField()
    new_mileage = models.IntegerField()
    class Meta:
        db_table = "data_logs"
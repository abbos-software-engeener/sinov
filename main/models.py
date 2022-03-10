from django.db import models


class WorkerTime(models.Model):
    user = models.ForeignKey('client.User', on_delete=models.SET_NULL, blank=True, null=True)
    work_time = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return f'{self.user.id} -- {self.date}'
from django.db import models


class Store(models.Model):
    class Meta:
        db_table = 'ae_test'
    test_id = models.BigAutoField(primary_key=True)
    test_1 = models.CharField(max_length=255, null=True, blank=True)
    test_2 = models.CharField(max_length=255, null=True, blank=True)

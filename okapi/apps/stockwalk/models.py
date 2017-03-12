from django.db import models


class Symbol(models.Model):

    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=500)
    sector = models.CharField(max_length=1000)

    class Meta:
        db_table = 'stockwalk_companies'


class Quote(models.Model):
    date = models.DateField()
    open = models.FloatField()
    low = models.FloatField()
    high = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()
    symbol = models.ForeignKey(Symbol, on_delete=models.CASCADE)
    volume = models.IntegerField()

    class Meta:
        db_table = 'stockwalk_quotes'

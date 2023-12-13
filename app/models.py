from django.db import models
from django.db.models import SET_NULL
from django_jalali.db import models as jmodels


class Method(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'Method'

    def __str__(self):
        return self.name or ''


class WebSite(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    css_color = models.TextField(blank=True, null=True)
    css_price_net = models.TextField(blank=True, null=True)
    css_price_gross = models.TextField(blank=True, null=True)
    method = models.ForeignKey(Method, blank=True, null=True, on_delete=SET_NULL, )
    address = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'WebSite'

    def __str__(self):
        return self.name or ''


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    publish = models.BooleanField(default=True, )

    class Meta:
        db_table = 'Product'

    def __str__(self):
        return self.name or ''


class SpiderProduct(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=SET_NULL)
    site = models.ForeignKey(WebSite, blank=True, null=True, on_delete=SET_NULL)
    link = models.TextField(blank=True, null=True)
    duration = models.PositiveIntegerField(blank=True, null=True)

    publish = models.BooleanField(default=True, )

    class Meta:
        db_table = 'SpiderProduct'

    def __str__(self):
        return self.product.name or ''


class Extract(models.Model):
    spider = models.ForeignKey(SpiderProduct, blank=True, null=True, on_delete=SET_NULL)

    date = jmodels.jDateField()
    datetime = jmodels.jDateTimeField()

    price_net = models.PositiveIntegerField(blank=True, null=True)
    price_gross = models.PositiveIntegerField(blank=True, null=True)

    variant = models.CharField(max_length=100, blank=True, null=True)

    msg = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    percent_change = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'Extract'

    def __str__(self):
        return self.spider.product.name or ''

    def save(self, *args, **kwargs):
        # Calculate percent change only if there's a previous record for the same prompt
        previous_record = Extract.objects.filter(spider=self.spider).order_by('-datetime').exclude(id=self.id).first()

        if previous_record and previous_record.price_net:
            percent_change = ((self.price_net - previous_record.price_net) / previous_record.price_net) * 100
            self.percent_change = round(percent_change, 3)
        else:
            # If there's no previous record or price, set percent_change to None
            self.percent_change = None

        super().save(*args, **kwargs)

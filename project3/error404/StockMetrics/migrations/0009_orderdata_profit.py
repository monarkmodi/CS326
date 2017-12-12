# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StockMetrics', '0008_orderdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdata',
            name='profit',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]

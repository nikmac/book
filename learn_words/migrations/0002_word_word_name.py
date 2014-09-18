# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn_words', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='word_name',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]

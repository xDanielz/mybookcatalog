# Generated by Django 4.0.1 on 2022-02-16 14:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_readingmaterial_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readingmaterial',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='mybookcatalog\\catalog\\static\\catalog\\images'),
        ),
        migrations.AlterField(
            model_name='readingmaterial',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 16, 14, 56, 25, 462102, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='readingmaterial',
            name='year_of_publication',
            field=models.DateField(default=datetime.datetime(2022, 2, 16, 14, 56, 25, 462102, tzinfo=utc), verbose_name='year of publication'),
        ),
    ]

# Generated by Django 2.0.8 on 2019-04-08 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20190313_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='numberofpersons',
            name='value_2',
            field=models.IntegerField(blank=True, default=0, help_text='A number of persons as outpatient', verbose_name='Value 2'),
        ),
        migrations.AlterField(
            model_name='numberofpersons',
            name='value',
            field=models.IntegerField(blank=True, default=0, help_text='A total number of persons / A number of persons as stationary', verbose_name='Value'),
        ),
    ]

# Generated by Django 2.2.5 on 2023-06-04 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_defaultsettings_cook_initials'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultsettings',
            name='storekeeper_post',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Storekeeper post'),
        ),
    ]

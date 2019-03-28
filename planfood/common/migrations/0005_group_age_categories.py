# Generated by Django 2.0.8 on 2019-03-28 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_productcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='age_categories',
            field=models.ManyToManyField(blank=True, related_name='groups', to='common.AgeCategory', verbose_name='Age Categories'),
        ),
    ]

# Generated by Django 3.2.7 on 2021-10-14 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_dailyfreetime_busytime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyfreetime',
            name='busytime',
            field=models.FloatField(null=True),
        ),
    ]

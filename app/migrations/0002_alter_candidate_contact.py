# Generated by Django 3.2.9 on 2021-12-19 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='contact',
            field=models.CharField(max_length=10),
        ),
    ]

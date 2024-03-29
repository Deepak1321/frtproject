# Generated by Django 3.2.9 on 2022-11-13 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20221110_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='country',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='exprience',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='highestedu',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='job_type',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='jobcategory',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='jobdescription',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='max_salary',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='min_salary',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='shift',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='website',
            field=models.CharField(default='', max_length=150),
        ),
    ]

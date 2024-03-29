# Generated by Django 3.2.9 on 2022-11-10 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_delete_candidate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('dob', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('min_salary', models.BigIntegerField()),
                ('max_salary', models.BigIntegerField()),
                ('job_type', models.CharField(max_length=150)),
                ('jobcategory', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('highestedu', models.CharField(max_length=150)),
                ('exprience', models.CharField(max_length=150)),
                ('website', models.CharField(max_length=150)),
                ('shift', models.CharField(max_length=150)),
                ('jobdescription', models.CharField(max_length=500)),
                ('profile_pic', models.ImageField(upload_to='app/img/candidate')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usermaster')),
            ],
        ),
    ]

# Generated by Django 5.1 on 2024-10-18 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_addpatient'),
    ]

    operations = [
        migrations.CreateModel(
            name='addPatients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('age', models.BigIntegerField()),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=150)),
                ('last_visit', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='addPatient',
        ),
    ]

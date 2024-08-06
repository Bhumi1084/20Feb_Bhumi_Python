# Generated by Django 5.0.7 on 2024-08-03 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_notices'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amountsendernm', models.CharField(max_length=20)),
                ('amountreceivernm', models.CharField(max_length=20)),
                ('amount', models.BigIntegerField()),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]

# Generated by Django 3.0.2 on 2020-01-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.IntegerField(default=0)),
                ('feature', models.CharField(max_length=30)),
                ('usage_status', models.CharField(max_length=25)),
                ('kms_driven', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]

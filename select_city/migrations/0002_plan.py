# Generated by Django 3.0.2 on 2020-01-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('select_city', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('repeat', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]

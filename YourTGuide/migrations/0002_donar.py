# Generated by Django 3.0.8 on 2020-09-03 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YourTGuide', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='donar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('mobile', models.CharField(max_length=64)),
                ('distr', models.CharField(max_length=64)),
                ('group', models.CharField(max_length=64)),
                ('diag', models.CharField(max_length=64)),
            ],
        ),
    ]
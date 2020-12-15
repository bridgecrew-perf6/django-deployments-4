# Generated by Django 2.2.5 on 2020-10-25 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addcountrycode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100, null=True)),
                ('country_code', models.IntegerField(null=True)),
                ('country_flag', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Listofcountrycode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100, null=True)),
                ('country_code', models.IntegerField(null=True)),
                ('country_flag', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]

# Generated by Django 2.2.5 on 2020-11-04 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20201104_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Totalpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('Page_name', models.CharField(max_length=100, null=True)),
                ('Page_url', models.CharField(max_length=100, null=True)),
                ('Page_error', models.CharField(max_length=100, null=True)),
                ('Total_page', models.IntegerField(null=True)),
                ('Page_maintained_by', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trendingpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('Page_name', models.CharField(max_length=100, null=True)),
                ('Page_url', models.CharField(max_length=100, null=True)),
                ('Page_error', models.CharField(max_length=100, null=True)),
                ('Totay_page', models.IntegerField(null=True)),
                ('Page_maintained_by', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]

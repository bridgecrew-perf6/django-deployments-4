# Generated by Django 2.2.5 on 2020-11-11 15:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Health_check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('Tiltle', models.CharField(max_length=100, null=True)),
                ('Sub_title', models.CharField(max_length=100, null=True)),
                ('Test_count', models.IntegerField(null=True)),
                ('Consultant', models.CharField(max_length=100, null=True)),
                ('Packages', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('discount', models.IntegerField(null=True)),
                ('work_days', models.CharField(max_length=100, null=True)),
                ('work_hours', models.CharField(max_length=100, null=True)),
                ('landline_no', models.IntegerField(null=True)),
                ('total_price', models.IntegerField(null=True)),
            ],
        ),
    ]

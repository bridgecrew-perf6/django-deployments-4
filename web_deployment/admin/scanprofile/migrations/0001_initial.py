# Generated by Django 2.2.5 on 2020-10-30 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scanentry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('scan_center_name', models.CharField(max_length=100, null=True)),
                ('business_start', models.CharField(max_length=100, null=True)),
                ('no_of_employee', models.IntegerField(null=True)),
                ('work_days', models.IntegerField(null=True)),
                ('mobile_no', models.IntegerField(null=True)),
                ('landline_no', models.IntegerField(null=True)),
                ('lab_email', models.CharField(max_length=100, null=True)),
                ('lab_url', models.CharField(max_length=100, null=True)),
                ('lab_logo', models.ImageField(blank=True, upload_to='images/')),
                ('lab_image', models.ImageField(blank=True, upload_to='images/')),
                ('service_provider', models.CharField(max_length=100, null=True)),
                ('street_name', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('pincode', models.IntegerField(null=True)),
                ('scan_name', models.CharField(choices=[('Xray', 'Xray'), ('Ultra Sound', 'Ultra Sound'), ('CT', 'CT'), ('PET', 'PET'), ('MRI', 'PET'), ('EUS', 'EUS'), ('Bne Densitometry(DEXA)', 'Bne Densitometry(DEXA)'), ('Fluoroscopy', 'Fluoroscopy'), ('Mammography', 'Mammography')], max_length=100)),
                ('price', models.IntegerField(null=True)),
                ('scan_test_list', models.TextField(null=True)),
                ('google_location', models.CharField(max_length=100, null=True)),
                ('aboutlab_description', models.TextField(null=True)),
            ],
        ),
    ]

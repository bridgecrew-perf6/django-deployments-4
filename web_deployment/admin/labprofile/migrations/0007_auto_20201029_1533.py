# Generated by Django 2.2.5 on 2020-10-29 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labprofile', '0006_auto_20201029_1217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labentry',
            old_name='lab_alt_tag',
            new_name='lab_logo_alt_tag',
        ),
    ]

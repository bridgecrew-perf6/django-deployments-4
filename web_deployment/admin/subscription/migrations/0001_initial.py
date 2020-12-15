# Generated by Django 2.2.5 on 2020-10-30 02:57

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('customer_name', models.CharField(max_length=30, null=True)),
                ('category_id', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('plan_subscription', models.CharField(choices=[('Gold', 'Gold'), ('Silver', 'Silver'), ('Platinum', 'Platinum')], max_length=100, null=True)),
                ('payment', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]

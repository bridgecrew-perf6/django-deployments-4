# Generated by Django 2.2.5 on 2020-10-30 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_mainslider_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='mainslider',
            name='home_slider',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='settings.Post')),
            ],
        ),
    ]

# Generated by Django 2.2.5 on 2020-10-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labprofile', '0003_auto_20201028_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listoflabbooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('package_name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('image_url', models.CharField(max_length=20, null=True)),
                ('image_alt_tag', models.CharField(max_length=20, null=True)),
                ('video_url', models.CharField(max_length=20, null=True)),
                ('video_alt_tag', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Listofdoctor',
            new_name='Package',
        ),
        migrations.AddField(
            model_name='listoflab',
            name='lab_alt_image',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='listoflab',
            name='lab_alt_tag',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='listoflab',
            name='video_alt_tag',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='listoflab',
            name='video_url',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

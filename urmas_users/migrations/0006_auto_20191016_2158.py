# Generated by Django 2.2.5 on 2019-10-16 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urmas_users', '0005_auto_20191016_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(blank=True, default='/images/profile.png', null=True, upload_to='img'),
        ),
    ]

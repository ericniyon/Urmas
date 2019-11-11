# Generated by Django 2.2.5 on 2019-10-22 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboad', '0004_auto_20191022_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='destnation',
            field=models.CharField(help_text='address', max_length=100),
        ),
        migrations.AlterField(
            model_name='mission',
            name='duration_of_mission',
            field=models.CharField(help_text='Eg- HH:MM', max_length=100),
        ),
        migrations.AlterField(
            model_name='mission',
            name='invitation_latter',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mission',
            name='purpose',
            field=models.CharField(help_text='mission purpose', max_length=200),
        ),
        migrations.AlterField(
            model_name='mission',
            name='result',
            field=models.CharField(help_text='expected result to your mission', max_length=200),
        ),
        migrations.AlterField(
            model_name='staff',
            name='upload_file',
            field=models.FileField(blank=True, null=True, upload_to='request_doc'),
        ),
    ]
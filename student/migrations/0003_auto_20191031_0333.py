# Generated by Django 2.2 on 2019-10-30 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20191031_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='s1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='s2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='s3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='s4',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='s5',
            field=models.IntegerField(default=0),
        ),
    ]

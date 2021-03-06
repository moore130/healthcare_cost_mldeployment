# Generated by Django 3.0.4 on 2021-10-29 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0003_auto_20210920_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predresults',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='bmi',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='charges',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='children',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='sex_female',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='sex_male',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='smoke_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='smoke_yes',
            field=models.IntegerField(),
        ),
    ]

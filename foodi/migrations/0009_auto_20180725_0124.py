# Generated by Django 2.0.7 on 2018-07-25 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodi', '0008_auto_20180724_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='carbs',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='cholesterol',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='fiber',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='protein',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='sat_fat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='sodium',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='sugar',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='total_fat',
            field=models.FloatField(),
        ),
    ]

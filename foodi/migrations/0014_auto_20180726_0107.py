# Generated by Django 2.0.7 on 2018-07-26 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodi', '0013_auto_20180726_0044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diary',
            options={'ordering': ['date_eaten']},
        ),
    ]
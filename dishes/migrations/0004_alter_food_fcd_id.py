# Generated by Django 4.0.4 on 2022-07-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0003_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='fcd_id',
            field=models.IntegerField(),
        ),
    ]

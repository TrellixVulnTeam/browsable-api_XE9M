# Generated by Django 3.2.5 on 2022-02-06 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoint', '0004_auto_20220205_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
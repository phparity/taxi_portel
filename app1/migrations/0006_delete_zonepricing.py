# Generated by Django 4.2 on 2023-05-04 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0005_alter_zonepricing_zone"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ZonePricing",
        ),
    ]
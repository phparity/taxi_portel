# Generated by Django 4.2 on 2023-05-04 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0004_zonepricing"),
    ]

    operations = [
        migrations.AlterField(
            model_name="zonepricing",
            name="zone",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app1.mapzone"
            ),
        ),
    ]

# Generated by Django 4.2 on 2023-05-08 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0007_zonepricing"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="app1.customermanagement",
            ),
        ),
    ]

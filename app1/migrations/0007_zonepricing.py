# Generated by Django 4.2 on 2023-05-04 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0006_delete_zonepricing"),
    ]

    operations = [
        migrations.CreateModel(
            name="ZonePricing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("client_price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "supplier_price",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("driver_price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "zone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app1.mapzone"
                    ),
                ),
            ],
        ),
    ]

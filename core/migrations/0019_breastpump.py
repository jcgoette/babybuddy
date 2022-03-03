# Generated by Django 4.0.3 on 2022-03-02 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_bmi_headcircumference_height"),
    ]

    operations = [
        migrations.CreateModel(
            name="Breastpump",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.FloatField(verbose_name="Amount")),
                ("time", models.DateTimeField(verbose_name="Time")),
                (
                    "child",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="breastpump",
                        to="core.Child",
                        verbose_name="Child",
                    ),
                ),
            ],
            options={
                "verbose_name": "Breastpump",
                "verbose_name_plural": "Breastpump",
                "ordering": ["-time"],
                "default_permissions": ("view", "add", "change", "delete"),
            },
        ),
        migrations.AddField(
            model_name="breastpump",
            name="notes",
            field=models.TextField(blank=True, null=True, verbose_name="Notes"),
        ),
    ]
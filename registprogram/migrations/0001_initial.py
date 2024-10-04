# Generated by Django 5.1.1 on 2024-10-04 19:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Subject",
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
                ("course_id", models.CharField(max_length=100)),
                ("course_name", models.CharField(max_length=100)),
                ("course_field", models.CharField(max_length=100)),
                ("course_semester", models.IntegerField()),
                ("course_year", models.IntegerField()),
                ("course_amount", models.IntegerField()),
                ("course_status", models.CharField(max_length=10)),
            ],
        ),
    ]

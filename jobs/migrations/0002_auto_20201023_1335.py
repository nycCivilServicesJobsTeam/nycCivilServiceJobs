# Generated by Django 3.1.2 on 2020-10-23 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="job_record",
            options={"verbose_name_plural": "Job Records"},
        ),
    ]
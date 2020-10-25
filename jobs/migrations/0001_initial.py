# Generated by Django 3.1.2 on 2020-10-17 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="job_record",
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
                ("job_id", models.IntegerField()),
                ("agency", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "posting_type",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("num_positions", models.IntegerField(blank=True, null=True)),
                (
                    "business_title",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "civil_service_title",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "title_classification",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "title_code_no",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("level", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "job_category",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "full_time_part_time_indicator",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "career_level",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("salary_range_from", models.FloatField(blank=True, null=True)),
                ("salary_range_to", models.FloatField(blank=True, null=True)),
                (
                    "salary_frequency",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("work_location", models.TextField(blank=True, null=True)),
                (
                    "division_work_unit",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("job_description", models.TextField(blank=True, null=True)),
                ("minimum_qual_requirements", models.TextField(blank=True, null=True)),
                ("preferred_skills", models.TextField(blank=True, null=True)),
                ("additional_information", models.TextField(blank=True, null=True)),
                ("to_apply", models.TextField(blank=True, null=True)),
                ("hours_shift", models.TextField(blank=True, null=True)),
                ("work_location_1", models.TextField(blank=True, null=True)),
                (
                    "recruitment_contact",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("residency_requirement", models.TextField(blank=True, null=True)),
                ("posting_date", models.DateTimeField(blank=True, null=True)),
                ("post_until", models.DateField(blank=True, null=True)),
                ("posting_updated", models.DateTimeField(blank=True, null=True)),
                ("process_date", models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]

# Generated by Django 3.1.2 on 2020-12-01 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="faq",
            fields=[
                ("faq_id", models.AutoField(primary_key=True, serialize=False)),
                ("question", models.CharField(blank=True, max_length=1000, null=True)),
                ("answer", models.CharField(blank=True, max_length=1000, null=True)),
                ("date_published", models.DateField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "Frequently Asked Questions",
            },
        ),
    ]

# Generated by Django 4.2.7 on 2024-01-05 11:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.CharField(
                blank=True, default="profile/basic.png", max_length=200, null=True
            ),
        ),
    ]
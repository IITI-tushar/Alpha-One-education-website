# Generated by Django 5.1.6 on 2025-03-27 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0047_review_is_featured"),
    ]

    operations = [
        migrations.CreateModel(
            name="ScheduledPost",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("content", models.CharField(max_length=280)),
                ("image", models.ImageField(blank=True, upload_to="scheduled_posts/")),
                ("scheduled_time", models.DateTimeField()),
                ("posted", models.BooleanField(default=False)),
                ("posted_at", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="profile",
            name="is_social_media_manager",
            field=models.BooleanField(default=False),
        ),
    ]

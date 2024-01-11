# Generated by Django 5.0 on 2023-12-23 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CONlog",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("subsr", models.IntegerField(default=None, null=True)),
                ("SMRY", models.TextField(default=None, max_length=2000, null=True)),
                ("ACTR_DISP", models.CharField(default=None, max_length=10, null=True)),
                ("disp_rtm", models.CharField(default=None, max_length=10, null=True)),
                ("pinfo", models.CharField(default=None, max_length=10, null=True)),
                ("disp_rtm_sec", models.IntegerField(default=0, null=True)),
                ("image_id", models.IntegerField(default=0, null=True)),
                ("episode_num", models.IntegerField(default=0, null=True)),
                ("log_dt", models.DateTimeField(default=None, null=True)),
                ("year", models.IntegerField(default=0, null=True)),
                ("month", models.IntegerField(default=0, null=True)),
                ("day", models.IntegerField(default=0, null=True)),
                ("hour", models.IntegerField(default=0, null=True)),
                ("minute", models.IntegerField(default=0, null=True)),
                ("second", models.IntegerField(default=0, null=True)),
                ("weekday", models.IntegerField(default=0, null=True)),
                ("day_name", models.CharField(default=None, max_length=20, null=True)),
                ("subsr_id", models.IntegerField(default=0, null=True)),
                ("kids", models.IntegerField(default=0, null=True)),
                (
                    "program_name",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                ("ct_cl", models.CharField(default=None, max_length=50, null=True)),
                ("release_date", models.IntegerField(blank=True, null=True)),
                (
                    "program_genre",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                ("age_limit", models.CharField(default=None, max_length=20, null=True)),
                ("nokids", models.IntegerField(default=0, null=True)),
                ("program_id", models.IntegerField(default=0, null=True)),
                ("e_bool", models.IntegerField(default=0, null=True)),
            ],
            options={
                "db_table": "contlog",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Userinfo",
            fields=[
                ("subsr", models.IntegerField(default=None)),
                ("subsr_id", models.IntegerField(primary_key=True, serialize=False)),
                ("kids", models.BooleanField(default=0)),
                ("ip", models.CharField(blank=True, max_length=25, null=True)),
                ("cluster", models.IntegerField(blank=True, default=None, null=True)),
                ("is_superuser", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=False)),
            ],
            options={
                "db_table": "userinfo",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="VOD_INFO",
            fields=[
                ("id", models.AutoField(default=0, primary_key=True, serialize=False)),
                (
                    "program_name",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                ("ct_cl", models.CharField(default=None, max_length=50, null=True)),
                ("image_id", models.IntegerField(default=0, null=True)),
                (
                    "poster_url",
                    models.URLField(default=None, max_length=1000, null=True),
                ),
                ("release_date", models.IntegerField(blank=True, null=True)),
                (
                    "program_genre",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                ("age_limit", models.CharField(default=15, max_length=20, null=True)),
                ("nokids", models.IntegerField(default=0, null=True)),
                (
                    "program_id",
                    models.CharField(default=None, max_length=100, null=True),
                ),
                ("e_bool", models.BooleanField(default=0, null=True)),
                ("SMRY", models.TextField(default=None, null=True)),
                ("ACTR_DISP", models.TextField(default=None, null=True)),
            ],
            options={
                "db_table": "vodinfo",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="VODLog",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("subsr", models.IntegerField(default=0, null=True)),
                ("use_tms", models.IntegerField(default=0, null=True)),
                ("SMRY", models.TextField(default=None, max_length=2000, null=True)),
                ("ACTR_DISP", models.CharField(default=None, max_length=10, null=True)),
                ("disp_rtm", models.CharField(default=None, max_length=10, null=True)),
                ("upload_date", models.DateTimeField(default=None, null=True)),
                ("pinfo", models.CharField(default=None, max_length=10, null=True)),
                ("disp_rtm_sec", models.IntegerField(default=0, null=True)),
                ("image_id", models.IntegerField(default=0, null=True)),
                ("episode_num", models.IntegerField(default=0, null=True)),
                ("log_dt", models.DateTimeField(default=None, null=True)),
                ("year", models.IntegerField(default=0, null=True)),
                ("month", models.IntegerField(default=0, null=True)),
                ("day", models.IntegerField(default=0, null=True)),
                ("hour", models.IntegerField(default=0, null=True)),
                ("minute", models.IntegerField(default=0, null=True)),
                ("second", models.IntegerField(default=0, null=True)),
                ("weekday", models.IntegerField(default=0, null=True)),
                ("day_name", models.CharField(default=None, max_length=20, null=True)),
                ("subsr_id", models.IntegerField(null=True)),
                ("kids", models.IntegerField(default=0, null=True)),
                (
                    "program_name",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                ("ct_cl", models.CharField(default=None, max_length=50)),
                (
                    "release_date",
                    models.IntegerField(blank=True, default=None, null=True),
                ),
                (
                    "program_genre",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                ("age_limit", models.CharField(default=None, max_length=20, null=True)),
                ("nokids", models.IntegerField(default=0, null=True)),
                ("program_id", models.IntegerField(default=0, null=True)),
                ("count_watch", models.IntegerField(default=0, null=True)),
                ("e_bool", models.IntegerField(default=0, null=True)),
            ],
            options={
                "db_table": "vodlog",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="VODSumut",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("subsr", models.IntegerField(default=0, null=True)),
                ("use_tms", models.IntegerField(default=0, null=True)),
                ("SMRY", models.TextField(default=None, max_length=2000, null=True)),
                ("ACTR_DISP", models.CharField(default=None, max_length=10, null=True)),
                ("disp_rtm", models.CharField(default=None, max_length=10, null=True)),
                ("upload_date", models.DateTimeField(default=None, null=True)),
                ("pinfo", models.CharField(default=None, max_length=10, null=True)),
                ("disp_rtm_sec", models.IntegerField(default=0)),
                ("image_id", models.IntegerField(default=0, null=True)),
                ("episode_num", models.IntegerField(default=0, null=True)),
                ("log_dt", models.DateTimeField(default=None, null=True)),
                ("year", models.IntegerField(default=0, null=True)),
                ("month", models.IntegerField(default=0, null=True)),
                ("day", models.IntegerField(default=0, null=True)),
                ("hour", models.IntegerField(default=0, null=True)),
                ("minute", models.IntegerField(default=0, null=True)),
                ("second", models.IntegerField(default=0, null=True)),
                ("weekday", models.IntegerField(default=0, null=True)),
                ("day_name", models.CharField(default=None, max_length=20, null=True)),
                ("subsr_id", models.IntegerField(default=0, null=True)),
                (
                    "program_name",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                ("ct_cl", models.CharField(default=None, max_length=50, null=True)),
                ("release_date", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "program_genre",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                ("age_limit", models.CharField(default=None, max_length=20, null=True)),
                ("nokids", models.IntegerField(default=0, null=True)),
                ("program_id", models.IntegerField(default=0, null=True)),
                ("count_watch", models.IntegerField(default=0, null=True)),
                ("e_bool", models.IntegerField(default=0, null=True)),
            ],
            options={
                "db_table": "vods_sumut",
                "managed": True,
            },
        ),
    ]
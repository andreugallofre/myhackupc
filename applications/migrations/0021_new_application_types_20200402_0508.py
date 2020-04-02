# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-02 12:08
from __future__ import unicode_literals
import applications.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import uuid


def forwards_func(apps, schema_editor):
    Application = apps.get_model("applications", "Application")
    HackerApplication = apps.get_model("applications", "HackerApplication")
    for application in Application.objects.all():
        HackerApplication(
            uuid=application.uuid,
            user=application.user,
            type='H',
            submission_date=application.submission_date,
            status_update_date=application.status_update_date,
            status=application.status,
            gender=application.gender,
            other_gender=application.other_gender,
            under_age=application.under_age,
            phone_number=application.phone_number,
            diet=application.diet,
            other_diet=application.other_diet,
            tshirt_size=application.tshirt_size,
            origin=application.origin,
            first_timer=application.first_timer,
            lennyface=application.lennyface,
            graduation_year=application.graduation_year,
            university=application.university,
            degree=application.degree,
            contacted=application.contacted,
            description=application.description,
            reimb=application.reimb,
            contacted_by=application.contacted_by,
            invited_by=application.invited_by,
        ).save()


def reverse_func(apps, schema_editor):
    Application = apps.get_model("applications", "Application")
    HackerApplication = apps.get_model("applications", "HackerApplication")
    for application in HackerApplication.objects.all():
        Application(
            uuid=application.uuid,
            user=application.user,
            submission_date=application.submission_date,
            status_update_date=application.status_update_date,
            status=application.status,
            gender=application.gender,
            other_gender=application.other_gender,
            under_age=application.under_age,
            phone_number=application.phone_number,
            diet=application.diet,
            other_diet=application.other_diet,
            tshirt_size=application.tshirt_size,
            origin=application.origin,
            first_timer=application.first_timer,
            lennyface=application.lennyface,
            graduation_year=application.graduation_year,
            university=application.university,
            degree=application.degree,
            contacted=application.contacted,
            description=application.description,
            reimb=application.reimb,
            contacted_by=application.contacted_by,
            invited_by=application.invited_by,
        ).save()


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0009_user_types_20200321_0441'),
        ('applications', '0020_merge_20200328_0908'),
    ]

    operations = [
        migrations.CreateModel(
            name='HackerApplication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('type', models.CharField(max_length=10)),
                ('submission_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status_update_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('P', 'Under review'), ('R', 'Wait listed'), ('I', 'Invited'), ('LR', 'Last reminder'), ('C', 'Confirmed'), ('X', 'Cancelled'), ('A', 'Attended'), ('E', 'Expired'), ('D', 'Dubious'), ('IV', 'Invalid')], default='P', max_length=2)),
                ('gender', models.CharField(choices=[('NA', 'Prefer not to answer'), ('M', 'Male'), ('F', 'Female'), ('NB', 'Non-binary'), ('X', 'Prefer to self-describe')], default='NA', max_length=23)),
                ('other_gender', models.CharField(blank=True, max_length=50, null=True)),
                ('under_age', models.BooleanField()),
                ('phone_number', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format:                                                                       '+#########'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('diet', models.CharField(choices=[('None', 'No requirements'), ('Vegeterian', 'Vegeterian'), ('Vegan', 'Vegan'), ('No pork', 'No pork'), ('Gluten-free', 'Gluten-free'), ('Others', 'Others')], default='None', max_length=300)),
                ('other_diet', models.CharField(blank=True, max_length=600, null=True)),
                ('tshirt_size', models.CharField(choices=[('W-XSS', "Women's - XXS"), ('W-XS', "Women's - XS"), ('W-S', "Women's - S"), ('W-M', "Women's - M"), ('W-L', "Women's - L"), ('W-XL', "Women's - XL"), ('W-XXL', "Women's - XXL"), ('XXS', 'Unisex - XXS'), ('XS', 'Unisex - XS'), ('S', 'Unisex - S'), ('M', 'Unisex - M'), ('L', 'Unisex - L'), ('XL', 'Unisex - XL'), ('XXL', 'Unisex - XXL')], default='M', max_length=5)),
                ('origin', models.CharField(max_length=300)),
                ('first_timer', models.BooleanField(default=False)),
                ('lennyface', models.CharField(default='-.-', max_length=300)),
                ('graduation_year', models.IntegerField(choices=[(2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024')], default=2018)),
                ('university', models.CharField(max_length=300)),
                ('degree', models.CharField(max_length=300)),
                ('contacted', models.BooleanField(default=False)),
                ('description', models.TextField(max_length=500)),
                ('reimb', models.BooleanField(default=False)),
                ('reimb_amount', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, 'Negative? Really? Please put a positive value')])),
                ('contacted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacted_by', to=settings.AUTH_USER_MODEL)),
                ('invited_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invited_applications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MentorApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=300)),
                ('first_timer', models.BooleanField(default=False)),
                ('lennyface', models.CharField(default='-.-', max_length=300)),
                ('graduation_year', models.IntegerField(choices=[(2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024')], default=2018)),
                ('university', models.CharField(max_length=300)),
                ('degree', models.CharField(max_length=300)),
                ('projects', models.TextField(blank=True, max_length=500, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('devpost', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('site', models.URLField(blank=True, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes', validators=[applications.validators.validate_file_extension])),
                ('english_level', models.IntegerField(default=0)),
                ('attendance', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=100)),
                ('why_mentor', models.CharField(max_length=500)),
                ('first_time_mentor', models.BooleanField()),
                ('fluent', models.CharField(max_length=150)),
                ('experience', models.CharField(max_length=300)),
                ('study_work', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SponsorApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VolunteerApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=300)),
                ('first_timer', models.BooleanField(default=False)),
                ('lennyface', models.CharField(default='-.-', max_length=300)),
                ('graduation_year', models.IntegerField(choices=[(2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024')], default=2018)),
                ('university', models.CharField(max_length=300)),
                ('degree', models.CharField(max_length=300)),
                ('english_level', models.IntegerField(default=0)),
                ('attendance', models.CharField(max_length=200)),
                ('cool_skill', models.CharField(max_length=100)),
                ('first_time_volunteer', models.BooleanField()),
                ('quality', models.CharField(max_length=150)),
                ('weakness', models.CharField(max_length=150)),
                ('fav_movie', models.CharField(max_length=60, null=True)),
                ('friends', models.CharField(max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RunPython(forwards_func, reverse_func),
    ]

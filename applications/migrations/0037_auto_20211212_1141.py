# Generated by Django 3.2.7 on 2021-12-12 10:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0036_alter_hackerapplication_reimb_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackerapplication',
            name='graduation_year',
            field=models.IntegerField(choices=[(2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025'), (2026, '2026'), (2027, '2027')], default=2022),
        ),
        migrations.AlterField(
            model_name='hackerapplication',
            name='reimb_amount',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, 'Negative? Really? Please put a positive value'), django.core.validators.MaxValueValidator(150.0, 'Not that much')]),
        ),
        migrations.AlterField(
            model_name='mentorapplication',
            name='graduation_year',
            field=models.IntegerField(choices=[(2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025'), (2026, '2026'), (2027, '2027')], default=2022),
        ),
        migrations.AlterField(
            model_name='volunteerapplication',
            name='graduation_year',
            field=models.IntegerField(choices=[(2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025'), (2026, '2026'), (2027, '2027')], default=2022),
        ),
    ]
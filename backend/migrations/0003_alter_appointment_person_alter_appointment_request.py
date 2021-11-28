# Generated by Django 4.0.dev20210827112741 on 2021-11-28 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_appointment_capacity_donationquestion_person_request_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='person',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.person'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='request',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.request'),
        ),
    ]
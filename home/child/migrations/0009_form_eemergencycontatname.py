# Generated by Django 4.1.6 on 2023-02-19 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0008_alter_form_date_of_birth_bs'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='eemergencycontatname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

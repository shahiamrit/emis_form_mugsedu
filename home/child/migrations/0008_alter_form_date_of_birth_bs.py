# Generated by Django 4.1.6 on 2023-02-19 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0007_rename_emergency_contact_father_form_eemergency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='date_of_birth_bs',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

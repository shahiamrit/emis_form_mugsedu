# Generated by Django 4.1.6 on 2023-02-12 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationality', models.CharField(blank=True, max_length=200, null=True)),
                ('graduate_school', models.CharField(blank=True, max_length=200, null=True)),
                ('student_image', models.ImageField(upload_to='')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('citizenship_no', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('contact_no', models.IntegerField()),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=100, null=True)),
                ('ethnicity', models.CharField(blank=True, max_length=100, null=True)),
                ('religion', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth_bs', models.DateField()),
                ('date_of_birth_ad', models.DateField()),
                ('batch', models.CharField(blank=True, max_length=100, null=True)),
                ('disability_status', models.CharField(blank=True, max_length=100, null=True)),
                ('sponsorship_status', models.CharField(blank=True, max_length=100, null=True)),
                ('rural_district', models.CharField(blank=True, max_length=100, null=True)),
                ('martyr_lineage', models.BooleanField()),
                ('school', models.CharField(blank=True, max_length=100, null=True)),
                ('level', models.CharField(blank=True, max_length=100, null=True)),
                ('program', models.CharField(blank=True, max_length=100, null=True)),
                ('semester', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('degree_name', models.CharField(blank=True, max_length=100, null=True)),
                ('board_university', models.CharField(blank=True, max_length=100, null=True)),
                ('brade_division', models.CharField(blank=True, max_length=100, null=True)),
                ('insitution_type', models.CharField(blank=True, max_length=100, null=True)),
                ('certificate_of_completion', models.ImageField(upload_to='')),
                ('transcipt', models.ImageField(upload_to='')),
                ('provisional', models.ImageField(upload_to='')),
                ('migration', models.ImageField(upload_to='')),
                ('cgpa', models.CharField(blank=True, max_length=100, null=True)),
                ('enrollment', models.DateField()),
                ('completion', models.DateField()),
                ('year', models.DateField()),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('certificate', models.ImageField(upload_to='')),
                ('remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=100, null=True)),
                ('father_phone', models.IntegerField()),
                ('mother_phone', models.IntegerField()),
                ('father_email', models.EmailField(max_length=254)),
                ('mother_email', models.EmailField(max_length=254)),
                ('father_profession', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_profession', models.CharField(blank=True, max_length=100, null=True)),
                ('emergency_contact_father', models.IntegerField()),
                ('emergency_contact_mother', models.IntegerField()),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('relation_with_student', models.CharField(blank=True, max_length=100, null=True)),
                ('province', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('palika', models.CharField(blank=True, max_length=100, null=True)),
                ('ward_no', models.IntegerField()),
                ('street_name', models.CharField(blank=True, max_length=100, null=True)),
                ('house_no', models.IntegerField()),
                ('province_d', models.CharField(blank=True, max_length=100, null=True)),
                ('district_d', models.CharField(blank=True, max_length=100, null=True)),
                ('palika_d', models.CharField(blank=True, max_length=100, null=True)),
                ('ward_no_d', models.IntegerField()),
                ('street_name_d', models.CharField(blank=True, max_length=100, null=True)),
                ('house_no_d', models.IntegerField()),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('branch', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_account_number', models.IntegerField()),
                ('bank_phone_number', models.IntegerField()),
            ],
        ),
    ]

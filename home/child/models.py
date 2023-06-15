from django.db import models

# Create your models here.
class Form(models.Model):
    # home
    nationality = models.CharField(max_length=200, blank=True, null=True)
    graduate_school = models.CharField(max_length=200, blank=True, null=True)
    student_image = models.ImageField()
    

    # personal information
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    citizenship_no = models.CharField(max_length=100, blank=True, null=True)
    cit_att = models.ImageField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    contact_no = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    blood_group = models.CharField(max_length=100, blank=True, null=True)
    ethnicity = models.CharField(max_length=100, blank=True, null=True)
    religion = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth_bs = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth_ad = models.DateField()
    batch = models.CharField(max_length=100, blank=True, null=True)
    disability_status = models.CharField(max_length=100, blank=True, null=True)
    sponsorship_status = models.CharField(max_length=100, blank=True, null=True)
    rural_district = models.CharField(max_length=100, blank=True, null=True)
    martyr_lineage = models.CharField(max_length=100, blank=True, null=True)
    # program enrollment information
    school = models.CharField(max_length=100, blank=True, null=True)
    level = models.CharField(max_length=100, blank=True, null=True)
    program = models.CharField(max_length=100, blank=True, null=True)
    semester = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)

    # Education History one
    degree_name = models.CharField(max_length=100, blank=True, null=True)
    board_university = models.CharField(max_length=100, blank=True, null=True)
    brade_division = models.CharField(max_length=100, blank=True, null=True)
    insitution = models.CharField(max_length=100, blank=True, null=True)
    insitution_type = models.CharField(max_length=100, blank=True, null=True)
    certificate_of_completion = models.ImageField()
    transcipt = models.ImageField()
    provisional = models.ImageField()
    migration = models.ImageField()
    cgpa = models.CharField(max_length=100, blank=True, null=True)
    enrollment = models.DateField()
    completion = models.DateField()

    degname1 = models.CharField(max_length=100, blank=True, null=True)
    university1 = models.CharField(max_length=100, blank=True, null=True)
    grade1 = models.CharField(max_length=100, blank=True, null=True)
    institution1 = models.CharField(max_length=100, blank=True, null=True)
    instype1 = models.CharField(max_length=100, blank=True, null=True)
    coc1 = models.ImageField(blank=True, null=True)
    tsc1 = models.ImageField(blank=True, null=True)
    prl1 = models.ImageField(blank=True, null=True)
    mgr1 = models.ImageField(blank=True, null=True)
    cgpa1 = models.CharField(max_length=100, blank=True, null=True)
    enrollmentyr1 = models.DateField(blank=True, null=True)
    completionyr1 = models.DateField(blank=True, null=True)

    degname2 = models.CharField(max_length=100, blank=True, null=True)
    university2 = models.CharField(max_length=100, blank=True, null=True)
    grade2 = models.CharField(max_length=100, blank=True, null=True)
    institution2 = models.CharField(max_length=100, blank=True, null=True)
    instype2 = models.CharField(max_length=100, blank=True, null=True)
    coc2 = models.ImageField(blank=True, null=True)
    tsc2 = models.ImageField(blank=True, null=True)
    prl2 = models.ImageField(blank=True, null=True)
    mgr2 = models.ImageField(blank=True, null=True)
    cgpa2 = models.ImageField(blank=True, null=True)
    enrollmentyr2 = models.CharField(max_length=100, blank=True, null=True)
    completionyr2 = models.CharField(max_length=100, blank=True, null=True)

    # Awards, Merits and Scholarship
    year = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    certificate = models.ImageField(blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)

    # Guardian Information
    father_name = models.CharField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    father_phone = models.CharField(max_length=100, blank=True, null=True)
    mother_phone = models.CharField(max_length=100, blank=True, null=True)
    father_email = models.EmailField()
    mother_email = models.EmailField()
    father_profession = models.CharField(max_length=100, blank=True, null=True)
    mother_profession = models.CharField(max_length=100, blank=True, null=True)
    eemergencycontatname = models.CharField(max_length=100, blank=True, null=True)
    eemergency = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    relation_with_student = models.CharField(max_length=100, blank=True, null=True)

    # Permanent Address
    province = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    palika = models.CharField(max_length=100, blank=True, null=True)
    ward_no = models.IntegerField()
    street_name = models.CharField(max_length=100, blank=True, null=True)
    house_no = models.IntegerField()

    # Present Address
    province_d = models.CharField(max_length=100, blank=True, null=True)
    district_d = models.CharField(max_length=100, blank=True, null=True)
    palika_d = models.CharField(max_length=100, blank=True, null=True)
    ward_no_d = models.BigIntegerField()
    street_name_d = models.CharField(max_length=100, blank=True, null=True)
    house_no_d = models.BigIntegerField()

    # Other information

    # Bank Details 
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    branch = models.CharField(max_length=100, blank=True, null=True)
    bank_account_number = models.CharField(max_length=100, blank=True, null=True)
    bank_phone_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    
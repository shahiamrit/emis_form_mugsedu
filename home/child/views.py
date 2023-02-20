from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Form

# Create your views here.


def home(request):
    if request.method == 'POST':
        nepali = request.POST.get('flexRadioDefault', '')
        userimg = request.FILES.get('userimg', '')
        school = request.POST.get('school', '')
        firstname = request.POST.get('firstname', '')
        middlename = request.POST.get('middlename', '')
        lastname = request.POST.get('lastname', '')
        citizenship = request.POST.get('citizenship', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')
        gender = request.POST.get('gender', '')
        blood = request.POST.get('blood', '')
        ethnicity = request.POST.get('eth', '')
        religion = request.POST.get('rel', '')
        dobbs = request.POST.get('bs', '')
        dobad = request.POST.get('ad', '')
        batch = request.POST.get('batch', '')
        disability = request.POST.get('disability', '')
        sponsorship = request.POST.get('sponsorship', '')
        rural = request.POST.get('rural', '')
        martial = request.POST.get('martial', '')
        # block 2

        school = request.POST.get('school', '')
        level = request.POST.get('level', '')
        program = request.POST.get('program', '')
        semester = request.POST.get('semester', '')
        status = request.POST.get('status', '')
        # block 3

        degname = request.POST.get('degname', '')
        university = request.POST.get('university', '')
        grade = request.POST.get('grade', '')
        institution = request.POST.get('institution', '')
        instype = request.POST.get('instype', '')
        coc = request.FILES.get('coc', '')
        tsc = request.FILES.get('tsc', '')
        prl = request.FILES.get('prl','')
        mgr = request.FILES.get('mgr', '')
        cgpa = request.POST.get('cgpa', '')
        enrollmentyr = request.POST.get('enrollmentyr', '')
        completionyr = request.POST.get('completionyr', '')

        degname1 = request.POST.get('degname1', '')
        university1 = request.POST.get('university1', '')
        grade1 = request.POST.get('grade1', '')
        institution1 = request.POST.get('institution1', '')
        instype1 = request.POST.get('instype1', '')
        coc1 = request.FILES.get('coc1', '')
        tsc1 = request.FILES.get('tsc1', '')
        prl1 = request.FILES.get('prl1','')
        mgr1 = request.FILES.get('mgr1', '')
        cgpa1 = request.POST.get('cgpa1', '')
        enrollmentyr1 = request.POST.get('enrollmentyr1', '')
        completionyr1 = request.POST.get('completionyr1', '')

        degname2 = request.POST.get('degname2', '')
        university2 = request.POST.get('university2', '')
        grade2 = request.POST.get('grade2', '')
        institution2 = request.POST.get('institution2', '')
        instype2 = request.POST.get('instype2', '')
        coc2 = request.FILES.get('coc2', '')
        tsc2 = request.FILES.get('tsc2', '')
        prl2 = request.FILES.get('prl2','')
        mgr2 = request.FILES.get('mgr2', '')
        cgpa2 = request.POST.get('cgpa2', '')
        enrollmentyr2 = request.POST.get('enrollmentyr2', '')
        completionyr2 = request.POST.get('completionyr2', '')

        # Block 4
        ayear = request.POST.get('ayear', '')
        atitle = request.POST.get('atitle', '')
        acertificate = request.FILES.get('acertificate', '')
        aremarks = request.POST.get('aremarks', '')

        # Block 5
        fname = request.POST.get('fname', '')
        mname = request.POST.get('mname', '')
        fphone = request.POST.get('fphone', '')
        mphone = request.POST.get('mphone', '')
        femail = request.POST.get('femail', '')
        memail = request.POST.get('memail', '')
        fprofession = request.POST.get('fprofession', '')
        mprofession = request.POST.get('mprofession', '')
        eemergencycontatname = request.POST.get('eemergencycontatname', '')
        econtact = request.POST.get('econtact', '')
        addressfield = request.POST.get('addressfield', '')
        rwstudent = request.POST.get('rwstudent', '')
        
        # Block 6
        provice = request.POST.get('provice', '')
        district = request.POST.get('district', '')
        palika = request.POST.get('palika', '')
        wardno = request.POST.get('wardno', '')
        streetname = request.POST.get('streetname', '')
        houseno = request.POST.get('houseno', '')

        # Block 7
        provice1 = request.POST.get('provice1', '')
        district1 = request.POST.get('district1', '')
        palika1 = request.POST.get('palika1', '')
        wardno1 = request.POST.get('wardno1', '')
        streetname1 = request.POST.get('streetname1', '')
        houseno1 = request.POST.get('houseno1', '')
        

        # Block 8
        bname = request.POST.get('bname', '')
        branch = request.POST.get('branch', '')
        ban = request.POST.get('ban', '')
        rbn = request.POST.get('rbn', '')
        # Saving to models
        instances = []
        data = Form(nationality=nepali, student_image=userimg, graduate_school=school, first_name=firstname, middle_name=middlename, last_name=lastname, citizenship_no=citizenship, email=email, contact_no=contact, gender=gender, blood_group=blood, ethnicity=ethnicity, religion=religion, date_of_birth_bs=dobbs, date_of_birth_ad=dobad, batch=batch, disability_status=disability, sponsorship_status=sponsorship, rural_district=rural, martyr_lineage=martial, school=school, level=level, program=program, semester=semester, status=status, degree_name=degname, board_university=university, brade_division=grade, insitution=institution, insitution_type=instype, certificate_of_completion=coc, transcipt=tsc, provisional=prl, migration=mgr, cgpa=cgpa, enrollment=enrollmentyr, completion=completionyr, degname1=degname1, university1=university1, grade1=grade1, institution1=institution1, instype1=instype1, coc1=coc1, tsc1=tsc1, prl1=prl1, mgr1=mgr1, cgpa1=cgpa1, enrollmentyr1=enrollmentyr1, completionyr1=completionyr1, degname2=degname2, university2=university2, grade2=grade2, institution2=institution2, instype2=instype2, coc2=coc2, tsc2=tsc2, prl2=prl2, mgr2=mgr2, cgpa2=cgpa2, enrollmentyr2=enrollmentyr2, completionyr2=completionyr2, year=ayear, title=atitle, certificate=acertificate, remarks=aremarks, father_name=fname, mother_name=mname, father_phone=fphone, mother_phone=mphone, father_email=femail, mother_email=memail, father_profession=fprofession, mother_profession=mprofession, eemergencycontatname=eemergencycontatname, eemergency=econtact, address=addressfield, relation_with_student=rwstudent, province=provice, district=district, palika=palika, ward_no=wardno, street_name=streetname, house_no=houseno,  province_d=provice1, district_d=district1, palika_d=palika1, ward_no_d=wardno1, street_name_d=streetname1, house_no_d=houseno1, bank_name=bname, branch=branch, bank_account_number=ban, bank_phone_number=rbn)
        instances.append(data)
        Form.objects.bulk_create(instances)
        return HttpResponse('Thank you for filling out the form')
        

    return render(request, 'index.html')

def eadmin(request):
    data = Form.objects.all()
    return render(request, 'eadmin.html', {'data': data})

def updateView(request, pk):
    data = Form.objects.all().filter(id=pk)
    return render(request, 'update.html', {'data': data})

def deleteView(request, pk):
    data = Form.objects.all().filter(id=pk)
    data.delete()
    return HttpResponseRedirect('/eadmin')
    
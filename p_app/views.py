from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from p_app.models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            return HttpResponse(
                '''<script>alert("Both username and password are required.");window.location="/"</script>'''
                )
            # messages.error(request, "Both username and password are required.")
            # return redirect('/')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, "Login successful")
            if user.is_superuser:
                return HttpResponse(
                '''<script>alert("Login successful.");window.location="/admin_welcome"</script>'''
                )
                # return redirect('/admin_welcome')
            else:
                return HttpResponse(
                '''<script>alert("Login successful.");window.location="/staff_welcome"</script>'''
                )
                # return redirect('/staff_welcome')
        else:
            return HttpResponse(
                '''<script>alert("Invalid username or password.");window.location="/"</script>'''
            )
            # messages.error(request, "Invalid username or password")
            # return redirect('/')
    return render(request, 'login.html')

@login_required(login_url="/") 
def admin_wel(request):
    return render(request,'a_wel.html')

def logoutpage(request):
     logout(request)
     return redirect('/')

@login_required(login_url="/") 
def admin_add_staff(request):
    if request.method == 'POST':
        staff_id = request.POST['staff_id']
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST.get('gen')
        phoneno = request.POST['phoneno']
        photo = request.FILES.get('photo')
        if not staff_id or not name or not email or not gender or not phoneno or not photo :
            return HttpResponse(
                '''<script>alert("All fields are required.");window.location="/admin_add_staff"</script>'''
            )
            # messages.error(request, "All fields are required.")
            # return redirect('/admin_add_staff')
        if staffdata.objects.filter(staff_id = staff_id , email = email ).exists():
            return HttpResponse(
                '''<script>alert("Staff already exists.");window.location="/admin_add_staff"</script>'''
            )
            # messages.error(request, "Staff ID is already taken.")
            # return redirect('/admin_add_staff')
        data = User.objects.create_user(username=email,password=staff_id,email=email)
        data.save()
        ob = staffdata()
        ob.staff_id = staff_id
        ob.name = name
        ob.email = email
        ob.gender = gender
        ob.phoneno = phoneno
        ob.photo = photo
        ob.USER = data
        ob.save()
        return HttpResponse(
        '''<script>alert("New staff added successfully.");window.location="/admin_add_staff"</script>'''
        )
        # messages.success(request, "New staff added successfully.")
        # return redirect('/admin_add_staff')
    else :
        return render(request,'a_addstaff.html')

@login_required(login_url="/") 
def admin_view_staff(request):
    # if request.method == 'POST':
    #     search = request.POST['search']
    #     data = staffdata.objects.filter(Q(name__icontains=search) | Q(email__icontains=search) | Q(staff_id__icontains=search))
    #     return render(request,'a_viewstaff.html',{"data":data , "search" :search})
    # else :
    data = staffdata.objects.all()
    return render(request,'a_viewstaff.html',{"data":data})

@login_required(login_url="/") 
def admin_edit_staff(request,id):
    ob = staffdata.objects.get(id=id) 
    f = ob.USER
    if request.method == 'POST':
        staff_id = request.POST['staff_id']
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST.get('gen')
        phoneno = request.POST['phoneno']
        photo = request.FILES.get('photo')
        ob.staff_id = staff_id
        ob.name = name
        ob.email = email
        ob.gender = gender
        ob.phoneno = phoneno
        if photo:
            ob.photo = photo  
        ob.save()
        f.username = email 
        f.email=email
        f.save()
        return HttpResponse(
        '''<script>alert("Data updated successfully.");window.location="/admin_view_staff"</script>'''
        )
        # return redirect('/admin_view_staff')
    else :
        return render(request,'a_editstaff.html',{"data":ob})

@login_required(login_url="/") 
def admin_delete_staff(request,id):
    a = staffdata.objects.get(id=id)
    b = a.USER
    a.delete()
    b.delete()
    return HttpResponse(
        '''<script>alert("Data deleted successfully");window.location="/admin_view_staff"</script>'''
    )
    # return redirect('/admin_view_staff')

@login_required(login_url="/") 
def admin_add_bed(request):
    if request.method == 'POST':
        equipment = request.POST['equipment']
        quantity = request.POST['quantity']
        description = request.POST['description']
        if not equipment or not quantity or not description  :
            return HttpResponse(
                '''<script>alert("All fields are required.");window.location="/admin_add_bed"</script>'''
            )
            # messages.error(request, "All fields are required.")
            # return redirect('/admin_add_bed')
        if bedequip.objects.filter(equipment = equipment ).exists():
            return HttpResponse(
                '''<script>alert("Bed equipment  already exists.");window.location="/admin_add_bed"</script>'''
            )
            # messages.error(request, "Bed equipment is already added.")
            # return redirect('/admin_add_bed')
        ob = bedequip()
        ob.equipment = equipment
        ob.quantity = quantity
        ob.description = description
        ob.save()
        return HttpResponse(
        '''<script>alert("New bed equipment added successfully.");window.location="/admin_add_bed"</script>'''
        )
        # messages.success(request, "New bed equipment added successfully.")
        # return redirect('/admin_add_bed')
    return render(request,'a_addbed.html')

@login_required(login_url="/") 
def admin_view_bed(request):
    # if request.method == 'POST':
    #     search = request.POST['search']
    #     data = bedequip.objects.filter(Q(equipment__icontains=search) | Q(quantity__icontains=search) | Q(description__icontains=search))
    #     return render(request,'a_viewbed.html',{"data":data , "search" :search})
    # else :
    data = bedequip.objects.all()
    return render(request,'a_viewbed.html',{"data":data})
    
@login_required(login_url="/") 
def admin_edit_bed(request,id):
    ob = bedequip.objects.get(id=id) 
    if request.method == 'POST':
        equipment = request.POST['equipment']
        quantity = request.POST['quantity']
        description = request.POST['description']
        ob.equipment = equipment
        ob.quantity = quantity
        ob.description = description  
        ob.save()
        return HttpResponse(
        '''<script>alert("Data updated successfully.");window.location="/admin_view_bed"</script>'''
        )
        # return redirect('/admin_view_bed')
    else :
        return render(request,'a_editbed.html',{"data":ob})

@login_required(login_url="/") 
def admin_delete_bed(request,id):
    bedequip.objects.get(id=id).delete()
    return HttpResponse(
        '''<script>alert("Data deleted successfully.");window.location="/admin_view_bed"</script>'''
    )
    # return redirect('/admin_view_bed')

@login_required(login_url="/") 
def admin_view_div(request):
    # if request.method == 'POST':
    #     search = request.POST['search']
    #     data = division.objects.filter(name__icontains=search)
    #     return render(request,'a_viewdiv.html',{"data":data , "search" :search})
    data = division.objects.all()
    return render(request,'a_viewdiv.html',{"data":data})

@login_required(login_url="/") 
def admin_view_div_patients(request,id):
    # if request.method == 'POST':
    #     search = request.POST['search']
    #     data = patientdata.objects.filter(Q(name__icontains=search) | Q(email__icontains=search) | Q(phoneno__icontains=search)  )
    #     return render(request,'a_divpat.html',{"data":data , "search" :search})
    # else :    
    ob = patientdata.objects.filter(DIV = id)
    return render(request,'a_divpat.html',{"data":ob})

@login_required(login_url="/") 
def admin_view_feedback(request):
    # if request.method == 'POST':
    #     search = request.POST['search']
    #     data = feedback.objects.filter(Q(STAFF__name__icontains=search) | Q(date__icontains=search) | Q(feedback__icontains=search))
    #     return render(request,'a_viewfeed.html',{"data":data , "search" :search})
    # else :
    data = feedback.objects.all()
    return render(request,'a_viewfeed.html',{"data":data})

@login_required(login_url="/") 
def admin_patient_history(request):
    # if request.method == 'POST':
    #     search = request.POST['search']
    #     data = patientdata.objects.filter(Q(name__icontains=search) | Q(email__icontains=search) | Q(phoneno__icontains=search) )
    #     return render(request,'a_viewpathis.html',{"data":data , "search" :search})
    # else :
    data = patientdata.objects.all()
    return render(request,'a_viewpathis.html',{"data":data})

@login_required(login_url="/") 
def admin__view_patient_report(request):
    data = report.objects.all()
    return render(request,'a_viewreport.html',{"data":data})
    
@login_required(login_url="/") 
def admin_change_pass(request):
    if request.method == 'POST':
        currpass = request.POST['currpass']
        newpass = request.POST['newpass']
        conpass = request.POST['conpass']  
        user = request.user

        if not user.check_password(currpass):
            return HttpResponse(
            '''<script>alert("Current password is incorrect.");window.location="/admin_change_password"</script>'''
            )
            # messages.error(request, "Current password is incorrect.")
        elif newpass != conpass:
            return HttpResponse(
            '''<script>alert("New password and confirm password do not match.");window.location="/admin_change_password"</script>'''
            )
            # messages.error(request, "New password and confirm password do not match.")
        else:
            user.set_password(newpass)
            user.save()
            return HttpResponse(
                '''<script>alert("Password changed successfully");window.location="/"</script>'''
            )
    else :
        return render(request, 'a_changepass.html')



@login_required(login_url="/") 
def staff_wel(request):
    data = staffdata.objects.get(USER = request.user)
    return render(request,'s_wel.html',{"data":data})

@login_required(login_url="/") 
def staff_view_profile(request):
    data = staffdata.objects.get(USER = request.user)
    return render(request,'s_viewprof.html',{"data":data})

@login_required(login_url="/") 
def staff_add_patient(request):
    divdata = division.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        dob = request.POST['dob']
        gender = request.POST['gen']
        phoneno = request.POST['phoneno']
        photo = request.FILES.get('photo')
        place = request.POST['place']
        district = request.POST['district']
        state = request.POST['state']
        pin = request.POST['pin']
        div_id = request.POST['div']

        if not (name and email and dob and gender and phoneno and photo and place and district and state and pin and div_id):
            return HttpResponse(
            '''<script>alert("All fields are required.");window.location="/staff_add_patient"</script>'''
            )
            # messages.error(request, " All fields are required.")
            # return redirect('/staff_add_patient')

        if patientdata.objects.filter(name=name, phoneno=phoneno , email=email).exists():
            return HttpResponse(
            '''<script>alert("Patient  already exists.");window.location="/staff_add_patient"</script>'''
            )
            # messages.error(request, " Patient is already added.")
            # return redirect('/staff_add_patient')

        ob = patientdata()
        ob.name = name
        ob.email = email
        ob.dob = dob
        ob.gender = gender
        ob.phoneno = phoneno
        ob.photo = photo
        ob.place = place
        ob.district = district
        ob.state = state
        ob.pin = pin
        ob.DIV = division.objects.get(id=div_id)
        ob.save()
        return HttpResponse(
            '''<script>alert("New patient added successfully.");window.location="/staff_add_patient"</script>'''
        )
        # messages.success(request, " New patient added successfully.")
        # return redirect('/staff_add_patient')
    else :
        return render(request, 's_addpatient.html', {"divisions": divdata})

@login_required(login_url="/") 
def staff_view_patient(request):
    data = patientdata.objects.all()
    return render(request,'s_viewpatient.html',{"data":data})

@login_required(login_url="/") 
def staff_search_patient(request):
    query = request.GET.get("q", "")
    patients = patientdata.objects.all()

    if query:
        patients = patients.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(phoneno__icontains=query)
        )

    results = [
        {
            "id": p.id,
            "name": p.name,
            "email": p.email,
            "dob": p.dob.strftime("%Y-%m-%d") if p.dob else "",
            "gender": p.gender,
            "phoneno": p.phoneno,
            "place": p.place,
            "district": p.district,
            "state": p.state,
            "pin": p.pin,
            "division": p.DIV.name if p.DIV else "",
            "photo": p.photo.url if p.photo else None,
        }
        for p in patients
    ]
    return JsonResponse({"results": results})


@login_required(login_url="/") 
def staff_edit_patient(request,id):
    ob = patientdata.objects.get(id = id)
    divdata = division.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        dob = request.POST['dob']
        gender = request.POST.get('gen')
        phoneno = request.POST['phoneno']
        photo = request.FILES.get('photo')
        place = request.POST['place']
        district = request.POST['district']
        state = request.POST['state']
        pin = request.POST['pin']
        div_id = request.POST['div']
        ob.name = name
        ob.email = email
        ob.dob = dob
        ob.gender = gender
        ob.phoneno = phoneno
        if photo:
            ob.photo = photo 
        ob.place = place
        ob.district = district
        ob.state = state
        ob.pin = pin
        ob.DIV = division.objects.get(id = div_id) 
        ob.save()
        return HttpResponse(
            '''<script>alert("Data updated successfully.");window.location="/staff_view_patient"</script>'''
            )
        # return redirect('/staff_view_patient')
    else :
        return render(request,'s_editpatient.html',{"divisions":divdata,"data":ob})

@login_required(login_url="/") 
def staff_delete_patient(request,id):
    patientdata.objects.get(id = id).delete()
    return HttpResponse(
        '''<script>alert("Data deleted successfully.");window.location="/staff_view_patient"</script>'''
    )
    # return redirect('/staff_view_patient')

@login_required(login_url="/") 
def staff_add_feedback(request):
    if request.method == 'POST':
        feed = request.POST['feedback']
        if not feed :
            return HttpResponse(
            '''<script>alert("Enter a valid feedback.");window.location="/staff_add_feedback"</script>'''
            )
            # messages.error(request, "Enter a valid feedback")
            # return redirect('/staff_add_feedback')
        ob = feedback()
        ob.feedback = feed
        ob.STAFF = staffdata.objects.get(USER = request.user)
        ob.save()
        return HttpResponse(
            '''<script>alert("Feedback added successfully.");window.location="/staff_add_feedback"</script>'''
            )
        # messages.success(request, "Feedback added successfully")
        # return redirect('/staff_add_feedback')
    else :
        return render(request,'s_addfeedback.html')

@login_required(login_url="/") 
def staff_view_feedback(request):
    data = staffdata.objects.get(USER = request.user)
    ob = feedback.objects.filter(STAFF = data)
    # if request.method == 'POST':
    #     search = request.POST['search']
    #     data = feedback.objects.filter(Q(date__icontains=search) | Q(feedback__icontains=search))
    #     return render(request,'s_viewfeedback.html',{"data":data , "search" :search})
    # else :
    return render(request,'s_viewfeedback.html',{"data":ob})

@login_required(login_url="/") 
def staff_add_report(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        date = request.POST['date']
        if not file or not date :
            return HttpResponse(
            '''<script>alert("All fields are required.");window.location="/staff_add_report"</script>'''
            )
            # messages.error(request,"All fields are required.")
            # return redirect('/staff_add_report')
        ob = report()
        ob.file = file
        ob.date = date
        ob.STAFF = staffdata.objects.get(USER = request.user)
        ob.save()
        return HttpResponse(
            '''<script>alert("Report added successfully.");window.location="/staff_add_report"</script>'''
        )
        # messages.success(request,"Report added successfully")
        # return redirect('/staff_add_report')
    return render(request,'s_report.html')

@login_required(login_url="/") 
def staff_add_medicine(request):
    if request.method == 'POST':
        name = request.POST['medicine']
        description = request.POST['description']
        photo = request.FILES.get('photo')
        if not name or not description or not photo :
            return HttpResponse(
                '''<script>alert("All fields are required.");window.location="/staff_add_medicine_list"</script>'''
            )
            # messages.error(request,"All fields are required")
            # return redirect('/staff_add_medicine_list')
        ob = medicinedata()
        ob.name = name
        ob.description = description
        ob.photo = photo
        ob.STAFF = staffdata.objects.get(USER = request.user)
        ob.save()
        return HttpResponse(
        '''<script>alert("Medicine added successfully.");window.location="/staff_add_medicine_list"</script>'''
        )
        # messages.success(request,"Medicine added successfully")
        # return redirect('/staff_add_medicine_list')
    else :
        return render(request,'s_addmed.html')

@login_required(login_url="/") 
def staff_view_medicine(request):
    data = medicinedata.objects.all()
    return render(request,'s_viewmed.html',{"data":data})

@login_required(login_url="/") 
def staff_search_medicine(request):
    q = request.GET.get('q')
    medicines = medicinedata.objects.filter(name__icontains=q)
    results = []
    for med in medicines:
        results.append({
            'id': med.id,
            'name': med.name,
            'description': med.description,
            'updated_at': med.updated_at.strftime('%Y-%m-%d'),
            'photo_url': request.build_absolute_uri(med.photo.url),  # FULL URL
        })
    return JsonResponse({'results': results})


@login_required(login_url="/") 
def staff_edit_medicine(request,id):
    data = medicinedata.objects.get(id = id)
    if request.method == 'POST':
        name = request.POST['medicine']
        description = request.POST['description']
        photo = request.FILES.get('photo')
        data.name = name
        data.description = description
        if photo:
            data.photo = photo 
        data.save()
        return HttpResponse(
        '''<script>alert("Data updated successfully.");window.location="/staff_view_medicine_list"</script>'''
        )
        # return redirect('/staff_view_medicine_list')
    else :
        return render(request,'s_editmed.html',{"data":data})

@login_required(login_url="/") 
def staff_delete_medicine(request,id):
    medicinedata.objects.get(id = id).delete()
    return HttpResponse(
        '''<script>alert("Data deleted successfully.");window.location="/staff_view_medicine_list"</script>'''
    )
    # return redirect('/staff_view_medicine_list')

@login_required(login_url="/") 
def staff_change_pass(request):
    if request.method == 'POST':
        currpass = request.POST['currpass']
        newpass = request.POST['newpass']
        conpass = request.POST['conpass']  
        user = request.user

        if not user.check_password(currpass):
            return HttpResponse(
                '''<script>alert("Current password is incorrect.");window.location="/staff_change_password"</script>'''
            )
            # messages.error(request, "Current password is incorrect.")
        elif newpass != conpass:
            return HttpResponse(
                '''<script>alert("New password and confirm password do not match.");window.location="/staff_change_password"</script>'''
            )
            # messages.error(request, "New password and confirm password do not match.")
        else:
            user.set_password(newpass)
            user.save()
            return HttpResponse(
                '''<script>alert("Password changed successfully");window.location="/"</script>'''
            )
    else :
        return render(request, 's_changepass.html')

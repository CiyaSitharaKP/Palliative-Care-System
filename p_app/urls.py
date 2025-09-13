
from django.contrib import admin
from django.urls import path
from p_app import views

urlpatterns = [
    path('',views.loginpage),
    path('admin_welcome/',views.admin_wel),
    path('logout/',views.logoutpage),
    path('admin_add_staff/',views.admin_add_staff),
    path('admin_view_staff/',views.admin_view_staff),
    path('admin_edit_staff/<id>/',views.admin_edit_staff),
    path('admin_delete_staff/<id>/',views.admin_delete_staff),
    path('admin_add_bed/',views.admin_add_bed),
    path('admin_view_bed/',views.admin_view_bed),
    path('admin_edit_bed/<id>/',views.admin_edit_bed),
    path('admin_delete_bed/<id>/',views.admin_delete_bed),
    path('admin_view_divisions/',views.admin_view_div),
    path('admin_division_patients/<id>/',views.admin_view_div_patients),
    path('admin_view_feedback/',views.admin_view_feedback),
    path('admin_view_patient_history/',views.admin_patient_history),
    path('admin_view_patient_report/',views.admin__view_patient_report),
    path('admin_change_password/',views.admin_change_pass),
    path('staff_welcome/',views.staff_wel),
    path('staff_view_profile/',views.staff_view_profile),
    path('staff_change_password/',views.staff_change_pass),
    path('staff_add_patient/',views.staff_add_patient),
    path('staff_view_patient/',views.staff_view_patient),
    path('staff_edit_patient/<id>/',views.staff_edit_patient),
    path('staff_delete_patient/<id>/',views.staff_delete_patient),
    path('staff_add_feedback/',views.staff_add_feedback),
    path('staff_view_feedback/',views.staff_view_feedback),
    path('staff_search_patient/',views.staff_search_patient),
    path('staff_add_report/',views.staff_add_report),
    path('staff_add_medicine_list/',views.staff_add_medicine),
    path('staff_view_medicine_list/',views.staff_view_medicine),
    path('staff_search_medicine/',views.staff_search_medicine),
    path('staff_edit_medicine_list/<id>/',views.staff_edit_medicine),
    path('staff_delete_medicine_list/<id>/',views.staff_delete_medicine),
    
] 

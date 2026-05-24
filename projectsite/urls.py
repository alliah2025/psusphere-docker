"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView
from studentorg import views

from studentorg.views import (
    OrgMemberListView, OrgMemberCreateView,
    OrgMemberUpdateView, OrgMemberDeleteView,
    CollegeListView, CollegeCreateView,
    CollegeUpdateView, CollegeDeleteView,
    ProgramListView, ProgramCreateView, ProgramUpdateView, ProgramDeleteView,
    StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView
)

urlpatterns = [ 
    # organization
    path("admin/", admin.site.urls), 
    path("accounts/", include("allauth.urls")), # allauth routes
    path('', views.HomePageView.as_view(), name='home'),

    path('organization_list', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>',OrganizationUpdateView.as_view(), name= 'organization-update'),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name='organization-delete'),

    # Org Members
    path('orgmembers', OrgMemberListView.as_view(), name='orgmember-list'),
    path('orgmembers/add/', OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('orgmembers/<pk>/', OrgMemberUpdateView.as_view(), name='orgmember-update'),
    path('orgmembers/<pk>/delete/', OrgMemberDeleteView.as_view(), name='orgmember-delete'),

    # Colleges
    path('colleges', CollegeListView.as_view(), name='college-list'),
    path('colleges/add/', CollegeCreateView.as_view(), name='college-add'),
    path('colleges/<pk>/', CollegeUpdateView.as_view(), name='college-update'),
    path('colleges/<pk>/delete/', CollegeDeleteView.as_view(), name='college-delete'),

    # Org Members
     path('orgmembers/', OrgMemberListView.as_view(), name='orgmember-list'),
    path('orgmembers/add/', OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('orgmembers/<pk>/', OrgMemberUpdateView.as_view(), name='orgmember-update'),
    path('orgmembers/<pk>/delete/', OrgMemberDeleteView.as_view(), name='orgmember-delete'),

    # Colleges
    path('colleges/', CollegeListView.as_view(), name='college-list'),
    path('colleges/add/', CollegeCreateView.as_view(), name='college-add'),
    path('colleges/<pk>/', CollegeUpdateView.as_view(), name='college-update'),
    path('colleges/<pk>/delete/', CollegeDeleteView.as_view(), name='college-delete'),
        

    #Students
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/add/', StudentCreateView.as_view(), name='student-add'),
    path('students/<pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('students/<pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),

    #Program
    path('programs/', ProgramListView.as_view(), name='program-list'),
    path('programs/add/', ProgramCreateView.as_view(), name='program-add'),
    path('programs/<pk>/', ProgramUpdateView.as_view(), name='program-update'),
    path('programs/<pk>/delete/', ProgramDeleteView.as_view(), name='program-delete'),

    path('admin/', admin.site.urls),
]


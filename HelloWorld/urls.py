"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#-*-coding:utf-8-*-
from django.conf.urls import include, url
from django.contrib import admin
from webadmin import views
from webadmin.account import userlogin, changepassword
from django.contrib.auth.views import logout
from webadmin.student import studentprofile
from webadmin import myclass,student,assessment,grade,activity,comperformance
#import settings
#admin.autodiscover()


urlpatterns = [
    #url(r'^grappelli/',include(grappelli.urls)),
    url(r'^admin/', admin.site.urls),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^webadmin/', include('webadmin'), name='webadmin'),
    url(r'^$', views.index, name='index'),


    #url(r'^grappelli/',include('grappelli.urls')),

    #favicon.ico
    #url(r'^favicon.ico$', views.generic.base.RedirectView.as_view(url='/static/images/favicon.png')),

    url(r'^accounts/login/$', userlogin,name="userlogin"),
    url(r'^accounts/changepassword/$', changepassword,name="changepassword"),
    url(r'^accounts/logout/$',  logout, {'next_page': '/accounts/login/'},name="userlogout"),

    #captcha
    url(r'^captcha/', include('captcha.urls')),

    #class
    url(r'^manage/class/$', myclass.index,name="manageclass"),
    url(r'^manage/addclass/$', myclass.addclass,name="addclass"),
    url(r'^manage/editclass/$', myclass.editclass,name="editclass"),
    url(r'^manage/deleteclass/$', myclass.deleteclass,name="deleteclass"),
    #class ajax
    url(r'^ajax/get_classes_list/$', myclass.get_classes_list,name="get_classes_list"),

    #student
    url(r'^manage/student/$', student.index,name="managestudent"),
    url(r'^manage/addstudent/$', student.addstudent,name="addstudent"),
    url(r'^manage/editstudent/$', student.editstudent,name="editstudent"),
    url(r'^manage/deletestudent/$', student.deletestudent,name="deletestudent"),
    url(r'^manage/initstudent/$', student.initstudent,name="initstudent"),
    url(r'^studentprofile/$', student.studentprofile,name="studentprofile"),
    #student ajax
    url(r'^ajax/get_students_list/$', student.get_students_list,name="get_students_list"),
    url(r'^ajax/select_classes/$', myclass.select_classes,name="select_classes"),

    #assessment
    url(r'^manage/assessment/$', assessment.index,name="manageassessment"),
    url(r'^manage/addassessment/$', assessment.addassessment,name="addassessment"),
    url(r'^manage/editassessment/$', assessment.editassessment,name="editassessment"),
    url(r'^manage/deleteassessment/$', assessment.deleteassessment,name="deleteassessment"),
    url(r'^view/assessment/$', assessment.viewassessment,name="viewassessment"),
    #assessment ajax
    url(r'^ajax/get_assessments_list/$', assessment.get_assessments_list,name="get_assessments_list"),
    url(r'^ajax/view_assessments_list/$', assessment.view_assessments_list,name="view_assessments_list"),
    #student assessment
    url(r'^manage/goassessment/$', assessment.goassessment,name="goassessment"),
    #student assessment ajax
    url(r'^ajax/go_assessments_list/$', assessment.go_assessments_list,name="go_assessments_list"),
    url(r'^ajax/go_assessments/$', assessment.go_assessments,name="go_assessments"),

    #grade
    url(r'^grade/importgrades/$', grade.importgrades,name="importgrades"),
    url(r'^manage/grades/$', grade.index,name="managegrades"),
    url(r'^manage/classgrades/$', grade.classgrades,name="classgrades"),
    #ajax grades
    url(r'^ajax/studentgrades/$', grade.studentgrades,name="studentgrades"),
    url(r'^ajax/ajaxclassgrades/$', grade.ajaxclassgrades,name="ajaxclassgrades"),

    #activity
    url(r'^manage/behavior/$', activity.behavior,name="behavior"),
    url(r'^manage/addbehavior/$', activity.addbehavior,name="addbehavior"),
    url(r'^manage/editbehavior/$', activity.editbehavior,name="editbehavior"),
    url(r'^manage/deletebehavior/$', activity.deletebehavior,name="deletebehavior"),
    url(r'^manage/adddevelopment/$', activity.adddevelopment,name="adddevelopment"),
    url(r'^manage/editdevelopment/$', activity.editdevelopment,name="editdevelopment"),
    url(r'^manage/deletedevelopment/$', activity.deletedevelopment,name="deletedevelopment"),
    url(r'^manage/development/$', activity.development,name="development"),
    #ajax activity
    url(r'^ajax/ajaxbehavior/$', activity.ajaxbehavior,name="ajaxbehavior"),
    url(r'^ajax/ajaxdevelopment/$', activity.ajaxdevelopment,name="ajaxdevelopment"),

    #comperformance
    url(r'^manage/comperformance_setup/$', comperformance.comperformance_setup,name="comperformance_setup"),
    url(r'^manage/addcomperformance_setup/$', comperformance.addcomperformance_setup,name="addcomperformance_setup"),
    url(r'^manage/editcomperformance_setup/$', comperformance.editcomperformance_setup,name="editcomperformance_setup"),
    url(r'^manage/deletecomperformance_setup/$', comperformance.deletecomperformance_setup,name="deletecomperformance_setup"),
    url(r'^manage/comperformance/$', comperformance.comperformance,name="comperformance"),
    url(r'^manage/studentcomperformance/$', comperformance.studentcomperformance,name="studentcomperformance"),
    url(r'^manage/classcomperformances/$', comperformance.classcomperformances,name="classcomperformances"),
    #ajax comperformance
    url(r'^ajax/ajaxcomperformance_setup/$', comperformance.ajaxcomperformance_setup,name="ajaxcomperformance_setup"),
    url(r'^ajax/ajaxclasscomperformances/$', comperformance.ajaxclasscomperformances,name="ajaxclasscomperformances"),
    url(r'^ajax/ajaxcomperformance/$', comperformance.ajaxcomperformance,name="ajaxcomperformance"),
    url(r'^ajax/ajaxupdatecomperformance/$', comperformance.ajaxupdatecomperformance,name="ajaxupdatecomperformance"),


]

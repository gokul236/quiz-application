from .import views
from django.urls import path

urlpatterns = [
    path("",views.loginpage,name="loginpage"),
    path("login",views.login1,name="login1"),
    path("register", views.register1, name="register1"),
    path("backtologin", views.backtologin, name="backtologin"),
    path("registersave", views.registersave, name="registersave"),
    path("adminlogout", views.adminlogout, name="adminlogout"),
    path("logout", views.logout, name="logout"),
    path("viewprofile", views.viewprofile, name="viewprofile"),
    path("bthfromviewprofile",views.bthfromviewprofile, name="bthfromviewprofile"),
    path("managequestions", views.managequestions, name="managequestions"),
    path("bthfrommanagequestions", views.bthfrommanagequestions, name="bthfrommanagequestions"),
    path("addquestion",views.addquestion, name="addquestion"),
    path("bthfromaddquestions",views.bthfromaddquestions,name="bthfromaddquestions"),
    path("savequestion",views.savequestion,name="savequestion"),
    path("removefromquestionstable",views.removefromquestionstable,name="removefromquestionstable"),
    path("manageusers",views.manageusers,name="manageusers"),
    path("bthfromusermanage",views.bthfromusermanage,name="bthfromusermanage"),
    path("removefromuserstable",views.removefromuserstable,name="removefromuserstable"),
    path("currentaffairs", views.currentaffairs, name="currentaffairs"),
    path("socialstudies", views.socialstudies, name="socialstudies"),
    path("basicscience", views.basicscience, name="basicscience"),
    path("maths", views.maths, name="maths"),
    path("mentalability", views.mentalability, name="mentalability"),
    path("generalknowledge", views.generalknowledge, name="generalknowledge"),
    path("optionabutton",views.optionabutton,name="optionabutton"),
    path("optionbbutton", views.optionbbutton, name="optionbbutton"),
    path("optioncbutton", views.optioncbutton, name="optioncbutton"),
    path("optiondbutton", views.optiondbutton, name="optiondbutton"),


    path("bthfromresult", views.bthfromresult, name="bthfromresult"),


]

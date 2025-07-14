from django.shortcuts import render
from django.http import HttpResponse
from .models import login
from .models import register
from .models import questionstable
import random


def loginpage(request):
    return render(request,"loginpage.html")
def login1(request):
    username=request.POST['username']
    password=request.POST['password']
    try:
        m=login.objects.get(username=username,password=password)
        if m.status=='1':
            request.session['user']=m.username
            return render(request,"userhome.html")
        elif m.status=='2':
            return render(request,"adminhome.html")
    except:
        return render(request,"loginpage.html")
def register1(request):
    return render(request,"registerpage.html")
def backtologin(request):
    return render(request,"loginpage.html")
def registersave(request):
    try:
        username = request.POST['username']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        photo = request.FILES['photo']
        qualification = request.POST['qualification']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password==confirmpassword:
            data=register(username=username,phonenumber=phonenumber,email=email,photo=photo,qualification=qualification,password=password,confirmpassword=confirmpassword)
            data.save()
            data1=login(username=username,password=password,status=1)
            data1.save()
            return render(request,"loginpage.html")
        else:
            return render(request,"registerpage.html")
    except:
        return render(request,"registerpage.html")
def adminlogout(request):
    return render(request,"loginpage.html")
def logout(request):
    return render(request,"loginpage.html")
def viewprofile(request):
    a=request.session['user']
    data=register.objects.filter(username=a)
    return render(request,"viewprofile.html",{'data':data})
def bthfromviewprofile(request):
    return render(request,"userhome.html")
def managequestions(request):
    data=questionstable.objects.all()
    return render(request,"managequestions.html",{'data':data})
def bthfrommanagequestions(request):
    return render(request, "adminhome.html")
def addquestion(request):
    return render(request,"addquestions.html")
def bthfromaddquestions(request):
    data1 = questionstable.objects.all()
    return render(request, "managequestions.html", {'data': data1})
def savequestion(request):
    try:
        questionid=request.POST['questionid']
        question= request.POST['question']
        optiona= request.POST['optiona']
        optionb= request.POST['optionb']
        optionc= request.POST['optionc']
        optiond= request.POST['optiond']
        correctanswer= request.POST['correctanswer']
        category= request.POST['category']
        if questionid=="":
            return render(request,"addquestions.html")
        elif question=="":
            return render(request, "addquestions.html")
        elif optiona=="":
            return render(request, "addquestions.html")
        elif optionb=="":
            return render(request, "addquestions.html")
        elif optionc=="":
            return render(request, "addquestions.html")
        elif optiond=="":
            return render(request, "addquestions.html")
        elif correctanswer=="":
            return render(request, "addquestions.html")
        elif category=="":
            return render(request, "addquestions.html")
        else:
            data = questionstable(questionid=questionid,question=question,optiona=optiona,optionb=optionb,optionc=optionc,optiond=optiond,correctanswer=correctanswer,category=category)
            data.save()
            data1 = questionstable.objects.all()
            return render(request, "managequestions.html", {'data': data1})
    except:
        return render(request, "addquestions.html")
def removefromquestionstable(request):
    id = request.POST['id']
    questionstable.objects.filter(id=id).delete()
    data1 = questionstable.objects.all()
    return render(request, "managequestions.html", {'data': data1})
def manageusers(request):
    data=register.objects.all()
    return render(request,"usermanage.html",{'data':data})
def bthfromusermanage(request):
    return render(request,"adminhome.html")
def removefromuserstable(request):
    id = request.POST['id']
    a=register.objects.get(id=id)
    register.objects.filter(username=a.username).delete()
    login.objects.filter(username=a.username).delete()
    data1 = register.objects.all()
    return render(request, "usermanage.html", {'data': data1})
def currentaffairs(request):
    try:
        correctanswercount = 0
        request.session['correctanswercount'] = correctanswercount
        percentage=0
        request.session['percentage'] = percentage
        status = ""
        request.session['status'] = status
        questionsgot = questionstable.objects.filter(category="current affairs")
        data=[]
        for i in questionsgot:
            data.append(i.questionid)
        randomgotid=random.choice(data)
        randomquestion=questionstable.objects.filter(questionid=randomgotid)
        data.remove(randomgotid)
        request.session['idlist']=data
        questionnumber = 1
        request.session['questionnumber'] = questionnumber
        return render(request, "questiondisplay.html",{'randomquestion':randomquestion,'questionnumber':questionnumber})
    except:
        return render(request,"userhome.html")
def socialstudies(request):
    try:
        correctanswercount = 0
        request.session['correctanswercount'] = correctanswercount
        percentage = 0
        request.session['percentage'] = percentage
        status=""
        request.session['status'] = status
        questionsgot = questionstable.objects.filter(category="social studies")
        data=[]
        for i in questionsgot:
            data.append(i.questionid)
        randomgotid=random.choice(data)
        randomquestion=questionstable.objects.filter(questionid=randomgotid)
        data.remove(randomgotid)
        request.session['idlist']=data
        questionnumber = 1
        request.session['questionnumber'] = questionnumber
        return render(request, "questiondisplay.html",{'randomquestion':randomquestion,'questionnumber':questionnumber})
    except:
        return render(request,"userhome.html")
def basicscience(request):
    try:
        correctanswercount = 0
        request.session['correctanswercount'] = correctanswercount
        percentage = 0
        request.session['percentage'] = percentage
        status = ""
        request.session['status'] = status
        questionsgot = questionstable.objects.filter(category="basic science")
        data=[]
        for i in questionsgot:
            data.append(i.questionid)
        randomgotid=random.choice(data)
        randomquestion=questionstable.objects.filter(questionid=randomgotid)
        data.remove(randomgotid)
        request.session['idlist']=data
        questionnumber = 1
        request.session['questionnumber'] = questionnumber
        return render(request, "questiondisplay.html",{'randomquestion':randomquestion,'questionnumber':questionnumber})
    except:
        return render(request,"userhome.html")
def maths(request):
    try:
        correctanswercount = 0
        request.session['correctanswercount'] = correctanswercount
        percentage = 0
        request.session['percentage'] = percentage
        status = ""
        request.session['status'] = status
        questionsgot = questionstable.objects.filter(category="maths")
        data=[]
        for i in questionsgot:
            data.append(i.questionid)
        randomgotid=random.choice(data)
        randomquestion=questionstable.objects.filter(questionid=randomgotid)
        data.remove(randomgotid)
        request.session['idlist']=data
        questionnumber = 1
        request.session['questionnumber'] = questionnumber
        return render(request, "questiondisplay.html",{'randomquestion':randomquestion,'questionnumber':questionnumber})
    except:
        return render(request,"userhome.html")
def mentalability(request):
    try:
        correctanswercount = 0
        request.session['correctanswercount'] = correctanswercount
        percentage = 0
        request.session['percentage'] = percentage
        status = ""
        request.session['status'] = status
        questionsgot = questionstable.objects.filter(category="mental ability")
        data=[]
        for i in questionsgot:
            data.append(i.questionid)
        randomgotid=random.choice(data)
        randomquestion=questionstable.objects.filter(questionid=randomgotid)
        data.remove(randomgotid)
        request.session['idlist']=data
        questionnumber = 1
        request.session['questionnumber'] = questionnumber
        return render(request, "questiondisplay.html",{'randomquestion':randomquestion,'questionnumber':questionnumber})
    except:
        return render(request,"userhome.html")
def generalknowledge(request):
    try:
        correctanswercount = 0
        request.session['correctanswercount'] = correctanswercount
        percentage = 0
        request.session['percentage'] = percentage
        status = ""
        request.session['status'] = status
        questionsgot = questionstable.objects.filter(category="general knowledge")
        data=[]
        for i in questionsgot:
            data.append(i.questionid)
        randomgotid=random.choice(data)
        randomquestion=questionstable.objects.filter(questionid=randomgotid)
        data.remove(randomgotid)
        request.session['idlist']=data
        questionnumber=1
        request.session['questionnumber']=questionnumber
        return render(request, "questiondisplay.html",{'randomquestion':randomquestion,'questionnumber':questionnumber})
    except:
        return render(request,"userhome.html")
def optionabutton(request):
    try:
        #correctanswer counting part
        optiona=request.POST['optiona']
        correctanswer=request.POST['correctanswer']
        if optiona == correctanswer:
            correctanswercount = request.session['correctanswercount']
            correctanswercount=correctanswercount+1
            request.session['correctanswercount']=correctanswercount
        #random question getting part
        data=request.session['idlist']
        randomgotid = random.choice(data)
        randomquestion = questionstable.objects.filter(questionid=randomgotid)
        data.remove(randomgotid)
        request.session['idlist'] = data
        #question number part
        questionnumber=request.session['questionnumber']
        questionnumber=questionnumber+1
        request.session['questionnumber'] = questionnumber
        if questionnumber>20:
            return render(request,"resultpage.html")
        return render(request, "questiondisplay.html", {'randomquestion': randomquestion,'questionnumber':questionnumber})
    except:
        #percentage counting part
        correctanswercount = request.session['correctanswercount']
        percentage = request.session['percentage']
        percentage=100*(correctanswercount/20)
        request.session['percentage']=percentage
        status=request.session['status']
        if percentage>75:
            status="you did it well"
        elif percentage>50:
            status="try hard to did well"
        else:
            status="poor try"
        request.session['status']=status
        #database adding

        return render(request,"resultpage.html",{'correctanswercount':correctanswercount,'percentage':percentage,'status':status})
def optionbbutton(request):
    try:
        # correctanswer counting part
        optionb = request.POST['optionb']
        correctanswer = request.POST['correctanswer']
        if optionb == correctanswer:
            correctanswercount = request.session['correctanswercount']
            correctanswercount = correctanswercount + 1
            request.session['correctanswercount'] = correctanswercount
        # random question getting part
        data=request.session['idlist']
        randomgotid = random.choice(data)
        randomquestion = questionstable.objects.filter(questionid=randomgotid)
        data.remove(randomgotid)
        request.session['idlist'] = data
        # question number part
        questionnumber = request.session['questionnumber']
        questionnumber = questionnumber + 1
        request.session['questionnumber'] = questionnumber
        if questionnumber>20:
            return render(request,"resultpage.html")
        return render(request, "questiondisplay.html", {'randomquestion': randomquestion,'questionnumber':questionnumber})
    except:
        # percentage counting part
        correctanswercount = request.session['correctanswercount']
        percentage = request.session['percentage']
        percentage = 100 * (correctanswercount / 20)
        request.session['percentage'] = percentage
        status = request.session['status']
        if percentage > 75:
            status = "you did it well"
        elif percentage > 50:
            status = "try hard to did well"
        else:
            status = "poor try"
        request.session['status'] = status
        return render(request, "resultpage.html",{'correctanswercount': correctanswercount, 'percentage': percentage, 'status': status})
def optioncbutton(request):
    try:
        # correctanswer counting part
        correctanswercount = request.session['correctanswercount']
        optionc = request.POST['optionc']
        correctanswer = request.POST['correctanswer']
        if optionc == correctanswer:
            correctanswercount = correctanswercount + 1
            request.session['correctanswercount'] = correctanswercount
        # random question getting part
        data=request.session['idlist']
        randomgotid = random.choice(data)
        randomquestion = questionstable.objects.filter(questionid=randomgotid)
        data.remove(randomgotid)
        request.session['idlist'] = data
        # question number part
        questionnumber = request.session['questionnumber']
        questionnumber = questionnumber + 1
        request.session['questionnumber'] = questionnumber
        if questionnumber>20:
            return render(request,"resultpage.html")
        return render(request, "questiondisplay.html", {'randomquestion': randomquestion,'questionnumber':questionnumber})
    except:
        # percentage counting part
        correctanswercount = request.session['correctanswercount']
        percentage = request.session['percentage']
        percentage = 100 * (correctanswercount / 20)
        request.session['percentage'] = percentage
        status = request.session['status']
        if percentage > 75:
            status = "you did it well"
        elif percentage > 50:
            status = "try hard to did well"
        else:
            status = "poor try"
        request.session['status'] = status
        return render(request, "resultpage.html",{'correctanswercount': correctanswercount, 'percentage': percentage, 'status': status})
def optiondbutton(request):
    try:
        # correctanswer counting part
        optiond = request.POST['optiond']
        correctanswer = request.POST['correctanswer']
        if optiond == correctanswer:
            correctanswercount = request.session['correctanswercount']
            correctanswercount = correctanswercount + 1
            request.session['correctanswercount'] = correctanswercount
        # random question getting part
        data=request.session['idlist']
        randomgotid = random.choice(data)
        randomquestion = questionstable.objects.filter(questionid=randomgotid)
        data.remove(randomgotid)
        request.session['idlist'] = data
        # question number part
        questionnumber = request.session['questionnumber']
        questionnumber = questionnumber + 1
        request.session['questionnumber'] = questionnumber
        if questionnumber>20:
            return render(request,"resultpage.html")
        return render(request, "questiondisplay.html", {'randomquestion': randomquestion,'questionnumber':questionnumber})
    except:
        # percentage counting part
        correctanswercount = request.session['correctanswercount']
        percentage = request.session['percentage']
        percentage = 100 * (correctanswercount / 20)
        request.session['percentage'] = percentage
        status = request.session['status']
        if percentage > 75:
            status = "you did it well"
        elif percentage > 50:
            status = "try hard to did well"
        else:
            status = "poor try"
        request.session['status'] = status

        return render(request, "resultpage.html",{'correctanswercount': correctanswercount, 'percentage': percentage, 'status': status})
def bthfromresult(request):
    return render(request,"userhome.html")
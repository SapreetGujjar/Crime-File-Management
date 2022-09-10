from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.conf.urls.static import static
from crime.models import Newuser, Addnews, Addmissing, Addwanted, Addfir, Addregister, Addhistory, Addcom2, Addcrime, Addmessage
def index(request):
	data=Addwanted.objects.all()
	data2=Addmissing.objects.all()
	data3=Addnews.objects.all()
	return render(request,"template/index.html",{"alldata":data,"alldata2":data2,"alldata3":data3})
def regcode(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.POST['t5']
		f=request.FILES['t6']
		g=request.POST['t7']
		data2=Newuser.objects.filter(email=b).count()
		if data2==0:
			data=Newuser(name=a,email=b, pwd=c, no=d, pincode=e, img=f,address=g)
			data.save()
			request.session['email'] = b
			return redirect("/user/")
		else:
			user = "This Email Is All Ready Register"
			return render(request,"template/msg.html",{"msg":user})	
	else:
		redirect('/index/')
def login(request):
	return render(request,"template/login.html")
def logincode(request):
	if request.method=="POST":
		email= request.POST['t1']
		pwd= request.POST['t2']
		if email == "admin@gmail.com" and pwd=="admin":
			request.session['admin'] = email
			return redirect("/admin1/")
		else:
			user = Newuser.objects.filter(email=email, pwd=pwd).count()
			if(user==0):	
				user = "Not match"
				return render(request,"template/msg.html",{"msg":user})
			else:
				request.session['email'] = email
				return redirect("/user/")
def admin1(request):
	if request.session.has_key('admin'):
		email = request.session['admin']
		return render(request,"template/admin.html", {"usernames" : email})
	else:
		return redirect('/login/')
def addnews(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.POST['t5']
		data=Addnews(title=a,date=b, time=c, place=d, matter=e)
		data.save()
		return redirect("/d_news/")
def d_news(request):
	if request.session.has_key('admin'):
		email = request.session['admin']
		data=Addnews.objects.all()
		return render(request,"template/viewnews.html", {"usernames" : email,"alldata":data})
	else:
		return redirect('/login/')
def delete_news(request,pk):
	id=pk
	Addnews.objects.filter(p_id=id).delete()
	return redirect("/d_news/")
def missing(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.POST['t5']
		f=request.POST['t6']
		g=request.POST['t7']
		h=request.FILES['t8']
		i=request.POST['t9']
		data=Addmissing(name=a,age=b, sex=c, place=d, date=e,cmp1=f,height=g,image=h,case1=i)
		data.save()
		return redirect("/d_missing/")
	else:
		if request.session.has_key('admin'):
			email = request.session['admin']
			return render(request,"template/missing.html", {"usernames" : email})
		else:
			return redirect('/login/')
def d_missing(request):
	if request.session.has_key('admin'):
		email = request.session['admin']
		data=Addmissing.objects.all()
		return render(request,"template/viewmissing.html", {"usernames" : email,"alldata":data})
	else:
		return redirect('/login/')
def delete_missing(request,pk):
	id=pk
	Addmissing.objects.filter(p_id=id).delete()
	return redirect("/d_missing/")
def wanted(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.POST['t5']
		f=request.POST['t6']
		g=request.POST['t7']
		h=request.FILES['t8']
		i=request.POST['t9']
		j=request.POST['t51']
		data=Addwanted(name=a,age=b, sex=c, place=d, date=e,cmp1=f,height=g,image=h,case1=i,type1=j)
		data.save()
		return redirect("/d_wanted/")
	else:
		if request.session.has_key('admin'):
			email = request.session['admin']
			return render(request,"template/wanted.html", {"usernames" : email})
		else:
			return redirect('/login/')

def d_wanted(request):
	if request.session.has_key('admin'):
		email = request.session['admin']
		data=Addwanted.objects.all()
		return render(request,"template/viewwanted.html", {"usernames" : email,"alldata":data})
	else:
		return redirect('/login/')

def delete_wanted(request,pk):
	id=pk
	Addwanted.objects.filter(p_id=id).delete()
	return redirect("/d_wanted/")
def fir(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.POST['t5']
		f=request.POST['t6']
		g=request.POST['t7']
		h=request.FILES['t8']
		i=request.POST['t9']
		j=request.POST['t10']
		data=Addfir(name=a,fname=b, sex=c, place=d, date=e,time=f,iproof=g,image=h,case1=i,address=j)
		data.save()
		return redirect("/d_fir/")
	else:
		if request.session.has_key('admin'):
			email = request.session['admin']
			return render(request,"template/fir.html", {"usernames" : email})
		else:
			return redirect('/login/')

def d_fir(request):
	if request.session.has_key('admin'):
		email = request.session['admin']
		data=Addfir.objects.all()
		return render(request,"template/viewfir.html", {"usernames" : email,"alldata":data})
	else:
		return redirect('/login/')

def delete_fir(request,pk):
	id=pk
	Addfir.objects.filter(p_id=id).delete()
	return redirect("/d_fir/")
def register(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.POST['t5']
		f=request.FILES['t6']
		g=request.POST['t7']
		data=Addregister(name=a,name2=b, sex=c, type1=d, occ=e,image=f,address=g)
		data.save()
		return redirect("/d_register/")
	else:
		if request.session.has_key('admin'):
			email = request.session['admin']
			return render(request,"template/register.html", {"usernames" : email})
		else:
			return redirect('/login/')

def d_register(request):
	if request.session.has_key('admin'):
		email = request.session['admin']
		data=Addregister.objects.all()
		return render(request,"template/viewregister.html", {"usernames" : email,"alldata":data})
	else:
		return redirect('/login/')

def delete_register(request,pk):
	id=pk
	Addregister.objects.filter(p_id=id).delete()
	return redirect("/d_register/")
def history(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.POST['t5']
		data=Addhistory(p_no=a,type1=b, date=c, place=d, case1=e)
		data.save()
		return redirect("/d_history/")
	else:
		if request.session.has_key('admin'):
			email = request.session['admin']
			return render(request,"template/history.html", {"usernames" : email})
		else:
			return redirect('/login/')

def d_history(request):
	if request.session.has_key('admin'):
		email = request.session['admin']
		data=Addhistory.objects.all()
		return render(request,"template/viewhistory.html", {"usernames" : email,"alldata":data})
	else:
		return redirect('/login/')

def delete_history(request,pk):
	id=pk
	Addhistory.objects.filter(p_id=id).delete()
	return redirect("/d_history/")
def user(request):
	if request.session.has_key('email'):
		email = request.session['email']
		data=Newuser.objects.filter(email=email).all()
		return render(request,"template/user.html", {"usernames" : data})
	else:
		return redirect('/login/')
def editprofile(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.POST['t5']
		f=request.POST['t6']
		Newuser.objects.filter(email=d).update(name=a,pwd=b, no=c, pincode=e,address=f)
		return redirect("/user/")
	else:
		redirect('/index/')
def u_complaint(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.POST['t5']
		f=request.POST['t6']
		data=Addcom2(name=a,email=b, no=c, type1=d,date=e, case1=f,rpy='PENDING')
		data.save()
		return redirect("/s_complaint/")
	else:
		if request.session.has_key('email'):
			email = request.session['email']
			data=Newuser.objects.filter(email=email).all()
			return render(request,"template/u_complaint.html", {"usernames" : data})
		else:
			return redirect('/login/')
def s_complaint(request):
	if request.session.has_key('email'):
		email = request.session['email']
		data=Addcom2.objects.filter(email=email).all()
		return render(request,"template/s_complaint.html", {"alldata" : data})
	else:
		return redirect('/login/')
def delete_cmp(request,pk):
	id=pk
	Addcom2.objects.filter(p_id=id).delete()
	if request.session.has_key('email'):
		return redirect("/s_complaint/")
	if request.session.has_key('admin'):
		return redirect("/user_complaint/")
def u_crime(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.POST['t5']
		f=request.POST['t6']
		data=Addcrime(name=a,email=b, no=c, suspect=d,date=e, case1=f,rpy='PENDING')
		data.save()
		return redirect("/s_crime/")
	else:
		if request.session.has_key('email'):
			email = request.session['email']
			data=Newuser.objects.filter(email=email).all()
			return render(request,"template/u_crime.html", {"usernames" : data})
		else:
			return redirect('/login/')
def s_crime(request):
	if request.session.has_key('email'):
		email = request.session['email']
		data=Addcrime.objects.filter(email=email).all()
		return render(request,"template/s_crime.html", {"alldata" : data})
	else:
		return redirect('/login/')
def delete_crime(request,pk):
	id=pk
	Addcrime.objects.filter(p_id=id).delete()
	if request.session.has_key('email'):
		return redirect("/s_crime/")
	if request.session.has_key('admin'):
		return redirect("user_crime/")
def u_message(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t5']
		e=request.POST['t6']
		data=Addmessage(name=a,email=b, no=c, type1=d,msg=e,rpy='PENDING')
		data.save()
		return redirect("/s_message/")
	else:
		if request.session.has_key('email'):
			email = request.session['email']
			data=Newuser.objects.filter(email=email).all()
			return render(request,"template/u_message.html", {"usernames" : data})
		else:
			return redirect('/login/')
def s_message(request):
	if request.session.has_key('email'):
		email = request.session['email']
		data=Addmessage.objects.filter(email=email).all()
		return render(request,"template/s_message.html", {"alldata" : data})
	else:
		return redirect('/login/')
def delete_message(request,pk):
	id=pk
	Addmessage.objects.filter(p_id=id).delete()
	if request.session.has_key('email'):
		return redirect("/s_message/")
	if request.session.has_key('admin'):
		return redirect("/user_message/")

def s_news(request):
	if request.session.has_key('email'):
		email = request.session['email']
		data=Addnews.objects.all()
		return render(request,"template/viewnews2.html", {"usernames" : email,"alldata":data})
	else:
		return redirect('/login/')
def s_missing(request):
	if request.session.has_key('email'):
		email = request.session['email']
		data=Addmissing.objects.all()
		return render(request,"template/viewmissing2.html", {"usernames" : email,"alldata":data})
	else:
		return redirect('/login/')
def s_wanted(request):
	if request.session.has_key('email'):
		email = request.session['email']
		data=Addwanted.objects.all()
		return render(request,"template/viewwanted2.html", {"usernames" : email,"alldata":data})
	else:
		return redirect('/login/')
def s_fir(request):
	if request.session.has_key('email'):
		email = request.session['email']
		data=Addfir.objects.all()
		return render(request,"template/viewfir2.html", {"usernames" : email,"alldata":data})
	else:
		return redirect('/login/')
def s_register(request):
	if request.session.has_key('email'):
		email = request.session['email']
		data=Addregister.objects.all()
		return render(request,"template/viewregister2.html", {"usernames" : email,"alldata":data})
	else:
		return redirect('/login/')
def s_history(request):
	if request.session.has_key('email'):
		email = request.session['email']
		data=Addhistory.objects.all()
		return render(request,"template/viewhistory2.html", {"usernames" : email,"alldata":data})
	else:
		return redirect('/login/')
def logout(request):
	if request.session.has_key('email'):
		del request.session['email']
	if request.session.has_key('admin'):
		del request.session['admin']
	return redirect("/login/")
def user_complaint(request):
	if request.session.has_key('admin'):
		email = request.session['admin']
		data=Addcom2.objects.all()
		return render(request,"template/user_complaint.html", {"alldata" : data})
	else:
		return redirect('/login/')
def user_crime(request):
	if request.session.has_key('admin'):
		email = request.session['admin']
		data=Addcrime.objects.all()
		return render(request,"template/user_crime.html", {"alldata" : data})
	else:
		return redirect('/login/')
def user_message(request):
	if request.session.has_key('admin'):
		email = request.session['admin']
		data=Addmessage.objects.all()
		return render(request,"template/user_message.html", {"alldata" : data})
	else:
		return redirect('/login/')
def cmp_rpy(request,pk):
	if request.session.has_key('admin'):
		email = request.session['admin']
		id=pk
		return render(request,"template/cmp_rpy.html", {"id":id})
def crime_rpy(request,pk):
	if request.session.has_key('admin'):
		email = request.session['admin']
		id=pk
		return render(request,"template/crime_rpy.html", {"id":id})
def msg_rpy(request,pk):
	if request.session.has_key('admin'):
		email = request.session['admin']
		id=pk
		return render(request,"template/msg_rpy.html", {"id":id})
def cmp_reply(request):
	if request.session.has_key('admin'):
		if request.method == "POST":
			id1=request.POST['t1']
			rpy=request.POST['t6']
			email = request.session['admin']
			data=Addcom2.objects.filter(p_id=id1).update(rpy=rpy)
			return redirect('/user_complaint/')
		else:
			return redirect('/user_complaint/')
	return redirect('/login/')
def crime_reply(request):
	if request.session.has_key('admin'):
		if request.method == "POST":
			id1=request.POST['t1']
			rpy=request.POST['t6']
			email = request.session['admin']
			data=Addcrime.objects.filter(p_id=id1).update(rpy=rpy)
			return redirect('/user_crime/')
		else:
			return redirect('/user_crime/')
	return redirect('/login/')
def msg_reply(request):
	if request.session.has_key('admin'):
		if request.method == "POST":
			id1=request.POST['t1']
			rpy=request.POST['t6']
			email = request.session['admin']
			data=Addmessage.objects.filter(p_id=id1).update(rpy=rpy)
			return redirect('/user_message/')
		else:
			return redirect('/user_message/')
	return redirect('/login/')	
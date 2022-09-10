from django.db import models
class Newuser(models.Model):
	p_id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	pwd=models.CharField(max_length=100)
	no=models.CharField(max_length=100)
	pincode=models.CharField(max_length=100)
	img= models.ImageField(upload_to = 'pictures/')
	address=models.TextField(max_length=500)
	def __str__(self):
		return self.name
class Addnews(models.Model):
	p_id = models.AutoField(primary_key=True)
	title=models.CharField(max_length=100)
	date=models.CharField(max_length=100)
	time=models.CharField(max_length=100)
	place=models.CharField(max_length=100)
	matter=models.TextField(max_length=2000)
	def __str__(self):
		return self.title
class Addmissing(models.Model):
	p_id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	age=models.CharField(max_length=100)
	sex=models.CharField(max_length=100)
	place=models.CharField(max_length=100)
	date=models.CharField(max_length=100)
	cmp1= models.TextField(max_length=500)
	height=models.TextField(max_length=500)
	image=models.ImageField(upload_to = 'missing/')
	case1=models.TextField(max_length=500)
	def __str__(self):
		return self.name
class Addwanted(models.Model):
	p_id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	age=models.CharField(max_length=100)
	sex=models.CharField(max_length=100)
	place=models.CharField(max_length=100)
	date=models.CharField(max_length=100)
	cmp1= models.TextField(max_length=500)
	height=models.TextField(max_length=500)
	image=models.ImageField(upload_to = 'missing/')
	case1=models.TextField(max_length=500)
	type1=models.CharField(max_length=500)
	def __str__(self):
		return self.name
class Addfir(models.Model):
	p_id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	fname=models.CharField(max_length=100)
	sex=models.CharField(max_length=100)
	place=models.CharField(max_length=100)
	date=models.CharField(max_length=100)
	time=models.CharField(max_length=100)
	iproof=models.TextField(max_length=500)
	image=models.ImageField(upload_to = 'fir/')
	case1=models.TextField(max_length=500)
	address=models.CharField(max_length=100)
	def __str__(self):
		return self.name
class Addregister(models.Model):
	p_id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	name2=models.CharField(max_length=100)
	sex=models.CharField(max_length=100)
	type1=models.CharField(max_length=100)
	occ=models.CharField(max_length=100)
	image=models.ImageField(upload_to = 'register/')
	address=models.CharField(max_length=100)
	def __str__(self):
		return self.name
class Addhistory(models.Model):
	p_id = models.AutoField(primary_key=True)
	p_no=models.CharField(max_length=100)
	type1=models.CharField(max_length=100)
	date=models.CharField(max_length=100)
	place=models.CharField(max_length=100)
	case1=models.TextField(max_length=100)
	def __str__(self):
		return self.name
class Addcom2(models.Model):
	p_id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	no=models.CharField(max_length=100)
	type1=models.CharField(max_length=100)
	date=models.CharField(max_length=100)
	case1=models.TextField(max_length=500)
	rpy=models.TextField(max_length=500)
	def __str__(self):
		return self.name
class Addcrime(models.Model):
	p_id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	no=models.CharField(max_length=100)
	suspect=models.CharField(max_length=100)
	date=models.CharField(max_length=100)
	case1=models.TextField(max_length=500)
	rpy=models.TextField(max_length=500)
	def __str__(self):
		return self.name
class Addmessage(models.Model):
	p_id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	no=models.CharField(max_length=100)
	type1=models.CharField(max_length=100)
	msg=models.TextField(max_length=500)
	rpy=models.TextField(max_length=500)
	def __str__(self):
		return self.name

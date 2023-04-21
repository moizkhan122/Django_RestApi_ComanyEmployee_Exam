from django.db import models

# Create your models here.

#company model here
class CompanyModel(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50) 
    about=models.TextField()
    type=models.CharField(max_length=100,choices=
                            (('IT','IT'),
                             ('Non IT','Non IT'),
                             ('Phone Mobile','Phone Mobile')
                             ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self) :
        return self.name + ' --- ' +self.location

#Employee Model
class EmployeeModel(models.Model):
    #mployee_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)  
    about=models.TextField()
    position=models.CharField(max_length=50,choices=
                            (('Manager','manager'),
                             ('Software Developer','sd'),
                             ('Project Leader','pl')
                             ))
    
    #make a link between CompanyModel and Employee Model
    company = models.ForeignKey(CompanyModel,on_delete=models.CASCADE)
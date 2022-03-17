from django.db import models
from django.contrib.auth.models import User
from datetime import date

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100,choices=(("Student","Student"),("Tutor","Tutor")))
    profile = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    study_level = models.CharField(max_length=100,null=True)
    assignment_reference_style = models.CharField(max_length=20,null=True)
    

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'User_Detail'
        verbose_name_plural = 'User Details'
        
        
    def update(self,*args,**kwargs):
        return None
        

class Orders(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    order_id = models.CharField(unique=True,max_length=20,null=True,blank=True)
    subject = models.CharField(max_length=20)
    desc = models.CharField(max_length=500,null=True,blank=True)
    deadline = models.DateTimeField()
    assignment = models.FileField(null=True,blank=True)
    duration = models.CharField(max_length=100,null=True,blank=True)
    CHOICES = (
        ('Awaiting Confirmation','Awaiting Confirmation'),
        ('Order Confirmed','Order Confirmed'),
        ('Payment Done','Payment Done'),
        ('Order Rejected','Order Rejected'),
        ('Assignment In Progress','Assignment In Progress'),
        ('Review Your Assignment','Review Your Assignment'),
        ('Assignment Under Revision','Assignment Under Revision'),
        ('Assignment Completed','Assignment Completed'),
        
    )
    status = models.CharField(max_length=100,choices=CHOICES)
    submission_date = models.DateField(default=date.today())
    assigned = models.BooleanField(default=False)
    reference_material = models.ImageField(null=True,blank=True)
    amount = models.IntegerField(default=0)
    assignment_completed_file = models.FileField()

    def __str__(self):
        return self.order_id
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
class LabOrders(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    order_id = models.CharField(unique=True,null=True,blank=True,max_length=20)
    deadline = models.DateTimeField()
    subject = models.CharField(max_length=20)
    lab_manual = models.FileField(null=True,blank=True)
    lab_data = models.FileField(null=True,blank=True)
    report_guidline = models.FileField(null=True,blank=True)
    reference_material = models.FileField(null=True,blank=True)
    CHOICES = (
        ('Awaiting Confirmation','Awaiting Confirmation'),
        ('Order Confirmed','Order Confirmed'),
        ('Order Rejected','Order Rejected'),
        ('Assignment In Progress','Assignment In Progress'),
        ('Review Your Assignment','Review Your Assignment'),
        ('Assignment Under Revision','Assignment Under Revision'),
        ('Assignment Completed','Assignment Completed'),
    )
    status = models.CharField(max_length=100,choices=CHOICES)
    submission_date = models.DateField(default=date.today())
    assigned = models.BooleanField(default=False)
    amount = models.IntegerField(default=0)
    
    def __str__(self):
        return self.order_id


            
class TutorRegister(models.Model):
    tutor = models.OneToOneField(User, on_delete=models.CASCADE)
    unique_id = models.CharField(unique=True,null=True,blank=True,max_length=20)
    name = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=13,null=True,blank=True)
    state = models.CharField(max_length=50,blank=True,null=True)
    city = models.CharField(max_length=60,blank=True,null=True)
    pin = models.IntegerField(blank=True,null=True)
    qualification_level = models.CharField(max_length=100)
    degree = models.CharField(max_length=100,blank=True,null=True)
    branch = models.CharField(max_length=100,blank=True,null=True)
    college = models.CharField(max_length=200,blank=True,null=True)
    college_id = models.FileField(null=True,blank=True)
    subject = models.CharField(max_length=40)


    def __str__(self):
        return str(self.unique_id)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Tutor Register'
        verbose_name_plural = 'Tutor Registers'

class TutorSolvedAssignment(models.Model):
    tutor = models.ForeignKey(TutorRegister,on_delete=models.CASCADE)
    order =  models.ForeignKey(Orders,on_delete=models.PROTECT,primary_key=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=30,choices=(('Pending','Pending'),('Completed','Completed')),default='Pending')

    def __str__(self):
        return self.tutor.tutor.email

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Tutor Solved Assignment'
        verbose_name_plural = 'Tutor Solved Assignments'

class TutorSolvedLabs(models.Model):
    tutor = models.ForeignKey(TutorRegister,on_delete=models.CASCADE)
    labs =  models.ForeignKey(LabOrders,on_delete=models.PROTECT,primary_key=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=30,choices=(('Pending','Pending'),('Completed','Completed')),default='Pending')

    def __str__(self):
        return self.tutor.tutor.email

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Tutor Solved lab'
        verbose_name_plural = 'Tutor Solved labs'
class TutorAccount(models.Model):
    tutor = models.OneToOneField(TutorRegister,on_delete=models.CASCADE)
    pan_number = models.CharField(max_length=20,null=True,blank=True)
    name_on_pan = models.CharField(max_length=100,null=True,blank=True)
    name_in_account = models.CharField(max_length=100,null=True,blank=True)
    account_number=  models.CharField(max_length=20,null=True,blank=True)
    ifsc = models.CharField(max_length=20,null=True,blank=True)


    def __str__(self):
        return self.tutor.tutor.username

        
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Account Detail'
        verbose_name_plural = 'Account Details'

class TutorPaymenyDetails(models.Model):
    tutor = models.ForeignKey(TutorRegister,on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=10,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    amount = models.IntegerField(null=True,blank=True)
    account = models.CharField(max_length=10 , null=True,blank=True)
    tds = models.CharField(max_length=4,null=True,blank=True)
    status = models.CharField(max_length=4,null=True,blank=True)

    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Tutor Payment Detail'
        verbose_name_plural = 'Tutor Payment Details'
        
    def __str__(self):
        return self.tutor.tutor.email

class TutorEarnedDetail(models.Model):
    tutor = models.ForeignKey(TutorRegister,on_delete=models.CASCADE)
    description = models.CharField(max_length=40,null=True,blank=True)
    time = models.TimeField(null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    amount = models.IntegerField(null=True,blank=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Tutor Earned Detail'
        verbose_name_plural = 'Tutor Earned Details'

    def __str__(self):
        return self.tutor.tutor.email

    
class TutorBalance(models.Model):
    balance = models.IntegerField()
    tutor = models.OneToOneField(TutorRegister,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tutor.tutor.email
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Balance'
        verbose_name_plural = 'Balances'
        
class Questions(models.Model):
    question = models.FileField()
    subject = models.CharField(max_length=100,choices=(('Physics','Physics'),('Maths','Maths'),('Essay Writing','Essay Writing'),
                                                       ('Chemistry','Chemistry'),('Accounting','Accounting'),
                                                       ('Economics','Economics'),('Management','Management'),
                        ('Biology','Biology'),('Chemical Engineering','Chemical Engineering'),
                        ('Computer Science','Computer Science'),('Nursing','Nursing'),
                        ('Electrical','Electrical'),('Mechanical','Mechanical'),
                        ('Finance','Finance'),('Civil Engineering','Civil Engineering')))
    def __str__(self):
        return self.subject

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

        
class Reviews(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    rating = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
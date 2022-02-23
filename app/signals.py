from gettext import install
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.dispatch import receiver
from django.db.models.signals import pre_save,pre_delete,post_save,post_delete
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.core import mail
from decouple import config
from app.models import Orders, TutorRegister


@receiver(pre_save,sender=User)
def presaveSignal(sender,instance,**kwargs):
    if instance.id != None:
        prev = User.objects.get(id=instance.id)
        if prev.is_active==False:
            if instance.is_active==True:
                c = {
                    'username':instance.username,
                    'email':instance.email,
                }
                email=instance.email
                email_msg = render_to_string('test_pass.txt',c)
                connection = mail.get_connection(backend='django.core.mail.backends.smtp.EmailBackend',host='smtp.hostinger.com',
                                                 use_tls=True,port=587,username='tutors@tutorchamps.com',password=config('tutorPassword'))
                connection.open()
                email = EmailMessage(subject='Best of luck for next time',body=email_msg,from_email='tutors@tutorchamps.com',to=[email])
                connection.send_messages([email])
                connection.close()


@receiver(post_delete,sender=TutorRegister)
def predeleteSignal(sender,instance,**kwargs):
    user = instance.tutor
    email = user.email
    username = user.username
    
    c = {
        'useranme':username,
        'email':email,
    }
    
    email_msg = render_to_string('test_fail.txt',c)
    connection = mail.get_connection(backend='django.core.mail.backends.smtp.EmailBackend',host='smtp.hostinger.com',
                                     use_tls=True,port=587,username='tutors@tutorchamps.com',password=config('tutorPassword'))
    connection.open()
    email = EmailMessage(subject='Best of luck for next time',body=email_msg,from_email='tutors@tutorchamps.com',to=[email])
    connection.send_messages([email])
    connection.close()
    
    
@receiver(post_save,sender=Orders)
def mailforOrder(sender,instance,created,**kwargs):
    if created:
        user = instance.user
        email = user.email
        orderId = instance.order_id
        c = {
            'id':orderId,
            'username':user.username,
        }
        content = render_to_string('order.txt',c)
        email = EmailMessage(subject="some subject",body=content,from_email='help@tutorchamps.com',to=[email])
        email.send(fail_silently=True)


@receiver(pre_save,sender=Orders)
def statusUpdated(sender,instance,**kwargs):
    c = {
        'id':instance.order_id,
    }
    user = instance.user
    email = user.email
    if instance.id != None:
        prevorder = Orders.objects.get(id=instance.id)
        if prevorder.status != instance.status:
            if instance.status =='Assignment Completed':
                content = render_to_string('comp_assignment.txt',c)
                email = EmailMessage(subject="subject",body=content,from_email='help@tutorchamps.com',to=[email])
                email.send()
            if instance.status =='Order Rejected':
                content = render_to_string('comp_assignment.txt',c)
                email = EmailMessage(subject="subject",body=content,from_email='help@tutorchamps.com',to=[email])
                email.send()
            if instance.status =='Order Confimed':
                content = render_to_string('comp_assignment.txt',c)
                email = EmailMessage(subject="subject",body=content,from_email='help@tutorchamps.com',to=[email])
                email.send()
            if instance.status =='Assignment Completed':
                content = render_to_string('comp_assignment.txt',c)
                email = EmailMessage(subject="subject",body=content,from_email='help@tutorchamps.com',to=[email])
                email.send()


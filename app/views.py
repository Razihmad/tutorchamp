from platform import uname
from decouple import config
import random
from django.contrib.messages.api import error
from django.core import mail
from django.http import JsonResponse, request
from django.http.response import Http404, HttpResponse, HttpResponseBadRequest
from django.http.response import Http404, HttpResponse
from app.models import LabOrders, Questions, Reviews, TutorEarnedDetail, TutorPaymenyDetails, TutorSolvedAssignment, TutorSolvedLabs, UserDetails, Orders, TutorRegister, TutorAccount,TutorBalance
from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import message, send_mail, BadHeaderError
from django.template.loader import render_to_string
import string
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.core.mail import EmailMessage
from django_chatter.models import Room
from app.serializers import LabSerializers, OrderSerializers
from django_chatter.utils import create_room, send_message


def password_reset_request(request):
    if request.method == "POST":
        email = request.POST.get('email')
        data = email.lower()
        associated_users = User.objects.filter(Q(email=data))
        if associated_users.exists():
            for user in associated_users:
                subject = "Password Reset Requested"
                email_template_name = "password_reset_email.txt"
                c = {
                    "email": user.email,
                    'domain': '127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                }
                email = render_to_string(email_template_name, c)
                connection = mail.get_connection(backend='django.core.mail.backends.smtp.EmailBackend',host='smtp.gmail.com',
                                         use_tls=True,port=587,username='admin@tutorchamps.com',password=config('adminPassword'))
                connection.open()
                try:
                    email = EmailMessage(subject=subject, body=email, from_email='TutorChamps Admin <admin@tutorchamps.com>',
                              to=[user.email])
                    connection.send_messages([email])
                    connection.close()
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                msg = {"status":"success","message":"We've emailed you instructions for setting your password, if an account exists with the email you entered. You should receive them shortly."+
                       "If you don't receive an email, please make sure you've entered the address you registered with, and check your spam folder."}
                return JsonResponse(data=msg)

    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password_reset.html", context={"password_reset_form": password_reset_form})


def home(request):
    if request.user.is_authenticated:
        return redirect("old-user")
    return render(request, 'index.html')


def blog(requset):
    return render(requset, 'blog.html')


def homework(request):
    return render(request, 'online-homework-help.html')


def assignment(request):
    return render(request, 'online-assignment-help.html')


def features(request):
    return render(request, 'features.html')


def reviews(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            content = request.POST.get('content')
            rating = int(request.POST.get('rating'))
            r = '' 
            for i in range(1,rating+1):
                r += str(i)
            user = request.user
            Reviews(user=user,content=content,rating=r).save()
        else:
            messages.info(request,'Please Login First')
            return redirect('reviews')
    reviews = Reviews.objects.all()
    return render(request, 'reviews.html',{'reviews':reviews})


def about(request):
    return render(request, 'about.html')

def essay(request):
    return render(request, 'essay.html')


def live(request):
    return render(request, 'live-session.html')


def course(request):
    return render(request, 'coursework.html')


def case(request):
    return render(request, 'case-study.html')


def dissert(request):
    return render(request, 'dissertation.html')


def project(request):
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=20))
    if request.method == "POST":
        subject = request.POST.get('subject')
        deadline = request.POST.get('deadline')
        lab_manual = request.FILES['lab_manual']
        report_guidline = request.FILES['report_guidline']
        lab_data = request.FILES['lab_data']
        reference_material = request.FILES['reference_material']
        try:
            user = request.user
            uname = user.username
            user = User.objects.get(username=uname)
            lab = LabOrders(user=user, subject=subject, lab_data=lab_data, lab_manual=lab_manual, report_guidline=report_guidline,
                   deadline=deadline, reference_material=reference_material,status='Awaiting Confirmation',assigned=False).save()
            id = lab.pk
            id +=1000
            lab.order_id = f'TC-lab-{id}'
            lab.save()
            return redirect('old-user')
        except:
            request.session['session_key'] = res
            print(res)
            new_user = User(username=res,email=res)
            new_user.save()
            labOrder = LabOrders(user=new_user, subject=subject, lab_data=lab_data, lab_manual=lab_manual, report_guidline=report_guidline,
                   deadline=deadline, reference_material=reference_material,status='Awaiting Confirmation',assigned=False)
            labOrder.save()
            id = labOrder.pk
            id += 1000
            labOrder.order_id = f'TC-lab-{id}'
            labOrder.save()
            return redirect('signup')
    return render(request, 'project.html')


def physics(request):
    return render(request, 'physics.html')


def chemistry(request):
    return render(request, 'chemistry.html')


def math(request):
    return render(request, 'math.html')


def english(request):
    return render(request, 'english.html')


def science(request):
    return render(request, 'science.html')


def programming(request):
    return render(request, 'programming.html')


def bio(request):
    return render(request, 'bio.html')


def engineer(request):
    return render(request, 'engineer.html')


def cs(request):
    return render(request, 'cs.html')


def static_assignment(request):
    return render(request, 'static.html')


def accounting(request):
    return render(request, 'accounting.html')


def eco(request):
    return render(request, 'ecco.html')


def nursing(request):
    return render(request, 'nursing.html')


def management(request):
    return render(request, 'management.html')

# assignment orders from the dashboard
@login_required(login_url='/login/')
def dashboard_old(request, **kwargs):
    user = request.user
    user_detail = UserDetails.objects.get_or_create(user=user)
    user_detail = user_detail[0]
    if user_detail.user_type=="Tutor":
        return redirect("tutor-dashboard")
    
    details = Orders.objects.filter(user=user)
    labs = LabOrders.objects.filter(user=user)
    if request.method == 'POST':
        desc = request.POST.get('desc')
        reference_material = request.FILES['reference_material']
        assignment = request.FILES['assignment']
        deadline = request.POST.get('deadline')
        subject = request.POST.get('subject')
        order = Orders(user=user, status='Awaiting Confirmation', desc=desc,reference_material=reference_material,assignment=assignment,
             deadline=deadline,subject=subject)
        order.save()
        id = order.pk
        id += 1000
        order.order_id = f'TC-HW-{id}'
        order.save()
        print("Order successful, order id : {}".format(order.order_id))
        send_message(request, "Order successful, order id : {}".format(order.order_id))
        c = {
            'user':user.username,
            'order_id':order.order_id,
            'subject':order.subject,
            'deadline':deadline,
            
        }
        email = user.email
        order_id = order.order_id
        email_msg = render_to_string('order.txt',c)
        mail = EmailMessage(subject=f'Order Created - {order_id}',body=email_msg,from_email='TutorChamps Student Support <help@tutorchamps.com>',to=[email,'help@tutorchamps.com'])
        mail.send()
        serializers = OrderSerializers(order)
        return JsonResponse(serializers.data)
    print(details)
    _context = {'details': details, 'user': user, 'user_detail': user_detail,'labs':labs, 'ordered': False}
    if "order" in kwargs.keys():
        if kwargs["order"] == "order-successful":
            _context["ordered"] = True
    print(_context["ordered"])
    return render(request, 'dash_board.html', _context)



# lab order from the dashboard
@login_required(login_url='/login/')
def labordes(request):
    user = request.user
    uname= user.username
    user = User.objects.get(username=uname)
    user_detail = UserDetails.objects.get_or_create(user=user)
    user_detail = user_detail[0]
    if request.method == 'POST':
        lab_manual = request.FILES['lab_manual']
        report_guidline = request.FILES['report_guideline']
        lab_data = request.FILES['lab_data']
        reference_material = request.FILES['reference_material']
        deadline = request.POST.get('deadline')
        subject = request.POST.get('subject')
        lab = LabOrders(user=user,reference_material=reference_material,
             deadline=deadline,subject=subject,lab_manual=lab_manual,report_guidline=report_guidline,
             lab_data=lab_data,status='Awaiting Confirmation',assigned=False)
        lab.save()
        id = lab.pk
        id +=1000
        lab.order_id = f'TC-lab-{id}'
        lab.save()
        c = {
            'user':user.username,
            'order_id':lab.order_id,
            'subject':lab.subject,
            'deadline':deadline,
            
        }
        email = user.email
        order_id = lab.order_id
        email_msg = render_to_string('order.txt',c)
        mail = EmailMessage(subject=f'Order Created - {order_id}',body=email_msg,from_email='TutorChamps Student Support <help@tutorchamps.com>',to=[email,'help@tutorchamps.com'])
        mail.send()
        serializers = LabSerializers(lab)
        return JsonResponse(serializers.data)
        
        
# live session ordes from the dashboard 
@login_required(login_url='/login/')
def live_session_orders(request):
    user = request.user
    user_detail = UserDetails.objects.get_or_create(user=user)
    user_detail = user_detail[0]
    if request.method == 'POST':
        desc = request.POST.get('desc')
        assignment = request.FILES['assignment']
        deadline = request.POST.get('deadline')
        duration = request.POST.get('Duration')
        subject = request.POST.get('subject')
        reference_material = request.FILES['reference_material']
        order = Orders(user=user, status='Awaiting Confirmation', desc=desc,assignment=assignment,
             deadline=deadline,subject=subject,duration=duration,reference_material=reference_material)
        order.save()
        id = order.pk
        id +=1000
        order.order_id = f'TC-LS-{id}'
        order.save()
        serializers = OrderSerializers(order)
        c = {
            'user':user.username,
            'order_id':order.order_id,
            'subject':order.subject,
            'deadline':deadline,
        }
        email=user.email
        order_id = order.order_id
        email_msg = render_to_string('order.txt',c)
        mail = EmailMessage(subject=f'Order Created - {order_id}',body=email_msg,from_email='TutorChamps Students Support <help@tutorchamps.com>',to=[email,'help@tutorchamps.com'])
        mail.send()
        return JsonResponse(serializers.data)

def signup(request):
    if request.user.is_authenticated:
        return redirect("old-user")
    data = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            User.objects.get(email=email)
            #messages.info(request, 'This email is already registered')
            data = {'status':'error','msg':'This email is already registered'}
            return JsonResponse(data)
        except ObjectDoesNotExist:

            uname = email.replace('@','_')
            user = User(username=uname, email=email)
            user.set_password(password)
            user.save()
            staff = User.objects.filter(groups__name='Students Help')            
            room = create_room(staff)
            room.members.add(user)
            room.save()
            user_detail = UserDetails(user=user,user_type="Student")
            user_detail.save()
            if request.session.get('session_key'):
                username = request.session['session_key']
                unknown_user = User.objects.get(username=username)
                try:
                    laborder = LabOrders.objects.get(user=unknown_user)
                    laborder.user = user
                    laborder.save()
                    c = {
                        'user':user.username,
                        'order_id':laborder.order_id,
                        'subject':laborder.subject,
                        'deadline':laborder.deadline
                        
                    }
                    order_id = laborder.order_id
                    email_msg = render_to_string('order.txt',c)
                    mail = EmailMessage(subject=f'Order Created - {order_id}',body=email_msg,from_email='TutorChamps Student Support <help@tutorchamps.com>',to=[email,'help@tutorchamps.com'])
                    mail.send()
                except:
                    order = Orders.objects.get(user=unknown_user)
                    order.user = user
                    order.save()
                    c = {
                        'user':user.username,
                        'order_id':order.order_id,
                        'subject':order.subject,
                        'deadline':order.deadline
                    }
                    order_id = order.order_id
                    print(order.deadline)
                    email_msg = render_to_string('order.txt',c)
                    mail = EmailMessage(subject=f'Order Created - {order_id}',body=email_msg,from_email='TutorChamps Student Support <help@tutorchamps.com>',to=[email,'help@tutorchamps.com'])
                    mail.send()            
                finally:
                    unknown_user.delete()
                    del request.session['session_key']
                    #messages.success(request, 'you have registered successfully')
                    usr = authenticate(username=uname,password=password)
                    login(request,usr)
                    data = {'status':'ok','msg':'User created successfully'}
                    print("Order successful, order id : {}".format(order.order_id))
                    send_message(request, "Order successful, order id : {}".format(order_id))
                    data['order'] = "YES"
                    #return redirect('new-user-ordered', order="order-successful")
                    return JsonResponse(data)
            else:    
                #messages.success(request, 'you have registered successfully')
                usr = authenticate(username=uname,password=password)
                login(request,usr)
                data = {'status':'ok','msg':'User created successfully'}
                c = {
                    'user':user.username
                }
                email_msg = render_to_string('signup.txt',c)
                mail = EmailMessage(subject='Welcome to TutorChamps',body=email_msg,from_email='TutorChamps Student Support <help@tutorchamps.com>',to=[email])
                mail.send()
                return JsonResponse(data)
            print(usr)
        
    print("here2")
    return render(request, 'signup.html', data)

@login_required(login_url='/login/')
def reset_pass(request):
    if request.method=='POST':
        user = request.user
        username = user.username
        password = request.POST.get('password')
        user.set_password(password)
        user.save()
        u = authenticate(username=username,password=password)
        login(request,u)
        messages.success(request,'Password changes successfully')
        return redirect('old-user')

        
@login_required(login_url='/login/')      
def profile(request):
    if request.method=='POST':
        user = request.user
        uname= user.username
        user = User.objects.get(username=uname)
        name = request.POST.get('nae')
        phone = request.POST.get('if-phone')
        email = request.POST.get('email')
        college = request.POST.get('College')
        user.email = email
        user.save()
        user_detail = UserDetails.objects.get_or_create(user=user)
        user_detail = user_detail[0]
        if request.FILES:
            profile = request.FILES['profile']
            user_detail.profile = profile
        user_detail.name = name
        user_detail.phone = phone
        user_detail.study_level = college
        user_detail.save()
        messages.success(request,'Details Updated Successfully')
        return redirect('old-user')


        

def signin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        email = email.lower()
        password = request.POST.get('password')          
        uname = email.replace('@','_')
        print(uname)
        user = authenticate(username=uname, password=password)
        if user:
            new_user = User.objects.get(username=uname)
            #userdetail = UserDetails.objects.get(user=new_user)
            #if userdetail.user_type=="Student":
            if user.is_active:
                login(request, user)
                user = request.user
                detail = UserDetails.objects.get_or_create(user=user)
                if request.session.get('session_key'):
                    username = request.session['session_key']
                    unknown_user = User.objects.get(username=username)
                    try:
                        laborder = LabOrders.objects.get(user=unknown_user)
                        laborder.user = user
                        id = laborder.pk
                        id +=1000
                        laborder.order_id = f'TC-lab-{id}'
                        laborder.save()
                        c = {
                            'user':user.username,
                            'order_id':laborder.order_id,
                            'subject':laborder.subject,
                            'deadline':laborder.deadline,
                        }
                        order_id = laborder.order_id
                        email_msg = render_to_string('order.txt',c)
                        mail = EmailMessage(subject=f'Order Created - {order_id}',body=email_msg,from_email='TutorChamps Student Support <help@tutorchamps.com>',to=[email,'help@tutorchamps.com'])
                        mail.send()  
                    except:
                        order = Orders.objects.get(user=unknown_user)
                        order.user = user
                        order.save()    
                        c = {
                            'user':user.username,
                            'order_id':order.order_id,
                            'subject':order.subject,
                            'deadline':order.deadline,
                        }
                        order_id = order.order_id
                        email_msg = render_to_string('order.txt',c)
                        mail = EmailMessage(subject=f'Order Created - {order_id}',body=email_msg,from_email='TutorChamps Student Support <help@tutorchamps.com>',to=[email,'help@tutorchamps.com'])
                        mail.send()   
                    unknown_user.delete()
                    del request.session['session_key']
                    messages.success(request, f"Welcome Back {email}")
                return redirect('old-user')
            else:
            
                data = {'status':'error','msg':'Your Account has been deactivated'}
                return JsonResponse(data)
            #else:
            #    data = {"status":"error","msg":"Not Allowed"}
            #    return JsonResponse(data)
        else:
            print('no user')
            data = {'status':'error','msg':"Invalid email or password"}
            return JsonResponse(data)
    return render(request, 'login.html')


@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('home')


def onlyorders(request):
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=20))
    if request.method == 'POST':
        subject = request.POST.get('subject')
        desc = request.POST.get('Details')
        deadline = request.POST.get('deadline')
        if request.FILES:
            assignment = request.FILES['files']
        else:
            assignment = None
        try:
            user = request.user
            uname= user.username
            user = User.objects.get(username=uname)
            order = Orders(subject=subject, desc=desc, deadline=deadline,
                   assignment=assignment, user=user, status='Awaiting Confirmation')
            order.save()
            id = order.pk
            id +=1000
            order.order_id = f'TC-HW-{id}'
            order.save()
            return redirect('old-user')
        except:
            request.session['session_key'] = res
            new_user = User(username=res,email=res)
            new_user.save()
            order = Orders(user=new_user,subject=subject,desc=desc,assignment=assignment,deadline=deadline,status='Awaiting Confirmation')
            order.save()
            id = order.pk
            id +=1000
            order.order_id = f'TC-HW-{id}'
            order.save()
            return redirect('signup')


def live_session(request):
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=20))
    b = request.user.is_authenticated
    if request.method == 'POST':
        deadline = request.POST.get('deadline')
        subject = request.POST.get('subject')
        file = request.FILES['files']
        duration = request.POST.get('duration')
        desc = request.POST.get('Details')
        
        if b:
            user = request.user
            order = Orders(deadline=deadline, subject=subject, assignment=file,
                           duration=duration, desc=desc, user=user,status="Awaiting Confirmation")
            order.save()
            id = order.pk
            id += 1000
            order.order_id = f'TC-LS-{id}'
            order.save()
            return redirect('old-user')
        else:
            request.session['session_key'] = res
            new_user = User(username=res,email=res)
            new_user.save()
            print(new_user)
            order = Orders(deadline=deadline,subject=subject,assignment=file,duration=duration,user=new_user,desc=desc,status='Awaiting Confirmation')
            order.save()
            id = order.pk
            id +=1000
            order.order_id = f'TC-LS-{id}'
            order.save()
    return render(request, 'live-session.html')

def tutor_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        email = email.lower()
        qualification_level = request.POST.get('level')
        subject = request.POST.get('subject')
        user = User.objects.get_or_create(username=email)
        password = config('tutorspassword')
        b = user[1]
        user = user[0]
        if b==True:
            user.email=email
            user.first_name=name
            user.save()
            UserDetails(user=user,user_type="Tutor").save()
            user.set_password(password)
            user.is_active = False
            user.save()
            hard = Questions.objects.filter(subject=subject)
            hard = random.choice(hard)
            tutor = TutorRegister(name=name,qualification_level=qualification_level, subject=subject,tutor=user)
            tutor.save()
            id = tutor.pk
            id +=3000
            subject = subject.upper()
            tutor.unique_id = f'{subject[0:3]}-{id}'
            tutor.save()
            c = {
                'user':name
            }
            email_msg = render_to_string('tutor_email.txt',c)
            connection = mail.get_connection(backend='django.core.mail.backends.smtp.EmailBackend',host='smtp.gmail.com',name="TutorChamps",
                                             use_tls=True,port=587,username='tutors@tutorchamps.com',password=config('tutorPassword'))
            connection.open()
            email = EmailMessage(subject='Welcome to TutorChamps || Complete the test',body=email_msg,from_email='TutorChamps Tutors Support <tutors@tutorchamps.com>',to=[email])
            hard = hard.question
            email.attach(hard.name,hard.read())
            connection.send_messages([email])
            connection.close()
            x = TutorBalance(tutor=tutor,balance=0)
            x.save()
            account = TutorAccount(tutor = tutor)
            account.save()
            return redirect(f'/thank-you/{id}/')
        else:
            messages.warning(request, 'already registered')
            return redirect('registration')
    return render(request, 'register.html')

def thanks(request,id):
    return render(request,'thank-you.html')

def tutor_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            new_user = User.objects.get(username=username)
            user_detail = UserDetails.objects.get(user=new_user)
            if user_detail.user_type=="Tutor":
                if user.is_active:
                    login(request, user)
                    return redirect('/tutor/dashboard/')
                else:
                    messages.info(
                        request, 'Your account has been deactivated. Contact the Tutorchamps Team to reactivate your account.')
                    return redirect('tutor')
            else:
                messages.info(request,"not allowed")
                return redirect("tutor")
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('tutor')
    return render(request, 'tutor.html')

def password_reset(request):
    if request.method=='POST':
        user = request.user
        username = user.username
        password = request.POST.get('password')
        confirm_password = request.POST.get('confm_password')
        user.set_password(password)
        user.save()
        u = authenticate(username=username,password=password)
        login(request,u)
        messages.success(request,'Password changes successfully')
        return redirect('tutor-dashboard')

@login_required(login_url='/tutor/')
def tutor_logout(request):
    logout(request)
    return redirect('/tutor/')

    

@login_required(login_url='/tutor/')
def tutor_dashboard(request):
    tutor = request.user
    tutor_register = TutorRegister.objects.get(tutor=tutor)
    subject = tutor_register.subject
    tutor_balance = TutorBalance.objects.get(tutor=tutor_register)
    orders = Orders.objects.filter(subject=subject,assigned=False,status='Order Confirmed')
    if request.method == "POST":
        pan_number = request.POST.get('pan_card')
        name_on_pan = request.POST.get('pan_name')
        name_in_account = request.POST.get('name_in_account')
        account_number = request.POST.get('account_number')
        confirm = request.POST.get('confirm_bank_account')
        ifsc = request.POST.get('ifsc')
        if int(account_number) == int(confirm):
            t = TutorAccount.objects.get(tutor = tutor_register)
            t.pan_number = pan_number
            t.account_number = account_number
            t.name_in_account = name_in_account
            t.name_on_pan = name_on_pan
            t.ifsc = ifsc
            t.save()
        else:
            messages.info(request,'pleaase check the account number')
            return redirect('tutor-dashboard')
    elif tutor_register.phone == None or tutor_register.degree==None:
        return redirect('/tutor_detail/')
    else:
        tutor_account = TutorAccount.objects.get(tutor=tutor_register)
        assignments = TutorSolvedAssignment.objects.filter(tutor=tutor_register)
        labs = TutorSolvedLabs.objects.filter(tutor = tutor_register)
        earned = TutorEarnedDetail.objects.filter(tutor=tutor_register)
        payment_history  = TutorPaymenyDetails.objects.filter(tutor= tutor_register)
        return render(request, 'tutor-dashboard.html',{'tutor_register': tutor_register,'tutor': tutor,'earned':earned,'payment_history':payment_history,
                    'b':tutor_balance.balance,'tutor_account':tutor_account,'assignments':assignments,'labs':labs,'orders':orders })

def tutordashboardtesting(request):
    return render(request,'tutor-dashboard.html')

def thank(request):
    return render(request,'thank-you.html')

@login_required(login_url='/tutor/')    
def interest(request):
    if request.method=="POST":
        user = request.user
        email = user.email
        tutor = TutorRegister.objects.get(tutor=user)
        tutor_id = tutor.unique_id
        order_id = request.POST.get('order_id')
        c = {
                'email':email,
                'tutor_id':tutor_id,
                'order_id':order_id,
            }
        email_msg = render_to_string('tutor_email.txt',c)
        connection = mail.get_connection(backend='django.core.mail.backends.smtp.EmailBackend',host='smtp.gmail.com',name="TutorChamps",
                                          use_tls=True,port=587,username='tutors@tutorchamps.com',password=config('tutorPassword'))
        connection.open()
        email = EmailMessage(subject='tutor interest has com',body=email_msg,from_email='TutorChamps Tutors Support <tutors@tutorchamps.com>',to=['adm.tutorchamps@gmail.com'])
        connection.send_messages([email])
        connection.close()
        data = {'msg':'interest shows successfully'}
        return JsonResponse(data)
            

@login_required(login_url='/tutor/')
def tutor_detail(request):
    tutor = request.user
    if request.method=='POST':
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pin = request.POST.get('pin')
        degree = request.POST.get('degree')
        branch = request.POST.get('branch')
        college = request.POST.get('college')
        college_id = request.FILES['college_id']
        tutor_detail = TutorRegister.objects.get(tutor=tutor)
        tutor_detail.phone = phone
        tutor_detail.college_id = college_id
        tutor_detail.state = state
        tutor_detail.city = city
        tutor_detail.branch = branch
        tutor_detail.pin = pin
        tutor_detail.college = college
        tutor_detail.degree = degree
        tutor_detail.save()
        return redirect('/tutor/dashboard/')
    return render(request,'tutor_detail.html')
    
@login_required(login_url='/tutor/')
def tutor_profile(request):
    tutor = request.user
    tutor_register = TutorRegister.objects.get(tutor=tutor)
    if request.method=='POST':
        name = request.POST.get('nae')
        email = request.POST.get('email')
        phone = request.POST.get('if-phone')
        college = request.POST.get('College')
        if len(name)>0:
            tutor_register.name = name
            tutor_register.save()
        if len(phone)>0:
            tutor_register.phone = phone
            tutor_register.save()
        if len(college)>0:
            tutor_register.college = college
            tutor_register.save()
        if len(email)>0:
            tutor.email = email
            tutor.save()
        return redirect('tutor-dashboard')
        
    

@login_required(login_url='/tutor/')
def withdrawl_money(request):
    tutor = request.user
    tutor_register = TutorRegister.objects.get(tutor=tutor)
    tutor_balance = TutorBalance.objects.get(tutor=tutor_register)
    if request.method == "POST":
        withdrawl = int(request.POST.get('withdrawl'))
        if tutor_balance.balance>=withdrawl:
            tutor_balance.balance -= withdrawl
            tutor_balance.save()
            
            # send email
            return redirect('tutor-dashboard')
        else:
            messages.warning(request,'you dont have enough balance')
            return redirect('tutor-dashboard')


def homework(request):
    return render(request, "online-homework-help.html")


def refund(request):
    return render(request, "refund.html")


def privacy(request):
    return render(request, "privacy.html")


def terms(request):
    return render(request, "terms.html")


def faq(request):
    return render(request, "faq.html")


def finance(request):
    return render(request, "finance.html")

def blog1(request):
    return render(request,'top_scholor.html')
def blog2(request):
    return render(request, 'how_to_do.html')
def blog3(request):
    return render(request, 'informative.html')
def blog4(request):
    return render(request, 'check_out_2.html')
def blog5(request):
    return render(request, 'check_out.html')
def blog6(request):
    return render(request, 'top_research.html')


def asignment_order(request):
    user = request.user
    uname= user.username
    user = User.objects.get(username=uname)
    if request.method=='POST':
        desc = request.POST.get('desc')
        assignment = request.FILES['files']
        subject = request.POST.get('subject')
        deadline = request.POST.get('deadline')
        Orders(user=user,desc=desc,assignment=assignment,subject=subject,deadline=deadline,status='Awaiting Confirmation').save()
        return redirect('old-user')
    
def save_order(request,backend,user,response,*args,**kwargs):
    email = user.email
    print(email)
    if request.session.get('session_key'):
        username = request.session['session_key']
        unknown_user = User.objects.get(username=username)
        try:
            laborder = LabOrders.objects.get(user=unknown_user)
            laborder.user = user
            laborder.save()
        except:
            order = Orders.objects.get(user=unknown_user)
            order.user = user
            id = order.pk
            id += 3000
            order.order_id = f'TC-HW-{id}'
            order.save()         
        unknown_user.delete()
        del request.session['session_key']

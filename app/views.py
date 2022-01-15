from django.contrib.messages.api import error
from django.core import mail
from django.http import request
from django.http.response import Http404, HttpResponse, HttpResponseBadRequest
from django.http.response import Http404, HttpResponse
from app.models import LabOrders, TutorEarnedDetail, TutorPaymenyDetails, TutorSolvedAssignment, TutorSolvedLabs, UserDetails, Orders, TutorRegister, Blog, TutorAccount,TutorBalance
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


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email'].lower()
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
                    try:
                        send_mail(subject, email, 'admin@tutorchamps.com',
                                  [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")

    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password_reset.html", context={"password_reset_form": password_reset_form})


def home(request):
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
    return render(request, 'reviews.html')


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
            LabOrders(user=user, subject=subject, lab_data=lab_data, lab_manual=lab_manual, report_guidline=report_guidline,
                   deadline=deadline, reference_material=reference_material).save()
            return redirect('old-user')
        except:
            if not request.session.session_key:
                request.session.save()
            session_key = request.session.session_key
            request.session['session_key'] = session_key
            new_user = User(username=session_key,email=session_key)
            new_user.save()
            LabOrders(user=new_user, subject=subject, lab_data=lab_data, lab_manual=lab_manual, report_guidline=report_guidline,
                   deadline=deadline, reference_material=reference_material).save()
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
def dashboard_old(request):
    user = request.user
    uname= user.username
    user = User.objects.get(username=uname)
    user_detail = UserDetails.objects.get_or_create(user=user)
    user_detail = user_detail[0]
    details = Orders.objects.filter(user=user)
    if request.method == 'POST':
        desc = request.POST.get('desc')
        reference_material = request.FILES['reference_material']
        assignment = request.FILES['assignment']
        deadline = request.POST.get('deadline')
        subject = request.POST.get('subject')
        Orders(user=user, status='Pending', desc=desc,reference_material=reference_material,assignment=assignment,
             deadline=deadline,subject=subject).save()
        
    return render(request, 'dash_board.html', {'details': details, 'user': user, 'user_detail': user_detail})

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
        LabOrders(user=user,reference_material=reference_material,
             deadline=deadline,subject=subject,lab_manual=lab_manual,report_guidline=report_guidline,
             lab_data=lab_data).save()
        return redirect('old-user')
        
        
# live session ordes from the dashboard 
@login_required(login_url='/login/')
def live_session_orders(request):
    user = request.user
    uname= user.username
    user = User.objects.get(username=uname)
    user_detail = UserDetails.objects.get_or_create(user=user)
    user_detail = user_detail[0]
    if request.method == 'POST':
        desc = request.POST.get('desc')
        assignment = request.FILES['ref_material']
        deadline = request.POST.get('deadline')
        duration = request.POST.get('Duration')
        subject = request.POST.get('subject')
        Orders(user=user, status='Pending', desc=desc,assignment=assignment,
             deadline=deadline,subject=subject,duration=duration).save()
        return redirect('old-user')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            User.objects.get(email=email)
            messages.info(request, 'This email is already registered')
            return redirect('login')
        except ObjectDoesNotExist:
            user = User(username=email, email=email)
            user.set_password(password)
            user.save()
            user_detail = UserDetails(user=user)
            user_detail.save()
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
                    order.save()
                unknown_user.delete()
                del request.session['session_key']
            messages.success(request, 'you have registered successfully')
            usr = authenticate(username=email,password=password)
            login(request,usr)
            return redirect('new-user')

    return render(request, 'signup.html')

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
        user = authenticate(username=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                usr = request.user
                uname= usr.username
                user = User.objects.get(username=uname)
                detail = UserDetails.objects.get_or_create(user=user)
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
                        order.save()
                    unknown_user.delete()
                    del request.session['session_key']
                messages.success(request, f"Welcome Back {email}")
                return redirect('old-user')
            else:
                messages.error(request, "Account is not Active")
                return redirect('home')
        else:
            messages.warning(request, "invalid email or password")
            return redirect('/login/')
    return render(request, 'login.html')


@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('home')


def onlyorders(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        desc = request.POST.get('Details')
        deadline = request.POST.get('deadline')
        assignment = request.FILES['files']
        try:
            user = request.user
            uname= user.username
            user = User.objects.get(username=uname)
            Orders(subject=subject, desc=desc, deadline=deadline,
                   assignment=assignment, user=user, status='Pending').save()
            return redirect('old-user')
        except:
            if not request.session.session_key:
                request.session.save()
            session_key = request.session.session_key
            request.session['session_key'] = session_key
            new_user = User(username=session_key,email=session_key)
            new_user.save()
            Orders(user=new_user,subject=subject,desc=desc,assignment=assignment,deadline=deadline,status='Pending').save()
            return redirect('signup')


def live_session(request):
    if request.method == 'POST':
        deadline = request.POST.get('deadline')
        subject = request.POST.get('subject')
        file = request.FILES['files']
        duration = request.POST.get('duration')
        desc = request.POST.get('Details')
        try:
            user = request.user
            uname= user.username
            user = User.objects.get(username=uname)
            order = Orders(deadline=deadline, subject=subject, assignment=file,
                           duration=duration, desc=desc, user=user,status="Pending")
            order.save()
            return redirect('old-user')
        except:
            if not request.session.session_key:
                request.session.save()

            session_key = request.session.session_key
            request.session['session_key'] = session_key
            new_user = User(username=session_key,email=session_key)
            new_user.save()
            Orders(deadline=deadline,subject=subject,assignment=file,duration=duration,user=new_user,desc=desc,status='Pending').save()
            return redirect('signup')
    return render(request, 'live-session.html')

def tutor_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        email = email.lower()
        qualification_level = request.POST.get('level')
        subject = request.POST.get('subject')
        user = User.objects.get_or_create(username=email,email=email)
        b = user[1]
        user = user[0]
        if b==True:
            tutor = TutorRegister(name=name,qualification_level=qualification_level, subject=subject,tutor=user)
            send_mail(subject='Welcome to the TutorChamps!!',
                      message=f'Dear {email} \n Thanks for contacting TutorChamps! You are at the right place for your requirements.' +
                      ' We are specialists in delivering the best quality assignment within the deadline. ' + 
                      '\n Please use the below link and password to access the dashboard to proceed further  \n Regards, Team TutorChamps',
                      from_email='admin@tutorchamps.com', recipient_list=[email])
            tutor.save()
            x = TutorBalance(tutor=tutor,balance=0)
            x.save()
            TutorAccount(tutor = tutor).save()
            return redirect('tutor')
        else:
            messages.warning(request, 'you already have been registered')
            return redirect('registration')
    return render(request, 'register.html')


def tutor_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('tutor-dashboard')
            else:
                messages.info(
                    request, 'Your account has been deactivated. Contact the Tutorchamps Team to reactivate your account.')
                return redirect('tutor')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('tutor')
    return render(request, 'tutor.html')
   

@login_required(login_url='/tutor/')
def tutor_dashboard(request):
    tutor = request.user
    tutor_register = TutorRegister.objects.get(tutor=tutor)
    tutor_balance = TutorBalance.objects.get(tutor=tutor_register)
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
    if len(tutor_register.phone)>0:
        return render(request,'tutor_detail.html')
    else:
        tutor_account = TutorAccount.objects.get(tutor=tutor_register)
        assignments = TutorSolvedAssignment.objects.filter(tutor=tutor_register)
        labs = TutorSolvedLabs.objects.filter(tutor = tutor_register)
        earned = TutorEarnedDetail.objects.filter(tutor=tutor_register)
        payment_history  = TutorPaymenyDetails.objects.filter(tutor= tutor_register)
        return render(request, 'tutor-dashboard.html',{'tutor_register': tutor_register,'tutor': tutor,'earned':earned,'payment_history':payment_history,
                    'b':tutor_balance.balance,'tutor_account':tutor_account,'assignments':assignments,'labs':labs })
    
    
# @login_required(login_url='/tutor/')
def tutor_detail(request):
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
        Orders(user=user,desc=desc,assignment=assignment,subject=subject,deadline=deadline,status='Pending').save()
        return redirect('old-user')
    
        
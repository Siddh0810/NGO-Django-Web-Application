from django.shortcuts import render,redirect
from .models import teamMember,Donation,Review
from django.core.mail import send_mail
# Create your views here.
def home(request):
    data = Donation.objects.all()
    review = Review.objects.all()
    total_sum = 0
    for item in data:
        total_sum += item.Amount
    teammember=teamMember.objects.count()
    video="https://www.instagram.com/reel/ChmwDEwp8_w/?igshid=MTc4MmM1YmI2Ng==="
    return render(request,'home.html',{'teammember':teammember,"video":video,'sum':total_sum,'review':review})

def about(request):
    return render(request,'aboutus.html')


def team(request):
    return render(request,'team.html')

    
def join(request):
   if request.method=="POST":
        name=request.POST.get('Name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        address=request.POST.get('address')
        birthday=request.POST.get('bday')
        data = teamMember(Name=name,Mobile=mobile,Email=email,Address=address,BirthDate=birthday) 
        data.save()
        # send_email_to_client()
        subject = 'New Join Us Submission'
        message = f'Name: {name}\nEmail: {email}\nMobile no. : {mobile}\nAddress: {address}\nBirthday: {birthday}'
        from_email = {email}  # Replace with your Gmail email
        recipient_list = ['saathigroup29@gmail.com']
        message1=f"Thank you for join Sathi Group"# Replace with your email or a list of recipients
        send_mail(subject, message, from_email, recipient_list)
        send_mail(subject, message1, recipient_list[0],from_email)
        return redirect('home')
   else:
        return render(request, 'join.html')
    
    
def Donate(request):
    if request.method=="POST":
        name=request.POST.get('Name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        address=request.POST.get('address')
        amount=request.POST.get('amount')
        data1 = Donation(Name=name,Mobile=mobile,Email=email,Address=address,Amount=amount) 
        data1.save()
        subject = 'New Join Us Submission'
        message = f'Name: {name}\nEmail: {email}\nMobile no. : {mobile}\nAddress: {address}\nAmout: {amount}'
        from_email = {email}  # Replace with your Gmail email
        recipient_list = ['saathigroup29@gmail.com']
        message1=f"Thank you for join Sathi Group"# Replace with your email or a list of recipients
        send_mail(subject, message, from_email, recipient_list)
        send_mail(subject, message1, recipient_list[0],from_email)
        return redirect('home')
    else:
        return render(request,'donation.html')

def Suggest(request):
    if request.method == "POST":
        email=request.POST.get('email')
        name = request.POST.get('username')
        review=request.POST.get('review')
        data2 = Review(Name=name,Email=email,Text=review) 
        data2.save()
        return redirect('home')
    return render(request,'home.html')
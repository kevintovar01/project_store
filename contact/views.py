from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage

def contact(request):
    form_contact = ContactForm()

    

    if request.method=='POST':
        form_contact=ContactForm(data=request.POST)
        if form_contact.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            content = request.POST.get("content")

            email=EmailMessage('mensaje desde App django',
            f'el usuario con nombre: {name} con direccion {email},te escribe:\n\n{content}',
            "", ['kevinetl01@gmail.com'], reply_to=[email])

            try:
                email.send()
                return redirect('/contact/?valid')
            except:
                return redirect('/contact/?notvalid')

    return render(request,'contact/contact.html', {'my_form': form_contact})
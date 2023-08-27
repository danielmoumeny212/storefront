
from django.shortcuts import render
from django.core.mail import EmailMessage , BadHeaderError
from templated_mail.mail import BaseEmailMessage 

def say_hello(request):
    try: 
        message = BaseEmailMessage (
            template_name='email/hello.html', 
            context={'name': 'Mosh'}
        )
        message.send(to=['danidkm242@gmail.com'])
    except BadHeaderError: 
         pass 
    return render(request, 'hello.html', {'name': 'Mosh'})



# message = EmailMessage('subject', 'message', 'from@manasse.com', ['danidkm242@gmail.com'])
        # message.attach_file('playground/static/images/dog.jpg')
        # message.send()
        
        # mail_admins('subject', 'message', html_message='message')
    #   send_mail ('subject', 'message', 'from@manasse.com',  ['danidkm242@gmail.com'])
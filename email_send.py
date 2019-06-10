# Python code to Send simple text message 
# your Gmail account  
import smtplib                              #python smtp(simple message transfer protocal)
txt="hellonew"  

for i in range(10):                         #specify how many times the message has to be send 
# creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) #gmail link under smtp and port number 
  
# start TLS for security                   
    s.starttls() 
  
# Authentication 
    s.login("your_email_id", "your_email_password") 
  
# message to be sent 
    message = "hi"
  
# sending the mail 
    s.sendmail("your_email_id", "Receiver_email_id", message) 
  

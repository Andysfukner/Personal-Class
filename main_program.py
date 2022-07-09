import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#função necessária para enviar o e-mail
def mail():
  host = "smtp.gmail.com"
  port = "587"
  login = "MEU_EMAIL@gmail.com"
  senha = "MINHA_SENHA"

  server = smtplib.SMTP(host, port)

  server.ehlo()
  server.starttls()
  server.login(login, senha)

  message = 'Olá, poderia imprimir uma cópia desse arquivo? Thanks'
  email_msg = MIMEMultipart()
  email_msg['From'] = login
  email_msg['To'] = 'EMAIL_DESTINATÁRIO@gmail.com'
  email_msg['Subject'] = 'Personal 1 cópia' #Exemplo

  email_msg.attach(MIMEText(message, 'plain'))
	
	#buscando arquivo
  cam_arquivo = f'C:/Users/Professores/Desktop/Andy/English/Personal/Book {book} - Lesson {lesson}.docx'
  attachment = open(cam_arquivo, 'rb')

  att = MIMEBase('application', 'octet-stream')
  att.set_payload(attachment.read())
  encoders.encode_base64(att)
 
   
  att.add_header('Content-Disposition', f'attachment; filename = Book {book} - Lesson {lesson}.docx') 
  attachment.close()
  email_msg.attach(att) 

  server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
  server.quit()

#Pedindo qual lição será realizada
def lessons():
    lesson = int(input('Qual lesson será realizada? '))
    return lesson

#Vendo se precisa cards ou documentos impressos
def printar ():
    print('='*30)
    if lesson in lista1 and lesson in lista2:
      print('Precisa de cards e documento impresso!')
      envio = input('Enviar E-mail? s/n \n')
      if envio == 's':
        #lista.append(f'Book {book} - Lesson {lesson}')(Ignorar)
        mail()
        
    elif lesson in lista1: 
      print('Precisa de cards!')
    elif lesson in lista2:
      print('Precisa de documento impresso!') 
      envio = input('Enviar E-mail? s/n \n')
      if envio == 's':
        #lista.append(f'Book {book} - Lesson {lesson}')
        mail()
        
    else:
      print('Não precisa de cards ou documento impresso!')       
    print('='*30)

while True:
  book=int(input('Qual o livro do aluno? '))
  if book==1:
    lista1 = [2, 7, 8, 14, 15, 17, 25, 23, 26, 29]
    lista2 = [11, 14, 17,  20, 23]
    lesson = lessons()
    printar()
  elif book==2:
    lista1 = [14, 18, 26, 28,30]
    lista2 = [12, 20]
    lesson = lessons()
    printar()
  elif book==3:
    lista1 = [6, 16, 18, 20]
    lista2 = [18, 22]
    lesson = lessons()
    printar()
  elif book==4:
    lista1 = [14]
    lista2 = [8, 16, 28]  
    lesson = lessons()
    printar()    
  elif book==5:
    lista1 = [6, 14, 18, 22, 24]
    lista2 = [2, 4, 8, 16, 20, 26, 28]   
    lesson = lessons()
    printar() 
  else:
    print('Ainda não temos o book: {}'.format(book))
    break

  #print(lista)

  sair=input('\nPressione "N" para sair e Enter para repetir: ').lower()
  if sair == 'n':
     break
     

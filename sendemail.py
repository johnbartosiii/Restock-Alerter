import smtplib
import os
import ssl


def send(to_email, subject, content):
	'''Send email to recipient via gmail SMTP.  Requires environment variables for authentication'''
	email = os.getenv("EMAIL")
	email_pass = os.getenv("EMAIL_PASS")
	auth = (email, email_pass)
	context = ssl.create_default_context()
	server = smtplib.SMTP_SSL( "smtp.gmail.com", 465, context=context)
	server.login(auth[0], auth[1])
	message = f'From: Restock Alerter\nSubject: {subject}\n\n{content}'
	server.sendmail(auth[0], to_email, message)
	server.quit()

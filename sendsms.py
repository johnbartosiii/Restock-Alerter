import smtplib
import os
import ssl

carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
}

def send(number, carrier, message):
	'''Send SMS via gmail SMTP.  Only supports carriers above.  Set auth via environment variables.'''
	# Replace the number with your own, or consider using an argument\dict for multiple people.
	to_number = f'{number}{carriers[carrier]}'
	sms_email = os.getenv("EMAIL")
	sms_email_pass = os.getenv("EMAIL_PASS")
	auth = (sms_email, sms_email_pass)

	# Establish a secure session with gmail's outgoing SMTP server using your gmail account
	#try:
	context = ssl.create_default_context()
	server = smtplib.SMTP_SSL( "smtp.gmail.com", 465, context=context)
	server.login(auth[0], auth[1])
	server.sendmail(auth[0], to_number, message)
	#except:
	#	print('Something went wrong.')


if __name__ == '__main__':
	send('4845466368', 'att', 'testing...')

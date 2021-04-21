from selenium import webdriver
import time
import smtplib # Simple Mail Transfer Protocol
import ssl # Secure Sockets Layer

path='C:\\Users\\Suprakash\\Anaconda3\\chromedriver.exe'
browser=webdriver.Chrome(executable_path=path)

city='kolkata'

browser.get('https://www.breezometer.com/air-quality-map/air-quality/india/'+city)
aqi_value=browser.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[3]/div[1]/div[2]/div[1]').text
aqi_value=int(aqi_value)

if(aqi_value<=100):
	print('AQI value is {}. No need to send email since it is moderate'.format(aqi_value))
else:
	if(aqi_value>300):
		message = 'AQI value is {}. Air pollution level is hazardous'.format(aqi_value)
	elif(aqi_value>200):
		message = 'AQI value is {}. Air pollution level is very unhealthy'.format(aqi_value)
	elif(aqi_value>150):
		message = 'AQI value is {}. Air pollution level is unhealthy'.format(aqi_value)
	else:
		message = 'AQI value is {}. Air pollution level is unhealthy for sensitive groups'.format(aqi_value)

	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = ""  # Enter your sender address
	receiver_email = ""  # Enter receiver address
	password = '' # Enter your password

	context = ssl.create_default_context() # Creates a new SSL Context object with default settings
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server: 
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)

	print("Email has been sent")
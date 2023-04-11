import aiohttp
import asyncio

async def send_mail(receiver_email, spoofed_email, spoofed_name, message, subject):
    try:
        msg = MIMEMultipart("related")
        msg['From'] = f"{spoofed_name} <{spoofed_email}>"
        msg['To'] = receiver_email
        msg['Subject'] = subject
        body = message
        msg.attach(MIMEText(body, 'plain'))
        # Get SMTP settings from config file
        smtp_host = config.get('SMTP', 'host')
        smtp_port = config.getint('SMTP', 'port')
        smtp_username = config.get('SMTP', 'username')
        smtp_password = config.get('SMTP', 'password')
        text = msg.as_string()
        async with aiohttp.ClientSession() as session:
            async with session.starttls(smtp_host, smtp_port):
                await session.login(smtp_username, smtp_password)
                await session.sendmail(spoofed_email, [receiver_email], text)
        print('Spoofed Email sent successfully to '+ str(receiver_email) + ' from ' + str(spoofed_name))
    except Exception as e:
        # Print the exception
        print(traceback.format_exc())

receiver_email = '<Receivers Email Address>'
spoofed_email = '<Spoofed Email Address>'
spoofed_name = '<Spoofed Name>' 
message = '<Text Message to send>'
subject = '<Email Subject/Title>'

# Create and run the coroutine to send email
asyncio.run(send_mail(receiver_email,spoofed_email,spoofed_name, message, subject))

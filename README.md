# Emailspoof

1) Spoof Email Sending Script

Using below script you can send the basic text message to the target email address using the spoofed email with the spoof name. Make sure you do the following changes in the script.py file & config.ini file.


receiver_email = ‘<Receivers Email address>’

spoofed_email = ‘<Spoofed Email Address>'

spoof_name =       ' <spoofed name >'

message   =‘<Text Message to send>*

subject = ‘<Email Subject/Title>’



changes to make in the spoof.py

Create a new config.ini

[SMTP]

host smtp-relay.sendinblue.com

port = 587

username -> <Your SMTP Email>

password= <Your SMTP Master Password>

changes to make in the config.Inl (if you are using some other

SMTP then make sure you also edit the host & port values)

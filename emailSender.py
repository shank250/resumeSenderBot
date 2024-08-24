import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import TextToEmailsFinder 
from config import get_password

from_email_shashank = get_password('shashank_google_email')
from_password_shashank = get_password('shashank_google_password')

from_email_raghuraj = get_password('raghuraj_google_email')
from_password_raghuraj = get_password('raghuraj_google_password')

class Sender:
    def send_email(self, sender, password, recipient, subject, html_part, turn):
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject
        

        
        msg.attach(html_part)

        try:
            # server = smtplib.SMTP('outlook.office365.com', 587)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            # server.set_debuglevel(1)  # Add debugging
            print("Connecting to server...")
            # server.ehlo('outlook.com')  # Use a valid domain here
            print("Starting TLS...")
            server.starttls()
            # server.ehlo('outlook.com')  # Repeat EHLO after STARTTLS
            server.ehlo()  # Repeat EHLO after STARTTLS
            
            print("Logging in...")
            server.login(sender, password)
            print("Sending email...")
            text = msg.as_string()
            server.sendmail(sender, recipient, text)
            print("Email sent successfully to ", recipient)
            find = TextToEmailsFinder.Fider()
            find.delete_client_email(recipient)
            find.add_email_to_sent(recipient)
            if turn: find.add_email_to_sent_by(recipient, find.shashank_sent)
            else: find.add_email_to_sent_by(recipient, find.raghuraj_sent)

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            try:
                server.quit()
            except:
                pass
        
    def auto_sender(self, turn):
        if turn:
            from_email = from_email_shashank
            from_pass = from_password_shashank
            recipient = TextToEmailsFinder.Fider().get_last_added_email()
            shashank_html_part = MIMEText(f'''
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #000000; background-color: #ffffff; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #000000; }}
        .header {{ text-align: center; border-bottom: 2px solid #000000; padding-bottom: 10px; margin-bottom: 20px; }}
        .content {{ margin-bottom: 20px; }}
        .footer {{ border-top: 1px solid #000000; padding-top: 10px; font-size: 14px; text-align: center; }}
        .button-container {{ text-align: center; margin: 20px 0; }}
        .button {{
            background-color: #000000;
            color: #ffffff;
            padding: 12px 24px;
            text-decoration: none;
            border: 1px solid #000000;
            font-weight: bold;
            display: inline-block;
            transition: background-color 0.3s ease;
        }}
        .button:hover {{
            background-color: #333333;
        }}
        .highlights {{ background-color: #f8f8f8; padding: 15px; border-left: 4px solid #000000; margin-bottom: 20px; }}
    </style>
</head>
<body>
    <div class="container">
        <!-- <div class="header">
            <h2>Shashank Srivastava</h2>
            <p>Internship Application: Software Development / Data Science</p>
        </div> -->
        <div class="content">
            <p>Greetings,</p>
            <p>I am writing to express my keen interest in a software development or data science internship within your esteemed organization. As a Bachelor of Technology student in Computer Science, I offer the following qualifications:</p>
            <div class="highlights">
                <ul>
                    <li><strong>Technical Skills:</strong> Proficient in Python, Java, C, Django, Azure, AWS</li>
                    <li><strong>Data Analysis:</strong> Experience with Numpy, Pandas, Scikit-learn</li>
                    <li><strong>Leadership:</strong> Microsoft Learn Student Ambassador, leading workshops for 300+ students</li>
                    <li><strong>Industry Experience:</strong> Completed AWS AI ML Virtual Internship</li>
                    <li><strong>Project Achievements:</strong>
                        <ul>
                            <li>Developed Automated Articles Generation Website (1,200+ event counts in first month)</li>
                            <li>Created YouTube Video Software (10,000+ views in two weeks)</li>
                        </ul>
                    </li>
                </ul>
            </div>
            <p>I am eager to contribute these skills to your team and further develop my expertise in a professional setting. I would welcome the opportunity to discuss how I can add value to your ongoing projects.</p>
        </div>
        <div class="button-container">
            <a href="https://resumecreators.azurewebsites.net/redirect-to-google/?email={recipient}&resume_id={turn}&redirect_url=https://drive.google.com/file/d/1w3zrU8Qj0S4syh3I9dAEamqP6c9m2q_X/view?usp=drive_link" class="button">View Full Resume</a>
        </div>
        <div class="footer">
            <p>Thank you for your consideration.</p>
            <p>Shashank Srivastava | +917348745464 | shashank21005@gmail.com</p>
        </div>
    </div>
    <img src="https://resumecreators.azurewebsites.net/tracking_pixel/?email={recipient}" width="1" height="1" alt="" />
</body>
</html>

''', 'html')

            Subject = "Shashank Srivastava - Software Development Internship Application"
            html_part = shashank_html_part
        else:
            from_email = from_email_raghuraj
            from_pass = from_password_raghuraj
            recipient = TextToEmailsFinder.Fider().get_last_added_email()
            # globals
            # recipient = recipient_current
            raghuraj_html_part = MIMEText( f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Resume Review Request - Raghuraj Pratap Yadav</title>
<style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #000000;
            background-color: #ffffff;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            border: 1px solid #000000;
            padding: 20px;
        }}
        h1 {{
            color: #000000;
            border-bottom: 1px solid #000000;
            padding-bottom: 10px;
        }}
        .button {{
            display: inline-block;
            padding: 10px 20px;
            background-color: #000000;
            color: #ffffff;
            text-decoration: none;
            border: 2px solid #000000;
            transition: background-color 0.3s, color 0.3s;
            margin-top: 20px;
        }}
        .button:hover {{
            background-color: #ffffff;
            color: #000000;
        }}
</style>
</head>
<body>
<div class="container">
<h1>Internship Application</h1>
<p>Dear Recruiter,</p>
<p>I hope this message finds you well. I am writing to request your review of my resume  for potential software development or data science or Machine Learning internship opportunities within your esteemed organization.</p>
<p>As an aspiring Software Development Engineer with a strong foundation in Artificial Intelligence and Machine Learning, I believe my skills and experiences align well with the innovative work your company is known for. My background includes:</p>
<ul>
<li>Hands-on experience with Agile methodologies through an internship at Infosys</li>
<li>Proficiency in full-stack web development, demonstrated by projects such as a Django-based resume builder hosted on Microsoft Azure</li>
<li>Active engagement as a Microsoft Student Ambassador, showcasing leadership and technical skills</li>
<li>Strong programming skills in Python, C, Java, and various frameworks including TensorFlow and Django</li>
<li>Experience with cloud services such as Azure and AWS</li>
</ul>
<p>I would be grateful for the opportunity to discuss how my skills and enthusiasm could contribute to your team's success. Please review my attached resume and let me know if there are any suitable internship positions available in software development or data science.</p>
<p>Thank you for your time and consideration. I look forward to the possibility of speaking with you further about opportunities within your organization.</p>
<p>Sincerely,<br>Raghuraj Pratap Yadav<br>
        +91 9899679338 | Raghurajpratapyadav11@gmail.com</p>
<a href="https://resumecreators.azurewebsites.net/redirect-to-google/?email={recipient}&resume_id={turn}&redirect_url=https://drive.google.com/file/d/1CcDGjpzQ8H4ctEaImtuYWi5CTcPopRI-/view?usp=drive_link" class="button">View Resume</a>
</div>
<img src="https://resumecreators.azurewebsites.net/tracking_pixel/?email={recipient}" width="1" height="1" alt="" />
</body>
</html>''', 'html')
            Subject = "Raghuraj Pratap Yadav - Software Development Internship Application"
            html_part = raghuraj_html_part

        # print(from_email, from_pass, recipient, Subject, html_part)
        self.send_email(from_email, from_pass, 
                        recipient=recipient, 
                        subject=Subject,
                        html_part=html_part, 
                        turn=turn
                        )

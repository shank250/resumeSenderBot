import re
import csv
import os

class Fider:
    def __init__(self):
        self.fileName = 'getjobs.txt'
        self.clients_file = 'clients.csv'
        self.sent_file = 'sent.csv'
        self.shashank_sent = 'shashank_sent.csv'
        self.raghuraj_sent = 'raghuraj_sent.csv'


    def fileReader(self):
        with open(self.fileName, 'r') as f:
            data = f.read()
       
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        email_matches = re.findall(email_pattern, data)
        email_matches = set(email_matches)
        return email_matches

    def get_existing_emails(self):
        existing_emails = set()
        for file in [self.clients_file, self.sent_file]:
            try:
                with open(file, 'r') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if row:  # Check if the row is not empty
                            existing_emails.add(row[0])  # Assuming email is in the first column
            except FileNotFoundError:
                print(f"Warning: {file} not found. Continuing...")
        return existing_emails

    def add_new_emails(self):
        new_emails = self.fileReader()
        existing_emails = self.get_existing_emails()
        
        new_clients = [email for email in new_emails if email not in existing_emails]
        
        if new_clients:
            with open(self.clients_file, 'a', newline='') as f:
                writer = csv.writer(f)
                for email in new_clients:
                    # if email not in existing_emails:
                    #     existing_emails.add(email)
                    writer.writerow([email])
            print(f"Added {len(new_clients)} new email(s) to {self.clients_file}")
        else:
            print("No new emails to add.")
    
    def get_last_added_email(self):
        try:
            with open(self.clients_file, 'r') as f:
                reader = csv.reader(f)
                emails = list(reader)
                if emails:
                    return emails[-1][0]  # Return the first column of the last row
                else:
                    return "No emails found in the file."
        except FileNotFoundError:
            return f"Error: {self.clients_file} not found."

    def delete_client_email(self, email_to_delete):
        temp_file = 'temp_clients.csv'
        email_found = False
        try:
            with open(self.clients_file, 'r') as input_file, open(temp_file, 'w', newline='') as output_file:
                reader = csv.reader(input_file)
                writer = csv.writer(output_file)
                for row in reader:
                    if row and row[0] != email_to_delete:
                        writer.writerow(row)
                    elif row and row[0] == email_to_delete:
                        email_found = True

            if email_found:
                os.replace(temp_file, self.clients_file)
                return f"Email {email_to_delete} has been deleted."
            else:
                os.remove(temp_file)
                return f"Email {email_to_delete} not found in the file."
        except FileNotFoundError:
            return f"Error: {self.clients_file} not found."

    def add_email_to_sent(self, email):
        try:
            with open(self.sent_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([email])
            return f"Email {email} has been added to {self.sent_file}"
        except IOError:
            return f"Error: Unable to write to {self.sent_file}"
        
    def add_email_to_sent_by(self, email, sender):
            try:
                with open(sender, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([email])
                return f"Email {email} has been added to {sender}"
            except IOError:
                return f"Error: Unable to write to {sender}"




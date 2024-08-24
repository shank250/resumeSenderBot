import telegramMessageReader, TextToEmailsFinder
import emailSender
import time
def main():
    reader = telegramMessageReader.TeleReader()
    text_to_email = TextToEmailsFinder.Fider()
    text_to_email.add_new_emails()
    sender = emailSender.Sender()
    turn = 1
    counter = 0
    while counter < 100:
        sender.auto_sender(turn)
        counter+=1
        print("COunter : ", counter, " Sleeping...")
        time.sleep(30)
        if turn == 0: turn = 1
        else: turn = 0

if  __name__ == '__main__':
    main()

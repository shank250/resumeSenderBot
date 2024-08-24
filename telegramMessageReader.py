from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
from dotenv import load_dotenv
from datetime import datetime, timezone
from config import get_password
import json
import os

api_id = get_password('api_id')
api_hash = get_password('api_hash')
phone = get_password('phone')

# The phone number you used to log in
# phone = 
# try:
#     os.remove('getjobs.txt')
# except:
#     pass


offset_file = 'offsetgetjobs.json'
messages_file = 'getjobs.txt'
client = TelegramClient('getjobss', api_id, api_hash)

def load_offset():
    if os.path.exists(offset_file):
        with open(offset_file, 'r') as file:
            return json.load(file).get('offset_id', 0)
    return 0

def save_offset(offset_id):
    with open(offset_file, 'w') as file:
        json.dump({'offset_id': offset_id}, file)

def save_messages(messages):
    with open(messages_file, 'a', encoding='utf-8') as file:
        for message in messages:
            if message.message:  # Check if the message is not None
                file.write(message.message + '\n')

class TeleReader:
    async def main(offsetDate = False):
        limit = 100  # Number of messages to retrieve per request
        max_batch_count = float('inf')
        if offsetDate:
            offset_date = None
        else:
            limit = int(input("No of Messages Per Batch:"))
            max_batch_count = int(input("No of Batches: "))
            offset_date = None
        await client.start(phone)
        
        # Get input channel
        # username = 'getjobss'  # Username or ID of the group
        channels = ['getjobss', 'jobs_and_internships_updates', 'PLACEMENTLELO', 'hiringdaily', 'TechUprise_Updates', 'algoprep_in', 'IT_Fresher_Jobs', 'relocateme', 'Government_Jobs_Sarkari_Naukri', 'Jobs_Internship_Campus_Placement', 'off_campus_jobs_and_internships', 'internship', 'OffCampus_Campus_Jobs_Internship']
        for channel in channels:
            print("*"*10,"Channel Name: ", channel,"*"*10 )
            username = channel
            if username.isdigit():
                entity = PeerChannel(int(username))
            else:
                entity = await client.get_entity(username)
            
            my_channel = entity
            
            # Get the messages
            # offset_id = load_offset()
            offset_id = 0
            
            all_messages = []
            batch_no = 1
            while True and batch_no < max_batch_count:
                print("Processing batch number: ", batch_no, end = " ")
                history = await client(GetHistoryRequest(
                    peer=my_channel,
                    offset_id=offset_id,
                    offset_date=offset_date,
                    add_offset=0,
                    limit=limit,
                    max_id=0,
                    min_id=0,
                    hash=0
                ))
                
                if not history.messages:
                    break
                
                messages = history.messages
                save_messages(messages)
                all_messages.extend(messages)
                offset_id = messages[-1].id
                save_offset(offset_id)
                print("[Completed]")
                # print(message)
                batch_no += 1
                # break  # Remove this line to retrieve more messages in batches

        # for message in all_messages:
        #     print(message.message)

        # Run the client
    with client:
        client.loop.run_until_complete(main())

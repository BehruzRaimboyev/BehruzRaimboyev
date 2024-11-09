import glob
import os
import requests
import fitz 

bot_token='7240011260:AAFTNHfecYNk-CdgFayGstRdCg1cM6LlbKQ'
channel_id=-1002366949553
book_file_path='C:/Users/cacain/Documents/nnnn.pdf'

if not bot_token or not channel_id:
    raise ValueError("Bot token or channel ID is missing in the environment variables.")


def extract_first_page_as_image(pdf_path: str):
    pdf_document = fitz.open(pdf_path)
    first_page = pdf_document.load_page(0)
    pix = first_page.get_pixmap(dpi=300)
    return pix


def send_to_telegram(bot_token: str, channel_id: str, file_path: str):
    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
    
 
    with open(file_path, 'rb') as file:
        files = {'document': (os.path.basename(file_path), file)}
        payload = {'chat_id': channel_id}
        response = requests.post(url, data=payload, files=files)
    
    if response.status_code == 200:
        print(f"Successfully sent {file_path} to {channel_id}")
    else:
        print(f"Failed to send {file_path}: {response.status_code} - {response.text}")


pdf_files = glob.glob(r'C:/Users/cacain/Documents/nnnn')



for file_path in pdf_files:
    print(f"Processing file: {file_path}")
    send_to_telegram(bot_token, channel_id, file_path)

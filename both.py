import requests

TELEGRAM_BOT_TOKEN = '8554495986:AAF-X26Y0F-J4KP1UNeeAiDbdZy01D_Qoc'
CHAT_ID = '8933388029'
IMAGE_URL = 'https://picsum.photos/800/600'

def send_image_to_telegram():
    try:
        image_response = requests.get(IMAGE_URL, stream=True, timeout=10)
        if image_response.status_code == 200:
            url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto'
            files = {'photo': image_response.content}
            data = {'chat_id': CHAT_ID, 'caption': 'تم سحب الصورة وإرسالها بنجاح بواسطة البوت!'}
            
            response = requests.post(url, files=files, data=data)
            if response.status_code == 200:
                print("تم إرسال الصورة بنجاح!")
            else:
                print(f"فشل الإرسال: {response.text}")
        else:
            print("فشل في تحميل الصورة.")
    except Exception as e:
        print(f"حدث خطأ: {e}")

if __name__ == '__main__':
    send_image_to_telegram()

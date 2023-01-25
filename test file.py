import easyocr
from googletrans import Translator
import time
import requests
from langdetect import detect_langs

def translate(text, source_language, target_language):
    base_url = "https://translate.googleapis.com/translate_a/single?"
    params = {
        "client": "gtx",
        "sl": source_language,
        "tl": target_language,
        "dt": "t",
        "q": text
    }
    response = requests.get(base_url, params=params)
    return response.json()[0][0][0]
   
translation = translate("hello","ar", "en")
print(translation)  
time.sleep(10)

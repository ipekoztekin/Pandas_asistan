import requests

# Arkadaşının çalıştırdığı o anahtar ve model ismiyle gidiyoruz
API_KEY = "AIzaSyBbKptHnvMkawg4OiyQHDzVqd-R1Sc8CW0"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={API_KEY}"

def asistan():
    print("\n--- PANDAS UZMANI ÇALIŞIYOR ---")
    while True:
        soru = input("\nSorun nedir?: ")
        if soru.lower() == 'q': break

        payload = {
            "contents": [{"parts": [{"text": f"Pandas uzmanı gibi kısa ve net cevap ver: {soru}"}]}]
        }

        try:
            res = requests.post(URL, json=payload)
            # Eğer 404 verirse ne olduğunu direkt ekrana basıyoruz
            if res.status_code != 200:
                print(f"HATA ({res.status_code}): {res.text}")
                continue
            
            data = res.json()
            print("\nASİSTAN:", data['candidates'][0]['content']['parts'][0]['text'])
        except Exception as e:
            print("Sistem hatası:", e)

if __name__ == "__main__":
    asistan()
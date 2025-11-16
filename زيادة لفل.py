import requests
import time

channel_id = "1258898445314424835"  # اكتب ID القناة
auth_token = "NTY0OTk3MDA0NDIyMjgzMjk0.GL7M-2.Z5l0N3bDQEuPslPxHkPrrPjvuYwKXZNow8vnHw"  # توكن حسابك العادي
message_text = "Don't forget to drink water droplet"
interval_seconds = 6  # 10 دقائق

headers = {
    "Authorization": auth_token
}

while True:
    for i in range(2):
        try:
            payload = {"content": message_text}
            response = requests.post(
                f"https://discord.com/api/v9/channels/{channel_id}/messages",
                headers=headers,
                json=payload
            )
            if response.status_code == 200:
                print(f"Message sent: {message_text}")
            else:
                print(f"Failed: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1)

    time.sleep(interval_seconds)
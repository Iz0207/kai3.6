import uvloop
import asyncio
from pyrogram import Client, filters

# Install uvloop
uvloop.install()

# Replace with your own Telegram API credentials
api_id = 21827985
api_hash = '249159e0fc539bb9bce0d5e974c44f88'

# Replace with your phone number, session file name, and password
phone = '+601156292264'
session_file = 'xzy0207'
password = '0207'

# Replace with the actual group chat IDs and allowed user IDs
group_chat_id1 = -1001766161750
allowed_user_id1 = 6070986947

group_chat_id2 = -1001863685543
allowed_user_id2 = 1518090731
allowed_user_id3 = 5042719163

# Explicitly create an event loop with uvloop
loop = uvloop.new_event_loop()
asyncio.set_event_loop(loop)

# Create a Client instance
app = Client(session_file, api_id=api_id, api_hash=api_hash)

# Define the function to handle incoming messages
async def auto_reply_to_photo(client, message):
    try:
        print(f"Received a photo message from user {message.from_user.id} in chat {message.chat.id}")
        # Asynchronously reply to the photo with "1"
        await client.send_message(message.chat.id, "1")
        print("Auto reply sent.")
    except Exception as e:
        print(f"Error processing photo: {e}")

# Register the message handler
@app.on_message(
    filters.photo & 
    ((filters.chat(group_chat_id1) & filters.user(allowed_user_id1)) |
     (filters.chat(group_chat_id2) & filters.user(allowed_user_id2)) |
     (filters.chat(group_chat_id2) & filters.user(allowed_user_id3)))
)
async def wrapper_function(_, message):  # Use _ to denote an unused variable
    await auto_reply_to_photo(app, message)

if __name__ == "__main__":
    # Run the Pyrogram client
    app.run()

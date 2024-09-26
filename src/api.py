import logging
from fastapi import FastAPI, HTTPException
from blocks import priority_block, priority_attachment
from channels import get_channel
from models import Message
from main import send_to_channel

app = FastAPI()

@app.post("/send_channel_msg")
async def send_msg_to_channel(message: Message) -> None:
    channel = get_channel(message.channel_id)
    
    if not channel:
        return
    try:
        if message.priority is not None:
            blocks = priority_block(title=message.title, text=message.text,
                                    priority=message.priority, link=message.link, link_title=message.link_title, image_link=message.image_link)
            
            attachments = priority_attachment(priority=message.priority, content=str(
                message.attachment.content) or '') if message.attachment else None

            send_to_channel(channel_id=channel, text=message.text,
                            blocks=blocks, attachments=attachments)

    except Exception as e:
        logging.error('Could not send message', e)
        raise HTTPException(status_code=500, detail="Message not sent")
    return message

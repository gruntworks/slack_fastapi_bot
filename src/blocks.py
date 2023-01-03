from models import Priority

def title_block(priority: Priority, title: str = '') -> list:
    return (
        {
            "type": "section",
            "text": {
                    "type": "mrkdwn",
                    "text": f"{':speech_balloon: ' if priority == Priority.normal else ''}"
                            f"{':warning: ' if priority == Priority.high else ''}"
                            f"{':bangbang: ' if priority == Priority.fatal else ''}"
                            f"{':white_check_mark: ' if priority == Priority.success else ''}"
                            f"{title}"
            }
        }
    )

def link_title_with_text(text: str, link: str, link_title: str) -> list:
    """ Generates block with link and text"""
    return (
        [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"{text} \n\n<{link}|{link_title}>",
                }
            }
        ]
    )

def priority_block(title: str, text: str, priority: Priority, link: str = None, link_title: str = None, image_link: str = None) -> list:
    block = []
    if title:
        block.append(title_block(priority, title))
    if text:
        block.append(
            {
                "type": "context",
                "elements": [
                    {
                        "type": "plain_text",
                        "text": f"{text}"
                    }
                ]
            })
    if link:
        block.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*<{link}|{link_title}>*"
                }
            })
    if image_link:
        block.append(
            {
                "type": "image",
                "image_url": f"{image_link}",
                "alt_text": "some image",
            }
        )
    block.append({"type": "divider" })
    return block


def priority_attachment(priority: Priority, content: str = '', pretext: str = '') -> list:
    color = ['#36C5F0', '#ECB22E', '#E01E5A', '#2eb886'][priority]
    return ([
        {
            "fallback": "Can't display the attachment",
            "color": color,
            "pretext": pretext or '',
            "text": content
        }
    ]
    )

import asyncio
from userbot.events import register
from userbot import CMD_HELP


@register(pattern=r".floodchat (.*)", outgoing=True)
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    input_str = event.pattern_match.group(1)
    action = "typing"
    if input_str:
        action = input_str
    async with event.client.action(event.chat_id, action):
        await asyncio.sleep(120)
        
        
CMD_HELP.update({
    "floodchat": ".floodchat\
    \nUsage: Creating Fake Chat actions Just for fun and spam."
})
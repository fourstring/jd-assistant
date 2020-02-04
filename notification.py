import functools

from pyrogram import Client
from pyrogram import Filters, Message

from config import global_config
from jd_assistant import Assistant

TARGET_CHAT = int(global_config.get('notification', 'target_chat'))


def telegram_init(telegram_notify):
    client = Client("tg_notify")

    @client.on_message(filters=Filters.command('jd'))
    def query_id(app: Client, message: Message):
        app.send_message(message.chat.id, f'命令发送者id:{message.from_user.id};当前聊天id:{message.chat.id}',
                         reply_to_message_id=message.message_id)

    @functools.wraps(telegram_notify)
    def inner(*args, **kwargs):
        telegram_notify(client, *args, **kwargs)

    client.start()
    return inner


@telegram_init
def telegram_success_notify_callback(client: Client, ass: Assistant, sku_id, count):
    client.send_message(TARGET_CHAT, f'商品{sku_id}共{count}个下单成功，请尽快支付')

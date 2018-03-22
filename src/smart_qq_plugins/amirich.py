# -*- coding: utf-8 -*-

from smart_qq_bot.logger import logger
from smart_qq_bot.signals import (
    on_all_message
)
from smart_qq_plugins import fetch
import time


@on_all_message(name='amirich')
def amirich(msg, bot):
    if "发哥最近发财了吗" in msg.content:
        t = time.time()
        print(t)
        curprice = fetch.fetchdata()
        print(time.time() -t)
        reply = bot.reply_msg(msg, return_function=True)
        logger.info("RUNTIMELOG " + str(msg.from_uin) + " calling me out, trying to reply....")
        if curprice - 0.2900 > 0:
            reply_content = "已经盈利" + str(round((curprice - 0.2900)/0.29 * 100, 2)) + "%"
        else:
            reply_content = "已经亏损" + str(round((0.2900 - curprice) / 0.29 * 100, 2)) + "%"
        # reply_content = (fetch.fetchdata() - 0.2900)/0.29
        reply(reply_content)

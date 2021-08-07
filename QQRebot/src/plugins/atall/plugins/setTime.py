from nonebot import require
import nonebot
from autoReport import autoReport

scheduler = require('nonebot_plugin_apscheduler').scheduler


@scheduler.scheduled_job('cron', hour='00', minute='01', id='autoRp1')
@scheduler.scheduled_job('cron', hour='08', minute='00', id='autoRp2')
@scheduler.scheduled_job('cron', hour='09', minute='00', id='autoRp3')
async def handle_first_receive():
    bot = nonebot.get_bots()['用来当机器人的qq号']
    a1 = autoReport("学号", "密码","姓名")
    a2 = autoReport("学号", "密码","姓名")
    a3 = autoReport("学号","密码", "姓名")
    a4  = autoReport("学号", "密码", "姓名")
    a5 = autoReport("学号", "密码", "姓名")
    a6 = autoReport("学号", "密码", "姓名")
    return await bot.call_api('send_msg', **{
        'message': a1+'\n'+'\n'+a2+'\n'+a3+'\n'+a4+'\n'+a5+'\n'+a6,
        'group_id': '群号'
    })

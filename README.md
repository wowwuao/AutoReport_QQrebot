用来自动填报UPC疫情防控通并给出反馈的QQ机器人

## 免责声明

- 此脚本仅供参考学习，本人不对此脚本产生的任何影响负责

- 请于下载此脚本之后于24小时内彻底删除此脚本

- 下载此脚本即视为同意此免责声明

  

## 环境
Python 3.7以上
```python
pip install nonebot2
pip install nonebot-adapter-cqhttp
pip install nonebot_plugin_apscheduler
pip install lxml
pip install requests
```
## 用法
1. 打开 gocqhttp 中的 config.yml 填入用来当机器人的QQ账号和密码
2. 在命令行里打开 go-cqhttp.exe(Windows系统) 或者 go-cqhttp(Linux系统)，进行模拟登录，确保登录成功。
3. 打开 QQRebot\src\plugins\atall\plugins\setTime.py
  根据汉字提示，进行填空。
4. 同时运行 go-cqhttp.exe(go-cqhttp) 和 bot.py ，看到 python控制台里有你用来当机器人的QQ号就证明连接成功了，可以通过 /echo XXX测试一下
5. 填报是根据上一天的历史记录来自动完成的，如果发生位置等信息变更，需要自己手动更新。疫情防控通填报脚本来源 https://github.com/DrS1X/UPC-Submit-Auto ，感谢这位老哥！




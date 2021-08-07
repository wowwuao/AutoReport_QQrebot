from pathlib import Path

# import nonebot
import nonebot
from nonebot import get_driver

from .config import Config

global_config = get_driver().config
plugin_config = Config(**global_config.dict())

# Export something for other plugin
# export = nonebot.export()
# export.foo = "bar"

# @export.xxx
# def some_function():
#     pass

_sub_plugins = set()
_sub_plugins |= nonebot.load_plugins(
    str((Path(__file__).parent / "plugins").resolve()))

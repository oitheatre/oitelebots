#!/usr/bin/env python

import yaml
import re


def subs_parameter(line, bot_pattern):
    results = re.findall(r'{{([A-Za-z0-9 _]+)}}', line)
    if results:
        for result in results:
            setting_value = bot_pattern[result.strip()]
            line = re.sub(r'{{' + result + '}}', str(setting_value), line)
    return line


with open('bot_settings.yml', 'r') as sf:
    bot_settings = yaml.safe_load(sf)

HOST_URL = bot_settings['HOST_URL']
PRODUCTION_PORT = bot_settings['PRODUCTION_PORT']
DEV_PORT = bot_settings['DEV_PORT']
FLASK_PORT = bot_settings['FLASK_PORT']

bot_settings.pop('HOST_URL', None)
bot_settings.pop('PRODUCTION_PORT', None)
bot_settings.pop('DEV_PORT', None)
bot_settings.pop('FLASK_PORT', None)

bot_patterns = []
for key, settings in bot_settings.items():
    bot_setting = {}
    bot_setting['BOT_NAME'] = key
    bot_setting['HOST_URL'] = HOST_URL
    bot_setting['PRODUCTION_PORT'] = PRODUCTION_PORT
    bot_setting['DEV_PORT'] = DEV_PORT
    bot_setting['FLASK_PORT'] = FLASK_PORT
    for skey, setting in settings.items():
        bot_setting[skey] = setting
    bot_setting['DEV_BOT_PORT'] = DEV_PORT + bot_setting['NUMBER_ID']
    bot_patterns.append(bot_setting)

with open('nginx_bot_template.conf') as tf:
    template_config = tf.read().splitlines()

new_config = []
strbuf = []
repeat = False
for line in template_config:
    if line.strip() == "%% BEGIN REPEAT %%":
        repeat = True
        continue
    if line.strip() == "%% END REPEAT %%":
        repeat = False
        for bot_pattern in bot_patterns:
            new_config.extend([subs_parameter(l, bot_pattern) for l in strbuf])
            new_config.append("\n")
        strbuf = []
        continue

    if not repeat:
        line = subs_parameter(line, bot_patterns[0])
        new_config.append(line)
    else:
        strbuf.append(line)

for line in new_config:
    print(line)

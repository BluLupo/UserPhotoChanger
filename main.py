#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright Hersel Giannella
# www.hersel.it

import os
import random
import datetime
from config import Config
from pyrogram import Client, filters
from apscheduler.schedulers.asyncio import AsyncIOScheduler

app = Client(
    "rand_profile_pict",
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)

# Constants for Scheduler
HOUR = 12
MINUTE = 30
SECOND = 00

# /rand Manual Random
@app.on_message(filters.command("rand") & filters.private & filters.user(Config.OWNER))
def rand_command():
    current_time = datetime.datetime.utcnow()
    directory = "img/"
    random_image = random.choice(os.listdir(directory))
    app.set_profile_photo(photo=open(directory + random_image,'rb'))
    print("Image modified on {}".format(current_time))


scheduler = AsyncIOScheduler()
scheduler.add_job(rand_command, 'cron', hour=HOUR, minute=MINUTE, second=SECOND)
scheduler.start()

app.run()
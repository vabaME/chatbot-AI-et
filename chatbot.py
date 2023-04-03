#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import openai

openai.api_key="SINU API VÕTI"
messages = []

# leia olemasolevad vestlusfailid
files = [f for f in os.listdir() if f.startswith("vestlus-") and f.endswith(".txt")]
# loo uus failinimi
if files:
    last_file = max(files)
    last_num = int(last_file.split("-")[1].split(".")[0])
    new_num = last_num + 1
else:
    new_num = 1
filename = f"vestlus-{new_num}.txt"

print("Sa võid nüüd vestelda.")
with open(filename, "w") as file:
    while True:
        try:
            message = input("")
        except UnicodeDecodeError:
            message = input("", encoding="UTF-8")
        messages.append({"role":"user","content": message})
        file.write("User: " + message + "\n")

        response=openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=messages
        )

        reply = response["choices"][0]["message"]["content"]
        print(reply)
        file.write("Bot: " + reply + "\n")

        if "goodbye" in message.lower():
            break

    file.close()


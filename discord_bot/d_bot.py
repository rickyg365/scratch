import os
import random
import datetime

import discord
from dotenv import load_dotenv
from data_handle import FarewellHandler, GreetingHandler


""" Load in environment variables """
# filepath = "sample_env.env"
filepath = "dbot.env"

load_dotenv(filepath)

# Load in Variables
token = os.getenv("TOKEN")

""" Start up Message Handlers """
greeter = GreetingHandler("greetings.txt")
byer = FarewellHandler("farewells.txt")

""" Setup Discord Client """
client = discord.Client()

def get_all_channels(client_obj):
    # get all channels
    all_channels = list(client.get_all_channels())

    output = {
        "category": [],
        "voice": [],
        'text': [],
        "other": []
    }

    # print(all_channels)
    for new_channel in all_channels:
        if type(new_channel) is discord.channel.TextChannel:
            output["text"].append(new_channel)
            # print(f"[ Text Channel ]: {new_channel}")
        elif type(new_channel) is discord.channel.VoiceChannel:
            output["voice"].append(new_channel)
            # print(f"[ Voice Channel ]: {new_channel}")
        elif type(new_channel) is discord.channel.CategoryChannel:
            output["category"].append(new_channel)
            # print(f"[ Category Channel ]: {new_channel}")
        else:
            # print(type(new_channel))
            output["other"].append(new_channel)
            # channel_kind="Other Channel"
            # print(f"[ {channel_kind} ]: {new_channel}")
    return output


# Create Functions
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}" )

    # get all channels
    all_channels = get_all_channels(client)
    # print(all_channels)
    
    # Send message to specific channel
    channel = client.get_channel(921144365299150919)
    await channel.send("Connected to bot-commands!")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Welcome to the Server {member}!")
    

""" Incorporate greeter and other handlers """
@client.event
async def on_message(message):
    # Message Variables
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    # Log
    print(f"{username} ({channel}): {user_message}")
    
    # so bot doesnt respond to self
    if message.author == client.user:
        return
    
    if channel == 'general':
        if user_message.lower() in greeter.valid_triggers:
            new_greeting = greeter.random()
            await message.channel.send(f"{new_greeting} {username}!")
            return
        
        if user_message.lower() in byer.valid_triggers:
            new_farewell = byer.random()
            await message.channel.send(f"{new_farewell} {username}!")
            return

        if user_message.lower() == '!random':
            response = f"This is your random number: {random.randrange(100_000)}"
            await message.channel.send(response)
            return

    if channel == 'bot_test':
        # Break down input
        base_input = user_message
        args = base_input.split(' ')

        if len(args) <= 2:
            print("Not enough inputs")
            return
        

        base_input = args[0]
        option = args[1]
        input_item = args[2].replace('-', ' ')
               
        
        if base_input == "!new":
            if option == "greeting":
                greeter.add_item(f"{input_item}")
                greeter.save()
            
                await message.channel.send(f"added: {input_item}!")
                return
            
            if option == "farewell":
                byer.add_item(f"{input_item}")
                byer.save()
                
                await message.channel.send(f"added: {input_item}!")
                return
        
        

    if user_message.lower() == "!anywhere":
        await message.channel.send("This can be used anywhere!")
        return

 
def main():
    # Start Discord Client
    client.run(token)

if __name__ == "__main__":
    main()

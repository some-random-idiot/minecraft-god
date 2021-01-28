import discord
import time
from subprocess import call

client = discord.Client()
prefix = "&"

connected = []  # Stores a list of vc ids

@client.event
async def on_ready():
    print("READY")


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith(f"{prefix}talk"):
        if message.author.voice.channel.id not in connected:
            await message.author.voice.channel.connect()
            connected.append(message.author.voice.channel.id)
            print(connected)

        voice_client = message.guild.voice_client
        dialogue = message.content[5:]

        if len(dialogue) < 96:
            with open(".\\SAM\\Test.bat", mode="w") as command_batch:
                command_batch.write("cd .\\SAM\\\n")
                command_batch.write(f"sam -wav temp.wav {dialogue}")
            call(".\\SAM\\Test.bat")
            voice_client.play(discord.FFmpegPCMAudio(".\\SAM\\temp.wav"))
        else:
            for i in range(0, len(dialogue), 96):
                while voice_client.is_playing():
                    pass
                with open(".\\SAM\\Test.bat", mode="w") as command_batch:
                    command_batch.write("cd .\\SAM\\\n")
                    command_batch.write(f"\nsam -wav temp.wav {dialogue[i:i+96]}")
                call(".\\SAM\\Test.bat")
                voice_client.play(discord.FFmpegPCMAudio(".\\SAM\\temp.wav"))


client.run("")

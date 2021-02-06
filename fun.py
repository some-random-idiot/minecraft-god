import discord
from discord import ChannelType
import random
from chest import prefix
from chest import CustomEmojis

client = discord.Client()


@client.event
async def on_ready():
    print("READY")


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith(f"{prefix}die"):
        await client.logout()

    if message.content.startswith(f"{prefix}build"):
        structure_name = message.content[7:]
        if structure_name == "" or structure_name.replace(" ", "") == "":
            await message.channel.send("Structure name can't be empty. Consult &help for more info.")
        else:
            embed = discord.Embed(title=f"{client.get_emoji(CustomEmojis.steve_alex_jumping)}Construction complete!"
                                        f"{client.get_emoji(CustomEmojis.steve_alex_jumping)}", color=0xFFEE00)

            if structure_name.lower() == "iron golem":
                embed.add_field(name=f"Here's your **Iron Golem**",
                                value=f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.carved_pumpkin)}\n"
                                      f"{client.get_emoji(CustomEmojis.iron_block)}{client.get_emoji(CustomEmojis.iron_block)}{client.get_emoji(CustomEmojis.iron_block)}\n"
                                      f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.iron_block)}")
                await message.channel.send(embed=embed)

            elif structure_name.lower() == "snow golem":
                embed.add_field(name=f"Here's your **Snow Golem**",
                                value=f"{client.get_emoji(CustomEmojis.carved_pumpkin)}\n"
                                      f"{client.get_emoji(763570364571320361)}\n{client.get_emoji(763570364571320361)}")
                await message.channel.send(embed=embed)

            elif structure_name.lower() == "tree":
                tree_type = random.randint(1, 6)

                if tree_type == 1:
                    embed.add_field(name=f"Here's your **Tree**",
                                    value=f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}\n"
                                          f"{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}\n"
                                          f"{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.oak_log)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.oak_log)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.oak_log)}")
                elif tree_type == 2:
                    embed.add_field(name=f"Here's your **Tree**",
                                    value=f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}\n"
                                          f"{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}\n"
                                          f"{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}\n"
                                          f"{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}{client.get_emoji(CustomEmojis.oak_leave)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.oak_log)}")
                elif tree_type == 3:
                    embed.add_field(name=f"Here's your **Tree**",
                                    value=f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}\n"
                                          f"{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}\n"
                                          f"{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.birch_log)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.birch_log)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.birch_log)}")
                elif tree_type == 4:
                    embed.add_field(name=f"Here's your **Tree**",
                                    value=f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}\n"
                                          f"{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}\n"
                                          f"{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.birch_log)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.birch_log)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.birch_log)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.birch_log)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.birch_log)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.birch_log)}")
                elif tree_type == 5:
                    embed.add_field(name=f"Here's your **Tree**",
                                    value=f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}\n"
                                          f"{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}\n"
                                          f"{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}{client.get_emoji(CustomEmojis.birch_leaf)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.birch_log)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.birch_log)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.birch_log)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.birch_log)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.birch_log)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.birch_log)}")
                elif tree_type == 6:
                    embed.add_field(name=f"Here's your **Tree**",
                                    value=f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.spruce_leaf)}{client.get_emoji(CustomEmojis.spruce_leaf)}{client.get_emoji(CustomEmojis.spruce_leaf)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.spruce_log)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.spruce_leaf)}{client.get_emoji(CustomEmojis.spruce_leaf)}{client.get_emoji(CustomEmojis.spruce_leaf)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.spruce_leaf)}{client.get_emoji(CustomEmojis.spruce_leaf)}{client.get_emoji(CustomEmojis.spruce_leaf)}{client.get_emoji(CustomEmojis.spruce_leaf)}{client.get_emoji(CustomEmojis.spruce_leaf)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.spruce_log)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.spruce_leaf)}{client.get_emoji(CustomEmojis.spruce_leaf)}{client.get_emoji(CustomEmojis.spruce_leaf)}{client.get_emoji(CustomEmojis.spruce_leaf)}{client.get_emoji(CustomEmojis.spruce_leaf)}\n"
                                          f"{client.get_emoji(CustomEmojis.spruce_leaf)}{client.get_emoji(CustomEmojis.spruce_leaf)}{client.get_emoji(CustomEmojis.spruce_leaf)}{client.get_emoji(CustomEmojis.spruce_leaf)}{client.get_emoji(CustomEmojis.spruce_leaf)}{client.get_emoji(CustomEmojis.spruce_leaf)}{client.get_emoji(CustomEmojis.spruce_leaf)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.spruce_log)}\n"
                                          f"{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.air)}{client.get_emoji(CustomEmojis.spruce_log)}")

                await message.channel.send(embed=embed)

    if message.content.startswith(f"{prefix}wakeup"):
        target_member = await message.guild.fetch_member(message.content[11:-1])
        vc_list = [channel for channel in message.guild.channels if channel.type == ChannelType.voice]

        if target_member.bot:
            await message.channel.send("Why are you trying to wake up a bot? Are you dumb?")
        elif not target_member.voice:
            await message.channel.send("Can't find that guy/gal sorry")
        else:
            await message.channel.send(f"Ok waking up {target_member.name}")
            from random import randint
            for i in range(15):
                await target_member.move_to(vc_list[randint(0, len(vc_list) - 1)])


client.run("")

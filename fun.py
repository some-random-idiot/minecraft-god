import discord
import random
from chest import CustomEmojis

client = discord.Client()
prefix = "&"


@client.event
async def on_ready():
    print("READY")


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith(f"{prefix}die"):
        await client.logout()

    if message.content.startswith("&build"):
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


client.run("")

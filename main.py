# Woah I'm actually doing something arguably productive now??? Ok enough of that.
import discord
import random
from chest import prefix
from chest import CustomEmojis

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Minecraft 10", url="https://www.twitch.tv/esl_csgo"))
    print("READY")


@client.event
async def on_message(message):
    # Check if message activity is due to other bots or itself.
    if message.author.bot:
        return

    if message.content.startswith(f"{prefix}help"):
        basic_cmds = ("```css\n"
                      "&help                             \n[Brings up this page]\n\n"
                      "&die                              \n[Shuts down the bot]"
                      "```")

        fun_cmds = ("```css\n"
                    "&build {:structure:}                \n[Builds the specified structure]\n\n"
                    "&wakeup {:user:}                    \n[Wake up a user by repeatedly changing their VC room]"
                    "```")

        util_cmds = ("```css\n"
                     "&skin {:username:}                \n[Grabs the skin of the specified user]"
                     "```")

        help_page = discord.Embed(title=f"{client.get_emoji(CustomEmojis.bookshelf)}Help page for cool gamers"
                                        f"{client.get_emoji(CustomEmojis.bookshelf)}", type="rich", description="Educate yourself.",
                                  colour=0xC38229)
        help_page.add_field(name=f"{client.get_emoji(CustomEmojis.grass_block)} **Basics**", value=basic_cmds)
        help_page.add_field(name=f"{client.get_emoji(CustomEmojis.tnt)} **Fun**", value=fun_cmds)
        help_page.add_field(name=f"{client.get_emoji(CustomEmojis.workbench)} **Utilities**", value=util_cmds)

        await message.channel.send(embed=help_page)

    if message.content.startswith(f"{prefix}die"):
        if message.author.id == 372641106187255818:
            death_choice = random.randint(1, 11)
            death_msg = None
            if death_choice == 1:
                death_msg = discord.Embed(title="**Minecraft_God** *drowned*",
                                          description=f"{client.get_emoji(CustomEmojis.red_bed)} I'm shutting down",
                                          color=0xFF0000)
            elif death_choice == 2:
                death_msg = discord.Embed(title="**Minecraft_God** *blew up*",
                                          description=f"{client.get_emoji(CustomEmojis.red_bed)} I'm shutting down",
                                          color=0xFF0000)
            elif death_choice == 3:
                death_msg = discord.Embed(title="**Minecraft_God** *was blown up by* **Creeper**",
                                          description=f"{client.get_emoji(CustomEmojis.red_bed)} I'm shutting down",
                                          color=0xFF0000)
            elif death_choice == 4:
                death_msg = discord.Embed(title="**Minecraft_God** *hit the ground too hard*",
                                          description=f"{client.get_emoji(CustomEmojis.red_bed)} I'm shutting down",
                                          color=0xFF0000)
            elif death_choice == 5:
                death_msg = discord.Embed(title="**Minecraft_God** *was squashed by a falling anvil*",
                                          description=f"{client.get_emoji(CustomEmojis.red_bed)} I'm shutting down",
                                          color=0xFF0000)
            elif death_choice == 6:
                death_msg = discord.Embed(title="**Minecraft_God** *was squashed by a falling block*",
                                          description=f"{client.get_emoji(CustomEmojis.red_bed)} I'm shutting down",
                                          color=0xFF0000)
            elif death_choice == 7:
                death_msg = discord.Embed(title="**Minecraft_God** *went up in flames*",
                                          description=f"{client.get_emoji(CustomEmojis.red_bed)} I'm shutting down",
                                          color=0xFF0000)
            elif death_choice == 8:
                death_msg = discord.Embed(title="**Minecraft_God** *burned to death*",
                                          description=f"{client.get_emoji(CustomEmojis.red_bed)} I'm shutting down",
                                          color=0xFF0000)
            elif death_choice == 9:
                death_msg = discord.Embed(title="**Minecraft_God** *was struck by lightning*",
                                          description=f"{client.get_emoji(CustomEmojis.red_bed)} I'm shutting down",
                                          color=0xFF0000)
            elif death_choice == 10:
                death_msg = discord.Embed(title="**Minecraft_God** *suffocated in a wall*",
                                          description=f"{client.get_emoji(CustomEmojis.red_bed)} I'm shutting down",
                                          color=0xFF0000)

            await message.channel.send(embed=death_msg)
            await client.logout()
        else:
            await message.channel.send("You are not my makyr.")


client.run("")

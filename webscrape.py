import discord
from chest import prefix
from chest import CustomEmojis
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

client = discord.Client()

browserOption = Options()
browserOption.headless = True
browser = webdriver.Firefox("./", options=browserOption)


@client.event
async def on_ready():
    print("READY")


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith(f"{prefix}die"):
        await client.logout()

    if message.content.startswith(f"{prefix}skin"):
        username = message.content[6:]
        if username == "" or username.replace(" ", "") == "":
            await message.channel.send("Username can't be empty. Consult &help for more info.")
        else:
            await message.channel.send(f"Hold on...{client.get_emoji(CustomEmojis.compass)}")

            browser.get(f"https://minecraftskinstealer.com/profile/{username}")
            try:
                icon_link = browser.find_element_by_xpath('/html/body/div[8]/div/div/div[1]/div[3]/div/div[1]/div/div[1]/div/img').get_attribute("src")
                skin_link = browser.find_element_by_xpath('//*[@id="fullbody-skin-render"]').get_attribute("src")
            except:
                await message.channel.send(f"{client.get_emoji(CustomEmojis.barrier)} User **{username}** not found. "
                                           f"Please try again.{client.get_emoji(CustomEmojis.barrier)}")

            embed = discord.Embed(title=f"{client.get_emoji(CustomEmojis.steve)}User found! Here you go.{client.get_emoji(CustomEmojis.alex)}",
                                  type="rich", color=0x009AFF)
            embed.add_field(name=f"Displaying the skin of user **{username}**",
                            value=f"[Download](https://minecraftskinstealer.com/api/v1/skin/download/skin/{username})")
            embed.set_thumbnail(url=icon_link)
            embed.set_image(url=skin_link)
            embed.set_footer(text="Scraped from https://minecraftskinstealer.com/")
            await message.channel.send(embed=embed)


client.run("")

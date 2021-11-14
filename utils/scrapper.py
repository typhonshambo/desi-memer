import discord
import requests

def ranMeme():
    request = requests.get("https://meme-api.herokuapp.com/gimme/")
    data = request.json()

    postLink = data['postLink']
    title = data['title']
    url = data['url']
    ups = data['ups']
    nsfw = data['nsfw']

    embed  = discord.Embed(
        color=discord.Colour.random(),
        title = title,
        timestamp=discord.utils.utcnow()
    )
    embed.set_image(url=url)
    embed.set_footer(text=f"👍 {ups}")

    return embed


def desiMeme():
    request = requests.get("https://meme-api.herokuapp.com/gimme/IndianDankMemes/")
    data = request.json()

    postLink = data['postLink']
    title = data['title']
    url = data['url']
    ups = data['ups']
    nsfw = data['nsfw']

    embed  = discord.Embed(
        color=discord.Colour.random(),
        title = title,
        timestamp=discord.utils.utcnow()
    )
    embed.set_image(url=url)
    embed.set_footer(text=f"👍 {ups}")

    return embed


from discord.ext import commands

import discord

class General(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="room", help="Usage: $room <code> <server> -> Broadcast an available room, example: $room XFDS Europa")
	async def room(self, ctx, code, server):
		voice = ctx.message.author.voice
		if voice == None:
			e = discord.Embed(title=f':x: You must to be in a Voice Channel \n', colour=discord.Colour(0xcc1818))
			await ctx.send('', embed=e)
			return
		voice_name = ctx.message.author.voice.channel.name
		quantity = 10 - len(voice.channel.members)
		
		title = ':white_check_mark: Room is available:'
		description = f'{code} Server {server} | Channel {voice_name} | Places {quantity}'
		e = discord.Embed(title=title, type="rich", description=description, colour=discord.Colour(0x09c49c))
		await ctx.send('', embed=e)

	@commands.command(name="funas", help="Usage: $funas -> Print the better five Impostor from this server")
	async def funas(self, ctx):
		funades = ["Pia 'muchotexto'", "Bryan 'ArAmIx'", "Javier 'koga'", "Catalina 'catasinbri'", "Kevin 'rojo'"]
		title = ":eyes: Funades list:"
		people_list = ""
		for names in funades:
			people_list += names + " \n"
		people_list += "\n Congrats to be the best five Impostor of the week! :fire:"
		e = discord.Embed(title=title, type="rich", description=people_list, colour=discord.Colour(0x09c48c))
		await ctx.send('', embed=e)
			
def setup(bot):
	bot.add_cog(General(bot))

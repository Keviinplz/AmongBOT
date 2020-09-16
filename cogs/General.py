from discord.ext import commands

import discord

class General(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	async def print_list(self, ctx, list_people, title, description):
		names_to_str_builder = ""
		for names in list_people:
			names_to_str_builder += names + '\n'
		names_to_str_builder += '\n' + description + '\n'
		e = discord.Embed(title=title, type="rich", description=names_to_str_builder, colour=discord.Colour(0x09c48c))
		await ctx.send('', embed=e)

	@commands.command(name="room", help="Usage: $room <code> <server> -> Broadcast an available room, example: $room XFDS Europa")
	async def room(self, ctx, code, server):
		voice = ctx.message.author.voice
		if voice == None:
			e = discord.Embed(description=f':x: You must to be in a Voice Channel \n', colour=discord.Colour(0xcc1818))
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
		cancel_list = ["Javier 'koga'", "Brayan 'L'", "Bastian 'Basti'", "Catalina 'catasinbri'", "Melanie 'melanie'"]
		title = "Best Impostors of the Week"
		description = ":fire: Congrats y'all"
		self.print_list(ctx, cancel_list, title, description)
	
	@commands.command(name="honor", help="Usage: $honor -> Print honorific people of this server")
	async def honor(self, ctx):
		honor_list = ["Pía 'muchotexto'", "Javier 'koga'", "Brayan 'ArAmIx'", "Kevin 'rojo'", "Catalina 'catasinbri'"]
		title = "Hall of Honor"
		description = ":love: Honorific people of the server"
		self.print_list(ctx, honor_list, title, description)
def setup(bot):
	bot.add_cog(General(bot))

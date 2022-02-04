from http import client
from discord.ext import commands
import discord, os, json
from discord.ext import commands
import datetime as datetime
from discord_components import (DiscordComponents, Button, ButtonStyle, Select, SelectOption)

@commands.command('ch')
@commands.has_permissions(administrator=True) #permissions
async def ch(ctx, user : discord.Member, *, role : discord.Role):
  if role in user.roles:
      await user.remove_roles(role) #removes the role if user already has
      await ctx.send(f"Removed {role} from {user.mention}")
  else:
      await user.add_roles(role) 
      await user.send(

          embed=discord.Embed(title='Welcome!', description=f'Welcome to **Valorant Customs** Hosts Team!', footer='Developed by Jute.#2022', color=255),
                components=[

                ])
        
      await ctx.send(f"Added {role} to {user.mention} and User DMed")
      channel = client.get_channel(929567004900352091)
      await channel.send(

          embed=discord.Embed(title='New Logs', description=f'{ctx.author} Add {user.mention} like Hosts.', footer='Developed by Jute.#2022', color=255),
                components=[

                ])


def ch(bot):
    bot.add_cog(ch(bot))
import discord
import typing
import datetime
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

@commands.guild_only()
class ChPlugin(commands.Cog):
    def __init__(self, bot):
        self.bot: discord.Client = bot
        self.db = bot.plugin_db.get_partition(self)
        self.mute_list = []

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
    

def setup(bot):
    bot.add_cog(ModerationPlugin(bot))

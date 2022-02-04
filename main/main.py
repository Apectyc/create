import discord
from discord.ext import commands

class DmOnJoinPlugin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

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
    
def ch(bot):
    bot.add_cog(ch(bot))
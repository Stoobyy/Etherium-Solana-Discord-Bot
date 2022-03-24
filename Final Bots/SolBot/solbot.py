import discord
from discord.utils import get
from discord.ext import commands
import time
import os
import json
from datetime import *
import requests 

prefix = '-' #Prefix here
client = commands.Bot(command_prefix = prefix,help_command=None)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="https://nftcop.io/"))
    print("Client Ready To Run - Command Prefix ! ")

@client.command(aliases=['latency'])
@commands.has_permissions(manage_messages=True)
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def register(ctx,address=None):
  if address==None:
    embed=discord.Embed(title='No address provided.',color=15277667)
    embed.add_field(name='Please rerun the command.',value=f'\n\n\n<:unknown_2:952949819612217454> [Our Website](http://nftcop.io)\n<:instagram:952950025737080892> [Our Instagram](https://www.instagram.com/nftcop.io/)\n<:Twitter:952950111548370995> [Our Twitter](https://twitter.com/mynftcop)',inline=False)
    embed.set_author(name='NFTCop - Whitelist Bot',icon_url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg') 
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg')
    await ctx.send(embed=embed)
  else:
    response=requests.get(f'https://public-api.solscan.io/account/{address}')
    raw=response.json()
    try:
      result=raw['lamports']
      result=float(result)
      with open('config.txt','r') as a:
        config=json.load(a)
      min=float(config['min'][0])
      if (result*0.000000001)>=min:
        with open('accounts.txt','r') as a:
          accounts=json.load(a)
        try:
          already=accounts[str(ctx.guild.id)][0].values()
        except:
          already=[]
        if ctx.author.id not in already:
          if str(ctx.guild.id) in accounts:
            if address in accounts[str(ctx.guild.id)][0]: 
              embed=discord.Embed(title='Duplicate Entry',color=15277667)
              embed.add_field(name='You cannot enter register the same address twice.',value=f'\n\n\n<:unknown_2:952949819612217454> [Our Website](http://nftcop.io)\n<:instagram:952950025737080892> [Our Instagram](https://www.instagram.com/nftcop.io/)\n<:Twitter:952950111548370995> [Our Twitter](https://twitter.com/mynftcop)',inline=False)
              embed.set_author(name='NFTCop - Whitelist Bot',icon_url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg') 
              embed.set_thumbnail(url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg')
              await ctx.send(embed=embed)
            else:
              with open('accounts.txt','w') as a:
                accounts[str(ctx.guild.id)][0].update({address:ctx.author.id})
                a.write(json.dumps(accounts))
              embed=discord.Embed(title='Successfully registered.',color=15277667)
              embed.add_field(name='Socials:', value='\n\n\n<:unknown_2:952949819612217454> [Our Website](http://nftcop.io)\n<:instagram:952950025737080892> [Our Instagram](https://www.instagram.com/nftcop.io/)\n<:Twitter:952950111548370995> [Our Twitter](https://twitter.com/mynftcop)')
              embed.set_author(name='NFTCop - Whitelist Bot',icon_url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg') 
              embed.set_thumbnail(url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg')
              await ctx.send(embed=embed)
          else:
            with open('accounts.txt','w') as a:
              accounts[str(ctx.guild.id)]=[{address:ctx.author.id}]
              a.write(json.dumps(accounts))
            embed=discord.Embed(title='Successfully registered.',color=15277667)
            embed.add_field(name='Socials:', value='\n\n\n<:unknown_2:952949819612217454> [Our Website](http://nftcop.io)\n<:instagram:952950025737080892> [Our Instagram](https://www.instagram.com/nftcop.io/)\n<:Twitter:952950111548370995> [Our Twitter](https://twitter.com/mynftcop)')
            embed.set_author(name='NFTCop - Whitelist Bot',icon_url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg') 
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg')
            await ctx.send(embed=embed)
        else:
          embed=discord.Embed(title='Error!',color=15277667)
          embed.add_field(name='You cannot register twice.',value=f'\n\n\n<:unknown_2:952949819612217454> [Our Website](http://nftcop.io)\n<:instagram:952950025737080892> [Our Instagram](https://www.instagram.com/nftcop.io/)\n<:Twitter:952950111548370995> [Our Twitter](https://twitter.com/mynftcop)',inline=False)
          embed.set_author(name='NFTCop - Whitelist Bot',icon_url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg') 
          embed.set_thumbnail(url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg')
          await ctx.send(embed=embed)
      else:
        embed=discord.Embed(title='Insufficient balance on account.',color=15277667)
        embed.add_field(name='Required Balance', value=f'`{min}`',inline=False)
        embed.add_field(name='Balance on account',value=f'`{result/1000000000000000000}`\n\n\n<:unknown_2:952949819612217454> [Our Website](http://nftcop.io)\n<:instagram:952950025737080892> [Our Instagram](https://www.instagram.com/nftcop.io/)\n<:Twitter:952950111548370995> [Our Twitter](https://twitter.com/mynftcop)',inline=False)
        embed.set_author(name='NFTCop - Whitelist Bot',icon_url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg') 
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg')
        await ctx.send(embed=embed)
    except:
      embed=discord.Embed(title='Invalid Solana Address!',color=15277667)
      embed.add_field(name='Please rerun the command.',value=f'\n\n\n<:unknown_2:952949819612217454> [Our Website](http://nftcop.io)\n<:instagram:952950025737080892> [Our Instagram](https://www.instagram.com/nftcop.io/)\n<:Twitter:952950111548370995> [Our Twitter](https://twitter.com/mynftcop)',inline=False)
      embed.set_author(name='NFTCop - Whitelist Bot',icon_url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg') 
      embed.set_thumbnail(url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg')
      await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def setminbalance(ctx,min=0.05):
  embed=discord.Embed(color=15277667)
  embed.add_field(name=f'Set Minimum Balance to {min}',value=f'\n\n\n<:unknown_2:952949819612217454> [Our Website](http://nftcop.io)\n<:instagram:952950025737080892> [Our Instagram](https://www.instagram.com/nftcop.io/)\n<:Twitter:952950111548370995> [Our Twitter](https://twitter.com/mynftcop)',inline=False)
  embed.set_author(name='NFTCop - Whitelist Bot',icon_url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg') 
  embed.set_thumbnail(url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg')
  await ctx.send(embed=embed)
  with open('config.txt','r') as a:
    config=json.load(a)
  with open('config.txt','w') as a:
    config['min']=[min]
    a.write(json.dumps(config))
    

@client.command()
@commands.has_permissions(manage_messages=True)
async def remove(ctx,address=None):
  if address==None:
    embed=discord.Embed(title='No address provided.',color=15277667)
    embed.add_field(name='Please rerun the command.',value=f'\n\n\n<:unknown_2:952949819612217454> [Our Website](http://nftcop.io)\n<:instagram:952950025737080892> [Our Instagram](https://www.instagram.com/nftcop.io/)\n<:Twitter:952950111548370995> [Our Twitter](https://twitter.com/mynftcop)',inline=False)
    embed.set_author(name='NFTCop - Whitelist Bot',icon_url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg') 
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg')
    await ctx.send(embed=embed)
  else:
    with open('accounts.txt','r') as a:
      list1=json.load(a)
    for i in list1[str(ctx.guild.id)][0]:
      if i==address:
        del list1[str(ctx.guild.id)][0][address]
        await ctx.message.add_reaction('👍')
        break
    with open('accounts.txt','w') as a:
      a.write(json.dumps(list1))

      
@client.command()
@commands.has_permissions(manage_messages=True)
async def view(ctx):
  with open('accounts.txt','r') as a:
    accs=json.load(a)
  try:
    embed=discord.Embed(title='All addresses',color=15277667)
    for i in range(len(accs[str(ctx.guild.id)][0])):
      embed.add_field(name=list(accs[str(ctx.guild.id)][0].keys())[i],value=f'Registered by <@{list(accs[str(ctx.guild.id)][0].values())[i]}>',inline=True)
    embed.add_field(name='Socials:',value=f'\n\n\n<:unknown_2:952949819612217454> [Our Website](http://nftcop.io)\n<:instagram:952950025737080892> [Our Instagram](https://www.instagram.com/nftcop.io/)\n<:Twitter:952950111548370995> [Our Twitter](https://twitter.com/mynftcop)',inline=False)
    embed.set_author(name='NFTCop - Whitelist Bot',icon_url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg') 
    await ctx.send(embed=embed)
  except:
    embed=discord.Embed(title='No Addresses found!',color=15277667)
    embed.add_field(name='Socials:',value=f'\n\n\n<:unknown_2:952949819612217454> [Our Website](http://nftcop.io)\n<:instagram:952950025737080892> [Our Instagram](https://www.instagram.com/nftcop.io/)\n<:Twitter:952950111548370995> [Our Twitter](https://twitter.com/mynftcop)',inline=False)
    embed.set_author(name='NFTCop - Whitelist Bot',icon_url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg') 
    await ctx.send(embed=embed)

    
@client.command()
@commands.has_permissions(manage_messages=True)
async def balance(ctx):
  with open('config.txt','r') as a:
    config=json.load(a)
  try:
    balance=config['min'][0]
  except:
    balance='No balance set.'
  embed=discord.Embed(title=f'Current balance is {balance}',color=15277667)
  embed.add_field(name='Socials:',value=f'\n\n\n<:unknown_2:952949819612217454> [Our Website](http://nftcop.io)\n<:instagram:952950025737080892> [Our Instagram](https://www.instagram.com/nftcop.io/)\n<:Twitter:952950111548370995> [Our Twitter](https://twitter.com/mynftcop)',inline=False)
  embed.set_author(name='NFTCop - Whitelist Bot',icon_url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg') 
  await ctx.send(embed=embed)
    
@client.command()
@commands.has_permissions(manage_messages=True)
async def export(ctx):
  with open('accounts.txt','r') as a:
    accounts=json.load(a)
  accounts=accounts[str(ctx.guild.id)][0]
  with open('accounts1.json','w') as b:
    b.write(json.dumps(accounts,indent=2))
  await ctx.send(file=discord.File('accounts1.json'))

@client.command()
async def reset(ctx):
  with open('accounts.txt','r') as a:
    accounts=json.load(a)
  del accounts[str(ctx.guild.id)]
  with open('accounts.txt','w') as a:
    a.write(json.dumps(accounts))
  await ctx.message.add_reaction('👍')
  
@client.command()
@commands.has_permissions(manage_messages=True)
async def help(ctx):
  embed=discord.Embed(title='Help Menu',color=15277667)
  embed.add_field(name='-setminbalance',value='Sets the minimum balance')
  embed.add_field(name='-register',value='Adds your address to the database')
  embed.add_field(name='-balance',value='Shows currently set minimum balance')
  embed.add_field(name='-remove',value='Removes an address from the database')
  embed.add_field(name='-view',value='Lists all addresses along with balance')
  embed.add_field(name='-export',value='Exports addresses as json.')
  embed.add_field(name='-reset',value='Erases the DB of the current server.')
  embed.add_field(name='Socials:',value=f'\n\n\n<:unknown_2:952949819612217454> [Our Website](http://nftcop.io)\n<:instagram:952950025737080892> [Our Instagram](https://www.instagram.com/nftcop.io/)\n<:Twitter:952950111548370995> [Our Twitter](https://twitter.com/mynftcop)',inline=False)
  embed.set_author(name='NFTCop - Whitelist Bot',icon_url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg') 
  embed.set_thumbnail(url='https://media.discordapp.net/attachments/952897208699727945/953974973259730974/solanas.jpg')
  await ctx.send(embed=embed)

client.run('') #Enter token here

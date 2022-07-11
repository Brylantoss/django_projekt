import hikari


bot = hikari.GatewayBot(token='OTk0NjU5NTc0MjM5OTg1NzM3.GRoZdA.AHSn1akkAL2eKb6L8LmLIckfakUyrRfvPAh_2s')
# NASŁUCHIWANIE KANAŁÓW


@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    a = event.content
    print(a)

    # @bot.listen(hikari.GuildMessageCreateEvent)
    # async def print_message(event):   
    #     b=event.content
    #     print('Zgloszenie '+ a +' zostalo przyjete')
    #print(event.content)


#Info od konsoli na temat bota
@bot.listen(hikari.StartedEvent)
async def bot_started(event = True):
    if event == True:
        print('Error')
    else:
        print('Bot is running...')

bot.run()



# import discord
# from discord.ext import commands

# client = commands.Bot(command_prefix= "?")
# client.remove_command("help")

# @client.event
# async def on_ready():
#     print("Bot is running...")



# @client.command()
# async def help(ctx):
#     await ctx.channel.send("Pomoc")

# client.run("OTk0NjU5NTc0MjM5OTg1NzM3.GIdqp_.2UPO-6UyZ2WGVM4Z5nHMUaVJBTmImddvbLGi0w")




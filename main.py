from configs import Config
from pyrogram import Client, filters, idle
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent
from TeamTeleRoid.forcesub import ForceSub
import asyncio

# Bot Client for Inline Search
Bot = Client(
    session_name=Config.Mdisk_search_filter_bot,
    api_id=Config.23098568,
    api_hash=Config.cb7098aa919c29da3e5f9af0f9086dd7,
    bot_token=Config.5809851448:AAEgTfUAhi8uytQjCSH2aJrpCSeciUMzkNg
)

# User Client for Searching in Channel.
User = Client(
    session_name=Config.1BVtsOL4Bu8UNyJ-TIOIvyDAJi4lzcDBjMmvc_xYC2MgZSYR1kNl2eFtrp4hgvAW4u0-RuDe4QbNMZDAX48EwZN__qqeTUBPeFAvN8XLcFvqBOJhzvNjezgsQm85BiKpW8dlOtruTLwLG_Hsctx21ZdjuCapMYyRJMx7dgms7VA2Da9Bm30M6gAliuZas1V2s09JybCci6Ml3qsv3wS4Up38zv8mEEuk1t_AbSy51KH4hBQKSZwi9JqbGsHeHa5crNKy8Ua7Aw1cluNAw3fICTQySkKctdd5fC9YzDOo84xuml1t0uRtm58GsBn1-yIJxuOMf6N9rnn9gcwiivHIVjXXqrrnMtYs=,
    api_id=Config.23098568,
    api_hash=Config.cb7098aa919c29da3e5f9af0f9086dd7
)

@Bot.on_message(filters.private & filters.command("start"))
async def start_handler(_, event: Message):
	await event.reply_photo("https://telegra.ph/file/19eeb26fa2ce58765917a.jpg",
                                caption=Config.START_MSG.format(event.from_user.mention),
                                reply_markup=InlineKeyboardMarkup([
					[InlineKeyboardButton('❤ Donation Link', url='https://t.me/ideal_bot_father')],
					[InlineKeyboardButton("Updates 𝙲𝚑𝚊𝚗𝚗𝚊𝚕", url="https://t.me/ideal_bot_father")],
					[InlineKeyboardButton("Donation", callback_data="Help_msg"),
                                        InlineKeyboardButton("About", callback_data="About_msg")]
				]))

@Bot.on_message(filters.private & filters.command("help"))
async def help_handler(_, event: Message):

    await event.reply_text(Config.ABOUT_HELP_TEXT.format(event.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
		[InlineKeyboardButton('❤ Donation Link', url='https://t.me/ideal_bot_father')
	 ],[InlineKeyboardButton("Updates 𝙲𝚑𝚊𝚗𝚗𝚊𝚕", url="https://t.me/ideal_bot_father"), 
             InlineKeyboardButton("𝙰𝚋𝚘𝚞𝚝", callback_data="About_msg")]
        ])
    )

@Bot.on_message(filters.incoming)
async def inline_handlers(_, event: Message):
    if event.text == '/start':
        return
    answers = f'**📂 Results For ➠ {event.text} \n\n➠ Type Only Movie Name With Correct Spelling.✍️\n➠ Add Year For Better Result.🗓️\n➠ Join @ideal_bot_father\n▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n\n**'
    async for message in User.search_messages(chat_id=Config.-1001844687848, limit=50, query=event.text):
        if message.text:
            thumb = None
            f_text = message.text
            msg_text = message.text.html
            if "|||" in message.text:
                f_text = message.text.split("|||", 1)[0]
                msg_text = message.text.html.split("|||", 1)[0]
            answers += f'**🍿 Title ➠ ' + '' + f_text.split("\n", 1)[0] + '' + '\n\n📜 About ➠ ' + '' + f_text.split("\n", 2)[-1] + ' \n\n▰▱▰▱▰▱▰▱▰▱▰▱▰▱\nLink Will Auto Delete In 60Sec...⏰\n\n**'
    try:
        msg = await event.reply_text(answers)
        await asyncio.sleep(65)
        await event.delete()
        await msg.delete()
    except:
        print(f"[{Config.BOT_SESSION_NAME}] - Failed to Answer - {event.from_user.first_name}")


@Bot.on_callback_query()
async def button(bot, cmd: CallbackQuery):
        cb_data = cmd.data
        if "About_msg" in cb_data:
            await cmd.message.edit(
			text=Config.ABOUT_BOT_TEXT,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton('❤ Donation Link', url='https://t.me/ideal_bot_father')
					],
					[
						InlineKeyboardButton("Updates 𝙲𝚑𝚊𝚗𝚗𝚊𝚕", url="https://t.me/ideal_bot_father")
					],
					[
						InlineKeyboardButton("Home", callback_data="gohome")
					]
				]
			),
			parse_mode="html"
		)
        elif "Help_msg" in cb_data:
            await cmd.message.edit(
			text=Config.ABOUT_HELP_TEXT,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
					InlineKeyboardButton('❤ Donation Link', url='https://t.me/ideal_bot_father')
					],
					[
					InlineKeyboardButton("Updates 𝙲𝚑𝚊𝚗𝚗𝚊𝚕", url="https://t.me/ideal_bot_father")
					], 
                                        [
					InlineKeyboardButton("Home", callback_data="gohome"),
					InlineKeyboardButton("About", callback_data="About_msg")
					]
				]
			),
			parse_mode="html"
		)
        elif "gohome" in cb_data:
            await cmd.message.edit(
			text=Config.START_MSG.format(cmd.from_user.mention),
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
                                        [
					InlineKeyboardButton('❤ Donation Link', url='https://t.me/ideal_bot_father')
					],
					[
					InlineKeyboardButton("Updates 𝙲𝚑𝚊𝚗𝚗𝚊𝚕", url="https://t.me/ideal_bot_father")
					],
					[
					InlineKeyboardButton("Donation", callback_data="Help_msg"),
					InlineKeyboardButton("About", callback_data="About_msg")
					]
				]
			),
			parse_mode="html"
		)

# Start Clients
Bot.start()
User.start()
# Loop Clients till Disconnects
idle()
# After Disconnects,
# Stop Clients
Bot.stop()
User.stop()

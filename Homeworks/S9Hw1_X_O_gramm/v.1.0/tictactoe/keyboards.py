from aiogram import types


def player_select_keyboard():
    buttons = [
        types.InlineKeyboardButton(text="X", callback_data="player_X"),
        types.InlineKeyboardButton(text="0", callback_data="player_0"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def turn_keyboard(turns: list):
    buttons = [
        types.InlineKeyboardButton(text=f"{turns[0]}", callback_data="turn_0"),
        types.InlineKeyboardButton(text=f"{turns[1]}", callback_data="turn_1"),
        types.InlineKeyboardButton(text=f"{turns[2]}", callback_data="turn_2"),
        types.InlineKeyboardButton(text=f"{turns[3]}", callback_data="turn_3"),
        types.InlineKeyboardButton(text=f"{turns[4]}", callback_data="turn_4"),
        types.InlineKeyboardButton(text=f"{turns[5]}", callback_data="turn_5"),
        types.InlineKeyboardButton(text=f"{turns[6]}", callback_data="turn_6"),
        types.InlineKeyboardButton(text=f"{turns[7]}", callback_data="turn_7"),
        types.InlineKeyboardButton(text=f"{turns[8]}", callback_data="turn_8"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    return keyboard

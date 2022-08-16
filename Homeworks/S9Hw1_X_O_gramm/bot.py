import logging
from os import getenv
from random import randint
from sys import exit

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token)

dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


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


class TicTacToe(StatesGroup):
    waiting_for_player_select = State()
    waiting_for_turn = State()
    waiting_for_game_end = State()


def cpu_turn(cpu_id: str, turns: list) -> list:
    ready = True if " " in turns else False
    while ready:
        turn = randint(0, 8)
        if turns[turn] == " ":
            turns[turn] = cpu_id
            return turns


def game_win(player_id: str, turns: list) -> bool:
    win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    player_combinations = list()

    for i in range(0, len(turns)):
        if turns[i] == player_id:
            player_combinations.append(i)

    for i in win_combinations:
        if set(i).issubset(player_combinations):
            return True


@dp.message_handler(commands="start", state="*")
async def cmd_start(message: types.Message):
    await message.answer("Выберите, будете играть X или 0", reply_markup=player_select_keyboard())
    await TicTacToe.waiting_for_player_select.set()


@dp.callback_query_handler(Text(startswith="player_"), state=TicTacToe.waiting_for_player_select)
async def player_select(call: types.CallbackQuery, state: FSMContext):
    action = call.data.split("_")[1]
    empty_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    if action == "X":
        await call.message.answer("Ок, играешь крестиками!")
        await state.update_data(player=action)
        await TicTacToe.next()
        await state.update_data(turns=empty_list)
        turns_dict = await state.get_data()
        await call.message.answer("Делайте ваш ход!", reply_markup=turn_keyboard(turns_dict['turns']))
    elif action == "0":
        await call.message.answer("Ок, играешь ноликами!")
        await state.update_data(player=action)
        await state.update_data(turns=cpu_turn("X", empty_list))
        turns_dict = await state.get_data()
        await call.message.answer("Делайте ваш ход!", reply_markup=turn_keyboard(turns_dict['turns']))
        await TicTacToe.next()
    await call.answer()


@dp.callback_query_handler(Text(startswith="turn_"), state=TicTacToe.waiting_for_turn)
async def next_turn(call: types.CallbackQuery, state: FSMContext):
    turns_dict = await state.get_data()
    if turns_dict['player'] == "X" and turns_dict['turns'][int(call.data.split("_")[1])] == ' ':
        turns_dict['turns'][int(call.data.split("_")[1])] = 'X'
        if game_win('X', turns_dict['turns']):
            await call.message.answer("Выиграли крестики! Конец игры!", reply_markup=turn_keyboard(turns_dict['turns']))
            return
        await state.update_data(turns=turns_dict['turns'])
        await state.update_data(turns=cpu_turn("0", turns_dict['turns']))
    elif turns_dict['player'] == "0" and turns_dict['turns'][int(call.data.split("_")[1])] == ' ':
        turns_dict['turns'][int(call.data.split("_")[1])] = '0'
        if game_win('0', turns_dict['turns']):
            await call.message.answer("Выиграли нолики! Конец игры!", reply_markup=turn_keyboard(turns_dict['turns']))
            return
        await state.update_data(turns=turns_dict['turns'])
        await state.update_data(turns=cpu_turn("Х", turns_dict['turns']))
    else:
        await call.message.answer("Упс! Здесь уже кто-то походил, попробуйте снова!")

    await call.message.answer("Делайте ваш ход!", reply_markup=turn_keyboard(turns_dict['turns']))
    await call.answer()


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)

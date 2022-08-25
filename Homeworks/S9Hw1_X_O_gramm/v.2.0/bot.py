import logging
from asyncio import sleep
from os import getenv
from sys import exit

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from tictactoe import *

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token)

dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


class TicTacToe(StatesGroup):
    waiting_for_player_select = State()
    player_turn = State()
    game_end = State()


@dp.message_handler(commands="help", state="*")
async def help_center(message: types.Message):
    await message.reply(f"{message.from_user.username}, пока я только умею по команде:\n"
                        f"/start - начать новую партеечку " + emoji.emojize(':hand_with_fingers_splayed:'))


@dp.message_handler(commands="start", state="*")
async def cmd_start(message: types.Message):
    await message.answer(f"{message.from_user.username}, выберите уровень сложности бота",
                         reply_markup=difficulty_select_keyboard())
    await TicTacToe.waiting_for_player_select.set()


@dp.callback_query_handler(Text(startswith="cpu_"), state=TicTacToe.waiting_for_player_select)
async def difficulty_select(call: types.CallbackQuery, state: FSMContext):
    action = call.data.split("_")[1]
    if action == 'noob':
        await state.update_data(cpu_level='noob')
    elif action == 'god':
        await state.update_data(cpu_level='god')
    await call.answer()
    await call.message.answer(f"Выберите, будете играть крестиками или ноликами",
                              reply_markup=player_select_keyboard())


@dp.callback_query_handler(Text(startswith="player_"), state=TicTacToe.waiting_for_player_select)
async def player_select(call: types.CallbackQuery, state: FSMContext):
    action = call.data.split("_")[1]
    empty_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    if action == 'X':
        await call.message.answer(f"Ок, играешь крестиками!")
        await state.update_data(player=action)
        await TicTacToe.next()
        await state.update_data(turns=empty_list)
        game_states = await state.get_data()
        await call.answer()
        await call.message.answer("Делайте ваш ход!", reply_markup=turn_keyboard(game_states['turns']))
    elif action == '0':
        game_states = await state.get_data()
        await call.message.answer("Ок, играешь ноликами!")
        await state.update_data(player=action)
        await call.answer()
        await call.message.answer("Бот обдумывает ход...")
        await state.update_data(turns=cpu_turn('X', empty_list, game_states['cpu_level']))
        game_states = await state.get_data()
        await call.message.answer("Делайте ваш ход!", reply_markup=turn_keyboard(game_states['turns']))
        await TicTacToe.next()


@dp.callback_query_handler(Text(startswith="turn_"), state=TicTacToe.player_turn)
async def next_turn(call: types.CallbackQuery, state: FSMContext):
    game_states = await state.get_data()
    if game_states['player'] == 'X' and game_states['turns'][int(call.data.split("_")[1])] == ' ':
        game_states['turns'][int(call.data.split("_")[1])] = 'X'
        await state.update_data(turns=game_states['turns'])
        if game_win('X', game_states['turns']):
            await call.message.answer("Вы выиграли! Поздравляем! " + emoji.emojize(":confetti_ball:"),
                                      reply_markup=turn_keyboard(game_states['turns']))
            await call.message.answer("Ваша награда " + emoji.emojize(":trophy:"))
            await types.ChatActions.upload_photo()
            await call.message.answer_photo(f'https://yandex.ru/images/search?text={cat_dictionary()}')
            await TicTacToe.next()
            await types.ChatActions.typing()
            await sleep(1)
            await call.message.answer(f"Может еще партеечку?\n"
                                      f"Для начала нажми /start " + emoji.emojize(':winking_face:'))
            return
        elif ' ' not in game_states['turns']:
            await call.message.answer("Ничья! Конец игры!", reply_markup=turn_keyboard(game_states['turns']))
            await TicTacToe.next()
            await types.ChatActions.typing()
            await sleep(1)
            await call.message.answer(f"Может еще партеечку?\n"
                                      f"Для начала нажми /start " + emoji.emojize(':winking_face:'))
            return
        await call.message.answer("Бот обдумывает ход...")
        await state.update_data(turns=cpu_turn('0', game_states['turns'], game_states['cpu_level']))

        if game_win('0', game_states['turns']):
            await call.message.answer("Вы проиграли! Как вы могли... " + emoji.emojize(':see-no-evil_monkey:'),
                                      reply_markup=turn_keyboard(game_states['turns']))
            await TicTacToe.next()
            await types.ChatActions.typing()
            await sleep(1)
            await call.message.answer(f"Может еще партеечку?\n"
                                      f"Для начала нажми /start " + emoji.emojize(':winking_face:'))
            return
        elif ' ' not in game_states['turns']:
            await call.message.answer("Ничья! Конец игры!", reply_markup=turn_keyboard(game_states['turns']))
            await TicTacToe.next()
            await types.ChatActions.typing()
            await sleep(1)
            await call.message.answer(f"Может еще партеечку?\n"
                                      f"Для начала нажми /start " + emoji.emojize(':winking_face:'))
            return

    elif game_states['player'] == '0' and game_states['turns'][int(call.data.split("_")[1])] == ' ':
        game_states['turns'][int(call.data.split("_")[1])] = '0'
        await state.update_data(turns=game_states['turns'])
        if game_win('0', game_states['turns']):
            await call.message.answer("Вы выиграли! Поздравляем! " + emoji.emojize(":confetti_ball:"),
                                      reply_markup=turn_keyboard(game_states['turns']))
            await call.message.answer("Ваша награда " + emoji.emojize(":trophy:"))
            await types.ChatActions.upload_photo()
            await call.message.answer_photo(f'https://yandex.ru/images/search?text={cat_dictionary()}')
            await TicTacToe.next()
            await types.ChatActions.typing()
            await sleep(1)
            await call.message.answer(f"Может еще партеечку?\n"
                                      f"Для начала нажми /start " + emoji.emojize(':winking_face:'))
            return
        elif ' ' not in game_states['turns']:
            await call.message.answer("Ничья! Конец игры!", reply_markup=turn_keyboard(game_states['turns']))
            await TicTacToe.next()
            await types.ChatActions.typing()
            await sleep(1)
            await call.message.answer(f"Может еще партеечку?\n"
                                      f"Для начала нажми /start " + emoji.emojize(':winking_face:'))
            return
        await call.message.answer("Бот обдумывает ход...")
        await state.update_data(turns=cpu_turn('X', game_states['turns'], game_states['cpu_level']))

        if game_win('X', game_states['turns']):
            await call.message.answer("Вы проиграли! Как вы могли... " + emoji.emojize(':see-no-evil_monkey:'),
                                      reply_markup=turn_keyboard(game_states['turns']))
            await TicTacToe.next()
            await types.ChatActions.typing()
            await sleep(1)
            await call.message.answer(f"Может еще партеечку?\n"
                                      f"Для начала нажми /start " + emoji.emojize(':winking_face:'))
            return
        elif ' ' not in game_states['turns']:
            await call.message.answer("Ничья! Конец игры!", reply_markup=turn_keyboard(game_states['turns']))
            await TicTacToe.next()
            await types.ChatActions.typing()
            await sleep(1)
            await call.message.answer(f"Может еще партеечку?\n"
                                      f"Для начала нажми /start " + emoji.emojize(':winking_face:'))
            return
    else:
        await call.message.answer("Упс! Здесь уже кто-то походил, попробуйте снова!")

    await call.message.answer("Делайте ваш ход!", reply_markup=turn_keyboard(game_states['turns']))
    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

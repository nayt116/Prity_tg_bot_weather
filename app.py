import config
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from pyowm import OWM


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
	strat_buttons = ['get weather', 'random']
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add(*strat_buttons)

	await message.answer('please choose...', reply_markup=markup)


@dp.message_handler(Text(equals = 'get weather'))
async def get_weather(message: types.Message):
	place = 'London'

	owm = OWM('9a7464ab1d4d8e55ec5d154990e18b64')
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place('London,GB')
	w = observation.weather
	temp = w.temperature('celsius')['temp']

	await message.answer('В городе: ' + place + 'сейчас' + str(temp) + ' градусов!')


@dp.message_handler(Text(equals='random'))
async def get_random_number(message: types.Message):
	rn = str(random.randint(1, 100000))
	await message.answer(rn)


if __name__=='__main__':
	executor.start_polling( dp, skip_updates=False )
#Модуль с обработчиком любых других запросов
#которые не попали в другие обработчики


from aiogram import Router
from aiogram.types import Message


router= Router()


#Этот хэндлер будет реагировать на любые сообщения
#не продусмотренные логикой работы бота
@router.message()
async def send_echo(message: Message):
    await message.answer(f"Это эхо! {message.text}")

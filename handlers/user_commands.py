from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards import inline_keyboards


router = Router()


@router.message(CommandStart())
async def start_com(message: Message):
    await message.answer("Добрый день!\n\nПожалуйста, выберите профиль, под которым Вы будете размечать фотографии!", 
                         reply_markup=inline_keyboards.doc_paginator())


@router.message()
async def echo(message: Message):
    await message.answer("Я вас не понимаю!")
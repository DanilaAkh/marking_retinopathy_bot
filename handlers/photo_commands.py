from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile

from keyboards import inline_keyboards
from data import db_connection

router = Router()


@router.callback_query(inline_keyboards.Doc_pagination.filter(F.action.in_(["first", "second", "third"])))
async def pagination_handler(call: CallbackQuery, callback_data: inline_keyboards.Doc_pagination):
    doc_num = int(callback_data.doc)
    doc = doc_num

    if callback_data.action == "second":
        doc = doc_num + 1
    elif callback_data.action == "third":
        doc = doc_num + 2

    image_data = await db_connection.get_image(doc)
    if image_data["name"] == "eof":
        await call.message.answer("Пока что нет неразмеченных фотографий!")
    else:
        image_name = image_data["name"]
        image = FSInputFile(f".\\data\\images\\{image_name}")
        await call.message.answer_photo(image,
                                        caption=f"Выберите один из вариантов:",
                                        reply_markup=inline_keyboards.photo_paginator(doc=doc, id=image_data["id"])
        )
    await call.answer()


@router.callback_query(inline_keyboards.Photo_pagination.filter(F.action.in_(["healthy", "stage1", "stage2", "stage3"])))
async def pagination_handler(call: CallbackQuery, callback_data: inline_keyboards.Photo_pagination):
    stage_num = int(callback_data.stage)
    doc = int(callback_data.doc)
    id = int(callback_data.id)
    stage = stage_num

    if callback_data.action == "stage1":
        stage = stage_num + 1
    elif callback_data.action == "stage2":
        stage = stage_num + 2
    elif callback_data.action == "stage3":
        stage = stage_num + 3
    
    await db_connection.insert_stage_to_db(id, doc, stage)

    image_data = await db_connection.get_image(doc)

    if image_data["name"] == "eof":
        await call.message.answer("Пока что нет неразмеченных фотографий!")
    else:
        image_name = image_data["name"]
        image = FSInputFile(f".\\data\\images\\{image_name}")
        await call.message.answer_photo(image,
                                        caption=f"Выберите один из вариантов:",
                                        reply_markup=inline_keyboards.photo_paginator(doc=doc, stage=stage_num, id=image_data["id"])
        )
    await call.answer()
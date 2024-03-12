from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class Doc_pagination(CallbackData, prefix="doc"):
    action: str
    doc: int


def doc_paginator(doc: int = 1):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Доктор 1", callback_data=Doc_pagination(action="first", doc=doc).pack()),
        InlineKeyboardButton(text="Доктор 2", callback_data=Doc_pagination(action="second", doc=doc).pack()),
        InlineKeyboardButton(text="Доктор 3", callback_data=Doc_pagination(action="third", doc=doc).pack())
    )
    return builder.as_markup()


class Photo_pagination(CallbackData, prefix="photo"):
    action: str
    stage: int
    doc: int
    id: int


def photo_paginator(id: int = 1, doc: int = 1, stage: int = 0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Здоров",
                             callback_data=Photo_pagination(action="healthy", stage=stage, doc=doc, id=id).pack()),
        InlineKeyboardButton(text="Стадия I",
                             callback_data=Photo_pagination(action="stage1", stage=stage, doc=doc, id=id).pack()),
        InlineKeyboardButton(text="Стадия II",
                             callback_data=Photo_pagination(action="stage2", stage=stage, doc=doc, id=id).pack()),
        InlineKeyboardButton(text="Стадия III",
                             callback_data=Photo_pagination(action="stage3", stage=stage, doc=doc, id=id).pack()),
        width=2
    )
    return builder.as_markup()
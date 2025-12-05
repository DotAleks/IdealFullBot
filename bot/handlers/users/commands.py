from aiogram import Router
from aiogram.filters.command import CommandStart,Command
from aiogram.types import Message

from core.strings import CMD_START_MESSAGE,CMD_HELP_MESSAGE


router = Router(name='user_commands_router')

@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(CMD_START_MESSAGE)

@router.message(Command('help'))
async def cmd_help(message: Message) -> None:
    await message.answer(CMD_HELP_MESSAGE)

@router.message(Command('dice'))
async def cmd_dice(message: Message) -> None:
    await message.answer_dice()

@router.message(Command('location'))
async def cmd_eiffel_detailed(message: Message) -> None:
    await message.answer_venue(
        latitude=48.8584,
        longitude=2.2945,
        title="Эйфелева башня (Eiffel Tower)",
        address="Avenue Anatole France, 75007 Paris, Франция",
    )

@router.message(Command('contact'))
async def cmd_contact(message: Message) -> None:
    await message.answer_contact('+7 991 520 59 26','Cahek')

@router.message(Command('animation'))
async def cmd_animation(message: Message) -> None:
    await message.answer_animation('https://media.tenor.com/lhBpQxxP9dAAAAAM/yuh-huh-cat.gif')

@router.message(Command('photo'))
async def cmd_photo(message: Message) -> None:
    await message.answer_photo('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQipbeVbeKv3X2t4hT8F87awvCC45UsZ8rQrA&s')
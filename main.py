import asyncio
from aiohttp import web

from aiogram import Bot,Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from aiogram.fsm.storage.memory import MemoryStorage

from core.config import config
from bot.handlers.routers import routers

async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(
        url=config.WEBHOOK_URL,
        drop_pending_updates=True,
    )

async def on_shutdown(bot: Bot) -> None:
    await bot.delete_webhook()
    await bot.session.close()


async def main():
    try:
        bot = Bot(config.BOT_TOKEN)
        storage = MemoryStorage()
        dp = Dispatcher(storage=storage)

        dp.include_routers(*routers)

        app = web.Application()
        webhook = SimpleRequestHandler(
            dispatcher=dp,
            bot=bot
        )

        webhook.register(app, path='/webhook')
        
        async def health(request):
            return web.Response(text='OK')
        app.router.add_get('/health', health)

        app.on_startup.append(lambda _: on_startup(bot))
        app.on_shutdown.append(lambda _: on_shutdown(bot))

        return app
    except Exception as e:
        print(e)
        return web.Application()

if __name__ == '__main__':
    try:
        app = asyncio.run(main())
        web.run_app(app=app, host=config.WEBAPP_HOST, port=config.WEBAPP_PORT)
    except Exception as e:
        print(e)


import asyncio
import random

import playwright.async_api
from playwright.async_api import async_playwright, expect, BrowserContext, Geolocation

from bot.utils import (Geo,
                       ProfileDatabase, logger)
from bot.config import settings, browserSpoofingScript, texts



async def start(profile: tuple[str, ...], db: ProfileDatabase,semaphore: asyncio.Semaphore) -> None:
    async with semaphore:
        name, path, proxy, user_agent, wallet_address, wallet_private_key, password, status = profile

        geo = Geo(proxy) if proxy else Geo()
        lat, lan, locale, timezone = await geo.get_info_from_proxy()
        await geo.close_connection()

        optional_params = {}
        if proxy:
            url = proxy.split('://')[0] + "://" + proxy.split('@')[1]
            proxy_user = proxy.split('@')[0].split('://')[1].split(':')[0]
            proxy_password = proxy.split('@')[0].split('://')[1].split(':')[1]


            optional_params['proxy'] = {
                'server': url,
                'username': proxy_user,
                'password': proxy_password
            }

        if settings.HEADLESS:
            optional_params['headless'] = True
            optional_params['channel'] = "chromium"

        else:
            optional_params['headless'] = False

        async with async_playwright() as p:
            try:
                logger.info(f"{name} | {proxy if proxy else '...'} | Profile started")
                context = await p.chromium.launch_persistent_context(
                    rf'{path}',
                    args= [
                        '--disable-blink-features=AutomationControlled'
                    ],
                    user_agent=user_agent,
                    permissions=['notifications'],
                    is_mobile=False,
                    geolocation= Geolocation(latitude=lat, longitude=lan),
                    locale=locale,
                    timezone_id=timezone,
                    bypass_csp=True,
                    **optional_params
                )


                await context.add_init_script(browserSpoofingScript)


                discord_page = await context.new_page()
                await discord_page.goto('https://discord.com/channels/@me', timeout=60000)
                await discord_page.wait_for_load_state('networkidle')


                login_button = discord_page.locator('label').get_by_text('Email or Phone Number')
                if await login_button.is_visible():
                    logger.warning(f"{name} | Need authorization, disable headless mod")
                    logger.warning(f"{name} | After logging into the account, type something into the console")
                    await async_input()

                logger.info(f"{name} | Started the Discord")
                penguins_button = discord_page.locator('div[data-dnd-name="Pixel Pengus 🐧✳"]')
                await expect(penguins_button).to_be_visible()
                await asyncio.sleep(random.uniform(1, 3))
                await penguins_button.hover()
                await penguins_button.click()

                await asyncio.sleep(random.uniform(1, 3))

                penguins_chat = discord_page.locator('a[data-list-item-id="channels___996797485961973870"]')
                await expect(penguins_chat).to_be_visible()
                await asyncio.sleep(random.uniform(2, 4))
                await penguins_chat.hover()
                await penguins_chat.click()

                try:
                    text_box = discord_page.locator('div[role="textbox"]')
                    await discord_page.wait_for_selector('div[role="textbox"]', state='visible', timeout=5000)
                    await asyncio.sleep(random.uniform(1, 3))

                    logger.info(f"{name} | Started sending messages")
                    for i in range(99999):
                            await text_box.fill(random.choice(texts))
                            await discord_page.keyboard.down('Enter')
                            await asyncio.sleep(7.3)

                except playwright.async_api.TimeoutError:
                    time = await discord_page.locator('//html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/div[2]/div/div[2]/div/span').inner_text()
                    # hours = discord_page.locator().inner_text()
                    # minutes = discord_page.locator().inner_text()
                    # seconds = discord_page.locator().inner_text()
                    logger.warning(f"You have received a ban for sending messages, it expires: {time}")
                    await context.close()

                await context.close()
                # await uniswap(context, name, password)

            except Exception as e:
                logger.error(f"{name} | {e}")
                await context.close()


async def async_input(prompt: str = "") -> str:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, input, prompt)






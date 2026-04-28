import asyncio
from playwright.async_api import async_playwright
import os

async def test_with_screenshots():
    # DISPLAY уже установлен в контейнере
    print(f"Display: {os.environ.get('DISPLAY')}")
    
    async with async_playwright() as p:
        browser = await p.webkit.launch(headless=False)
        page = await browser.new_page()
        
        print("🌐 Загружаю сайт...")
        await page.goto('https://www.wikipedia.org')
        
        print("📸 Делаю скриншот...")
        await page.screenshot(path='screenshots/wiki_xvfb.png')
        
        print("✅ Скриншот сохранён: screenshots/wiki_xvfb.png")
        
        await browser.close()

if __name__ == '__main__':
    asyncio.run(test_with_screenshots())
import asyncio
from playwright.async_api import async_playwright
import time

async def test_visit_website():
    """Открыть сайт в Safari и посмотреть через VNC"""
    
    async with async_playwright() as p:
        print("\n" + "="*60)
        print("🌐 ОТКРЫВАЮ САЙТ В SAFARI")
        print("="*60)
        
        # Запустите браузер ВИДИМЫМ
        browser = await p.webkit.launch(headless=False)
        page = await browser.new_page()
        
        # ПЕРЕЙДИТЕ НА САЙТ
        print("\n📍 Переходу на: https://www.google.com")
        await page.goto('https://www.google.com')
        
        # Получите заголовок
        title = await page.title()
        print(f"✅ Заголовок страницы: {title}")
        
        # Окно остаётся открытым 30 секунд
        print("\n🎯 Окно Safari открыто в VNC!")
        print("⏳ Оно закроется через 30 секунд...")
        print("💡 Подключитесь через VNC (localhost:5901) чтобы видеть браузер")
        
        time.sleep(30)
        
        # Скриншот
        await page.screenshot(path='screenshots/google.png')
        print("\n📸 Скриншот сохранён: screenshots/google.png")
        
        await browser.close()
        print("✅ Браузер закрыт")
        print("="*60 + "\n")

if __name__ == '__main__':
    asyncio.run(test_visit_website())
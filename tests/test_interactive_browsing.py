import asyncio
from playwright.async_api import async_playwright
import time

async def test_interactive():
    """Интерактивный режим - вы можете взаимодействовать с браузером"""
    
    async with async_playwright() as p:
        print("\n" + "="*70)
        print("🎮 ИНТЕРАКТИВНЫЙ РЕЖИМ SAFARI")
        print("="*70)
        
        browser = await p.webkit.launch(headless=False)
        page = await browser.new_page()
        
        # Откройте начальную страницу
        print("\n🚀 Запускаю Safari...")
        await page.goto('https://www.example.com')
        print("✅ Safari запущен и видимый в VNC!")
        
        print("\n" + "="*70)
        print("ДОСТУПНЫЕ КОМАНДЫ:")
        print("="*70)
        print("1. Клики на элементы")
        print("2. Заполнение форм")
        print("3. Вводы в текстовые поля")
        print("4. Скриншоты")
        print("5. Все это можно делать автоматически через Python!")
        print("="*70)
        
        # Примеры действий
        print("\n📍 Примеры действий, которые браузер выполняет:")
        
        print("\n1️⃣ Загружаю Google...")
        await page.goto('https://www.google.com')
        await page.fill('input[name="q"]', 'Python Playwright')
        print("   ✅ Ввёл текст в поиск")
        time.sleep(2)
        
        print("\n2️⃣ Нажимаю Enter...")
        await page.press('input[name="q"]', 'Enter')
        await page.wait_for_load_state('networkidle')
        print("   ✅ Результаты загружены")
        time.sleep(3)
        
        print("\n3️⃣ Делаю скриншот...")
        await page.screenshot(path='screenshots/interactive_demo.png')
        print("   ✅ Скриншот: screenshots/interactive_demo.png")
        
        print("\n🎯 Браузер остаётся открытым 30 секунд")
        print("💡 Смотрите все это в VNC окне (localhost:5901)")
        time.sleep(30)
        
        await browser.close()
        print("\n✅ Браузер закрыт")
        print("="*70 + "\n")

if __name__ == '__main__':
    asyncio.run(test_interactive())
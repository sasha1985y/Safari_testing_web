import asyncio
from playwright.async_api import async_playwright

async def interactive_safari():
    async with async_playwright() as p:
        # headless=False - браузер будет видимым
        browser = await p.webkit.launch(headless=False)
        
        page = await browser.new_page()
        await page.goto('https://sasha1985y.github.io/Resume_Kuyantsev_Alexander_Dev/')
        
        # Браузер останется открыт, пока вы не закроете его
        # Вы можете взаимодействовать с ним вручную
        print("🌐 Safari открыт. Вы можете взаимодействовать с ним.")
        print("Нажмите Enter в терминале, чтобы продолжить...")
        input()
        
        # Сделайте скриншот
        await page.screenshot(path='screenshots/safari_interactive.png')
        
        await browser.close()

if __name__ == '__main__':
    asyncio.run(interactive_safari())
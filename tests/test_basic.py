import asyncio
from playwright.async_api import async_playwright

async def test_basic():
    async with async_playwright() as p:
        browser = await p.webkit.launch(headless=True)
        page = await browser.new_page()
        
        await page.goto('https://sasha1985y.github.io/Resume_Kuyantsev_Alexander_Dev/')
        title = await page.title()
        print(f"✅ Заголовок: {title}")
        
        await page.screenshot(path='screenshots/example.png')
        await browser.close()

if __name__ == '__main__':
    asyncio.run(test_basic())
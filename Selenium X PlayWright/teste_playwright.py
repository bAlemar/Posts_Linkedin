from playwright.async_api import async_playwright
import asyncio
import time
import psutil

async def playwright_scraping(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        page = await browser.new_page()

        await page.goto(url)
     



async def main(urls):
    start_time = time.time()  # Registra o tempo de início
    
    for i in range(0, len(urls), 2):   
        
        # Primeiro lot de urls a ser rodado
        slot_urls = urls[i:i+2]

        #Armazenando as tasks a serem rodadas
        tasks = []
        for j in range(len(slot_urls)):
            # Executar a extração para a URL atual
            task = asyncio.create_task(playwright_scraping(slot_urls[j]))
            tasks.append(task)
        await asyncio.gather(*tasks)
    
    # Calculo tempo
    end_time = time.time()  
    duration = end_time - start_time
    print("Tempo de execução (Playwright): {:.2f} segundos".format(duration))
    
    # Monitoramento de hardware
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    print("Uso de CPU: {:.2f}%".format(cpu_percent))
    print("Uso de Memória: {:.2f}%".format(memory_percent))

    return


if __name__ == '__main__':
    urls = [
            'https://kabum.com.br/','https://www.google.com',
            'https://www.amazon.com.br/','https://www.mercadolivre.com.br/' 
                ]
    asyncio.run(main(urls))
from selenium import webdriver
import threading
import time
import psutil



def scraping_selenium(url):
    driver = webdriver.Chrome()


    
    driver.get(url)

    driver.quit()
    return

 

def main(urls):
    start_time = time.time()  # Registra o tempo de início
    
    # Percorrer 2 em 2
    for i in range(0, len(urls), 2):
        
        # Primeiro lot de urls a ser rodado
        slot_urls = urls[i:i+2]
        
        #Iniciando as threads
        threads = []
        for url in slot_urls:
            thread = threading.Thread(target=scraping_selenium, args=(url,))
            thread.start()
            threads.append(thread)
        
        # finalizando as threads
        for thread in threads:
            thread.join()

    # Calculo tempo
    end_time = time.time()  
    duration = end_time - start_time
    print("Tempo de execução (Selenium): {:.2f} segundos".format(duration))
    
    # Monitoramento de hardware
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    print("Uso de CPU: {:.2f}%".format(cpu_percent))
    print("Uso de Memória: {:.2f}%".format(memory_percent))



if __name__ == '__main__':
    urls = [
            'https://kabum.com.br/','https://www.google.com',
            'https://www.amazon.com.br/','https://www.mercadolivre.com.br/' 
            ]
    main(urls)


import requests
import lxml.html as html
import os # Crear carpeta 
import datetime 

home_url = "https://www.larepublica.co/"
xpath_links        = "//text-fill/a/@href" #Por alguna razon toma h2 como textfill
xpath_titulo       = "//text-fill[not(@class)]/span/text()"
xpath_description  = '//div[@class = "lead"]/p/text()'
xpath_body         = '//div[@class = "html-content"]/p/text()'

def parse_notice(link, folder):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice  = response.content.decode("utf-8")
            parsed  = html.fromstring(notice)

            try:
                title = parsed.xpath(xpath_titulo)[0]
                title = title.replace('\"', " ")
                description = parsed.xpath(xpath_description)[0]
                body  = parsed.xpath(xpath_body)

                with open(f"{folder}/{title}.txt", "w", encoding = "utf-8" ) as f:
                    f.write(title)
                    f.write("\n\n")
                    f.write(description)
                    f.write("\n\n")
                    for p in body:
                        f.write(p)
                        f.write("\n")
                    f.close()


            except IndexError:
                return 
                
        else: 
            raise ValueError(f"Error = {response.status_code    }")


    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        response = requests.get(home_url)
        if response.status_code == 200:
            home = response.content.decode('utf-8') # Decode cambia los valores como ñ en letras que python entienda
            parse = html.fromstring(home)  # Usando lxml me transforma el codigo html de requests a codigo xpath
            links_xpath_content = parse.xpath(xpath_links) # Busca la expresión xpath en el html xpath
            #print(links_xpath)

            today = datetime.date.today().strftime("%d-%m-%Y") # Parsear la fecha en forma de str y con dia mes y año
            if not os.path.isdir(today):
                os.mkdir(today)
            
            for link in links_xpath_content:
                parse_notice(link, today)    
        else:
            raise ValueError(f"Error {response.status_code}")
    
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__ == "__main__":
    run()
import sys
import os
import os.path

try:
    if len(sys.argv) != 2:
        print("Usagem: gerar_html.py [diretório]")
    if not os.path.exists(sys.argv[1]):
        raise FileNotFoundError

    with open("pagina.html", "w", encoding="utf-8") as pagina:
        pagina.write("""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
    <meta charset="utf-8">
    <title>Título da Página</title>
    </head>
    <body>""")
        inicial = os.getcwd()
        img_count = 0
        if os.getcwd() != sys.argv[1]:
            os.chdir(sys.argv[1])
        for arquivo in os.listdir(sys.argv[1]):
            if os.path.isfile(arquivo):
                if arquivo[-4:] == ".jpg" or arquivo[-4:] == ".png":
                    img_count += 1
                    pagina.write(f"<h1><a href={sys.argv[1]}/{arquivo}>Imagem {img_count}</a></h1>")
        pagina.write("</body></html>")

except FileNotFoundError:
    print("Erro: arquivo ou diretório inexistente.")

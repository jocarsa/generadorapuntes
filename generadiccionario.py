import os
import html
import json
import tkinter as tk
from tkinter import ttk



def get_folder_list(path):
    folder_list = []
    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            folder_list.append(os.path.join(root, dir_name))
    return folder_list

def get_files_and_folders(directory, depth=0):
    items = []
    for item in os.listdir(directory):
        if item[0] != ".":
            path = os.path.join(directory, item)
            if os.path.isfile(path):
                items.append((path, depth))
                
            else:
                items.append((path, depth))
                items.extend(get_files_and_folders(path, depth + 1))
    return items

def get_selected_value():
    selected_value = folder_combobox.get()
    print("Selected Value:", selected_value)
    limpio = selected_value.replace("../","")
    apuntes(limpio)

def apuntes(carpeta):

    excepciones = ['registros.sqlite','registros.csv','datos.json','README.md','jquery-3.7.0.js','jquery-3.7.0.min.js','jquery-3.6.0.min.js','jquery-3.7.0.slim.js','jquery-3.7.0.slim.min.js','jquery-ui.min.css','jquery-ui.min.js','jquery-ui.structure.min.css','jquery-ui.theme.min.css','jquery.js']
    abreviaturas = ['traductor.csv']
    archivos = {}
    # Usage example
    directory_path = "..\\"+carpeta
    subecarpeta = "GitHub2/"
    titulo = "Titulo 11"
    subtitulo = "Subtitulo"
    autor = "Jose Vicente Carratala"
    cabecera = "Esta es la cabecera"
    piedepagina = "Este es el pie de pagina"
    try:
        f = open(directory_path+'\\datos.json', encoding='utf-8')
        data = json.load(f)
        print(data)
        titulo = data['titulo']
        subtitulo = data['subtitulo']
        autor = data['autor']
        cabecera = data['cabecera']
        piedepagina = data['piedepagina']
    except:
        pass


    file_list = get_files_and_folders(directory_path)
    try:
        os.remove(directory_path+"-doc.html")
        os.remove(directory_path+"-pres.html")
    except:
        pass
    f = open(directory_path+"-doc.html", "a", encoding='utf-8-sig')
    fpower = open(directory_path+"-pres.html", "a", encoding='utf-8-sig')
    f.write('''
        <!doctype html>
        <html>
            <head>
                <link rel="Stylesheet" href="generadorapuntes/estilo.css">
                
            </head>
            <body>
            <header>'''+cabecera+'''</header>
            <main>
            <div id="pageFooter">Page </div>
            <div id="primerapagina">'''+titulo+'''</div>
            <div id="titulo">'''+titulo+'''</div>
            <div id="subtitulo">'''+subtitulo+'''</div>
            <div id="autor">'''+autor+'''</div>
            <div class="ruptura"></div>
            <div id="table-of-contents"></div>
            <div id="tabladecontenido">Tabla de contenido</div>
            <script src="generadorapuntes/jquery-3.7.0.min.js"></script>
            <table>
            
    ''')
    fpower.write(
'''
        <!doctype html>
        <html>
            <head>
                <link rel="Stylesheet" href="generadorapuntes/estilo.css">
                
            </head>
            <body id="diapositivas">
           
            </div>
            <div id="primeradiapositiva" class="diapositiva">
            <div id="titulo">'''+titulo+'''</div>
            </div>
            </div>
            <div id="segundadiapositiva" class="diapositiva">
            <div id="titulo">'''+titulo+'''</div>
            <div id="subtitulo">'''+subtitulo+'''</div>
            <div id="autor">'''+autor+'''</div>
            </div>
            </div>
            <script src="generadorapuntes/jquery-3.7.0.min.js"></script>
            
            
    '''
        )
    ###################################INDICE

    nivel1 = 0
    nivel2 = 0
    nivel3 = 0
    nivel4 = 0
    nivel5 = 0
    nivel6 = 0

    # Print the list of files and folders
    for item,depth in file_list:
        directorio = os.path.dirname(item)
        archivo = os.path.basename(item)
        explotado = os.path.splitext(archivo)
        nombrearchivo = explotado[0]
        extensionarchivo = explotado[1]
        nombrenuevoarchivo = nombrearchivo+".acomment"+extensionarchivo
        nombrenuevoarchivoconsola = nombrearchivo+".zconsole"+extensionarchivo
        nombrenuevoarchivoactividad = nombrearchivo+".zzactividad"+extensionarchivo
        if not "zconsole" in item and not "acomment" in item  and not "zzactividad" in item and os.path.isfile(item) and not os.path.exists(directorio+"//"+nombrenuevoarchivo) and not "png" in item and not "jpg" in item:     
            f2 = open(directorio+"//"+nombrenuevoarchivo, 'w+')
        if not "zconsole" in item and not "acomment" in item  and not "zzactividad" in item and os.path.isfile(item) and not os.path.exists(directorio+"//"+nombrenuevoarchivoconsola) and not "png" in item and not "jpg" in item:     
            f2 = open(directorio+"//"+nombrenuevoarchivoconsola, 'w+')
        if not "zconsole" in item and not "acomment" in item  and not "zzactividad" in item and os.path.isfile(item) and not os.path.exists(directorio+"//"+nombrenuevoarchivoactividad) and not "png" in item and not "jpg" in item:     
            f2 = open(directorio+"//"+nombrenuevoarchivoactividad, 'w+')
        #print(item)
        if not(os.path.isfile(item)):
            f.write("</pre>")
            if depth  == 0:
                nivel1+=1
                f.write("<tr><td><a href='#"+item+"'><p class='indice"+str(depth+1)+"'> "+str(nivel1)+"."+"-"+item.split('\\')[-1].split('-')[-1]+"</p></a></td><td class='numpagina'></td></tr>")
                fpower.write("</div><div class='diapositiva invertida'><h1>"+item.split('\\')[-1].split('-')[-1]+"</h1>")
                nivel2 = 1
                nivel3 = 1
                nivel4 = 1
                nivel5 = 1
                nivel6 = 1
            elif depth  == 1:
                nivel2+=1
                f.write("<tr><td><a href='#"+item+"'><p class='indice"+str(depth+1)+"'> "+str(nivel1)+"."+str(nivel2-1)+"."+"-"+item.split('\\')[-1].split('-')[-1]+"</p></a></td><td class='numpagina'></td></tr>")
                fpower.write("</div><div class='diapositiva'><h2>"+item.split('\\')[-1].split('-')[-1]+"</h2>")

                nivel3 = 1
                nivel4 = 1
                nivel5 = 1
                nivel6 = 1
            elif depth  == 2 and not("royecto" in item):
                nivel3+=1
                f.write("<tr><td><a href='#"+item+"'><p class='indice"+str(depth+1)+"'> "+str(nivel1)+"."+str(nivel2-1)+"."+str(nivel3-1)+"."+"-"+item.split('\\')[-1].split('-')[-1]+"</p></a></td><td class='numpagina'></td></tr>")
                fpower.write("<h3>"+item.split('\\')[-1].split('-')[-1]+"</h3>")
                
                nivel4 = 1
                nivel5 = 1
                nivel6 = 1
            elif depth  == 3 and not("royecto" in item):
                nivel4+=1
                f.write("<tr><td><a href='#"+item+"'><p class='indice"+str(depth+1)+"'> "+str(nivel1)+"."+str(nivel2-1)+"."+str(nivel3-1)+"."+str(nivel4-1)+"."+"-"+item.split('\\')[-1].split('-')[-1]+"</p></a></td><td class='numpagina'></td></tr>")
                
                nivel5 = 1
                nivel6 = 1
            elif depth  == 4 and not("royecto" in item):
                nivel5+=1
                f.write("<tr><td><a href='#"+item+"'><p class='indice"+str(depth+1)+"'> "+str(nivel1)+"."+str(nivel2-1)+"."+str(nivel3-1)+"."+str(nivel4-1)+"."+str(nivel5-1)+"."+"-"+item.split('\\')[-1].split('-')[-1]+"</p></a></td><td class='numpagina'></td></tr>")
                

                nivel6 = 1
            elif depth  == 5 and not("royecto" in item):
                f.write("<tr><td><p class='indice"+str(depth+1)+"'> "+str(nivel1)+"."+str(nivel2-1)+"."+str(nivel3-1)+"."+str(nivel4-1)+"."+str(nivel5-1)+"."+str(nivel6-1)+"."+"-"+item.split('\\')[-1].split('-')[-1]+"</p></a></td><td class='numpagina'></td></tr>")
                nivel6+=1                   
                
    f.write("</table><div id='content'>")
        
    ###################################CONTENIDO
    archivos = {}
    nivel1 = 0
    nivel2 = 0
    nivel3 = 0
    nivel4 = 0
    nivel5 = 0
    nivel6 = 0

    # Print the list of files and folders
    for item,depth in file_list:
        #print(item)
        if not(os.path.isfile(item)):
            f.write("</pre>")
            if depth  == 0:
                archivos = {}
                nivel1+=1
                f.write("<h"+str(depth+1)+" id='"+item+"'> "+str(nivel1)+"."+"-"+item.split('\\')[-1].split('-')[-1]+"</h"+str(depth+1)+">")
                
                nivel2 = 1
                nivel3 = 1
                nivel4 = 1
                nivel5 = 1
                nivel6 = 1
            elif depth  == 1:
                nivel2+=1
                f.write("<h"+str(depth+1)+" id='"+item+"'> "+str(nivel1)+"."+str(nivel2-1)+"."+"-"+item.split('\\')[-1].split('-')[-1]+"</h"+str(depth+1)+">")
                

                nivel3 = 1
                nivel4 = 1
                nivel5 = 1
                nivel6 = 1
            elif depth  == 2:
                nivel3+=1
                f.write("<h"+str(depth+1)+" id='"+item+"'> "+str(nivel1)+"."+str(nivel2-1)+"."+str(nivel3-1)+"."+"-"+item.split('\\')[-1].split('-')[-1]+"</h"+str(depth+1)+">")
                
                
                nivel4 = 1
                nivel5 = 1
                nivel6 = 1
            elif depth  == 3:
                nivel4+=1
                f.write("<h"+str(depth+1)+" id='"+item+"'> "+str(nivel1)+"."+str(nivel2-1)+"."+str(nivel3-1)+"."+str(nivel4-1)+"."+"-"+item.split('\\')[-1].split('-')[-1]+"</h"+str(depth+1)+">")
                
                nivel5 = 1
                nivel6 = 1
            elif depth  == 4:
                nivel5+=1
                f.write("<h"+str(depth+1)+" id='"+item+"'> "+str(nivel1)+"."+str(nivel2-1)+"."+str(nivel3-1)+"."+str(nivel4-1)+"."+str(nivel5-1)+"."+"-"+item.split('\\')[-1].split('-')[-1]+"</h"+str(depth+1)+">")
                

                nivel6 = 1
            elif depth  == 5:
                f.write("<h"+str(depth+1)+" id='"+item+"'> "+str(nivel1)+"."+str(nivel2-1)+"."+str(nivel3-1)+"."+str(nivel4-1)+"."+str(nivel5-1)+"."+str(nivel6-1)+"."+"-"+item.split('\\')[-1].split('-')[-1]+"</h"+str(depth+1)+">")
                nivel6+=1                   
                
            if  "royecto" in os.path.basename(item):
                #nivel2+=1
                #f.write("<h2> </h2>")
                f.write("<b>Estructura del directorio</b><br>")
                nivel3 = 1
                nivel4 = 1
                nivel5 = 1
                nivel6 = 1
                file_list2 = get_files_and_folders(item)
                estructura = ""
                for item2,depth2 in file_list2:
                    if not "acomment" in item2:
                        sub = False
                        for i in range(0,depth2):
                            sub = True
                            estructura += "<img src='vacio.svg' class='carpeta' style='margin-left:5px;'>"
                        if sub == True:
                            estructura += "<img src='nodocarpeta.svg' class='carpeta' style='margin-left:5px;'>"
                        if os.path.isfile(item2) and not "acomment" in item:
                           estructura += "<img src='archivo.svg' class='carpeta'>"
                        else:
                            estructura += "<img src='carpeta.svg' class='carpeta'>"
                        if not "acomment" in item:
                            estructura += item2.split('\\')[-1].split('-')[-1]+"<br>"
                f.write(estructura)
                #f.write("<h2> Contenido:</h2>")
                #f.write("<h3>Directorio raíz:</h3>")
        else:

            if "comment" in item:
                #f.write("<p class='negrita'>"+item.split('\\')[-1].split('-')[-1].split('.')[0]+"</p>")
                pass
                
            else:
                
                #f.write("<div class='nombrearchivo'>"+os.path.basename(item).split('\\')[-1]+"</div>")
                partido = item.split('\\')
                micadena = ""
                if not "acomment" in item:
                    for i in range(2,len(partido)):
                        micadena += "/"
                        if i == len(partido)-1:
                            micadena += "<img src='archivo.svg' class='carpeta'>"
                        else:
                            micadena += "<img src='carpeta.svg' class='carpeta'>"
                        
                        micadena += partido[i].split('-')[-1]
                    if "captura" in item:
                        f.write("<p class='negrita'>Resultado:</p>")
                        f.write("<div class='nombrearchivo'><div class='boton rojo'></div><div class='boton amarillo'></div><div class='boton verde'></div><div class='url'></div></div>")
                    elif "console" in item:
                        if os.stat(item).st_size != 0:
                            f.write("<div class='nombrearchivo console'><div class='boton rojo'></div><div class='boton amarillo'></div><div class='boton verde'></div>"+micadena+"</div>")
                    elif "zzactividad" in item:
                        if os.stat(item).st_size != 0:
                            f.write("<div class='cabeceraactividad'>Actividad</div>")
                    else:
                        f.write("<div class='nombrearchivo'><div class='boton rojo'></div><div class='boton amarillo'></div><div class='boton verde'></div>"+micadena+"</div>")
            
               
        if "png" in item or "jpg" in item:
            archivos[os.path.basename(item)] = os.path.getsize(item)
            print("imagen: "+item+" - "+str(os.path.getsize(item)))            
        try:
            if "acomment" in item:
                f.write("</pre><pre class='nocode'>")
                f.write("<p><b>"+os.path.basename(item).split("-")[1].split(".")[0]+"</b></p>")
                f.write("<p>")
                file_path = item
                with open(file_path, 'r', encoding='utf-8-sig') as file:
                    content = file.read()
                    #f.write(content)
                    lines = content.splitlines()
                    
                    for i in range(0,len(lines)):
                        if "--" in lines[i]:
                            f.write("<pre class='code code2'>"+(lines[i].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("--",""))+"</pre>")
                            
                        else:
                            f.write(lines[i].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")+"<br>")
                f.write("</p>")
                f.write("</pre>")
                pass
            elif "captura" in item:
                f.write("</pre><pre class='captura'><img src='"+subecarpeta+item+"'></pre>")
            elif "png" in item or "jpg" in item:
                f.write("</pre><pre class='nocode'><img src='"+subecarpeta+item+"'></pre>")
            else:
                file_path = item
                with open(file_path, 'r', encoding='utf-8-sig') as file:
                    content = file.read()
                    if os.path.basename(item) in excepciones:
                        f.write("</pre><pre class='code'>(omitido)</pre<br>")
                    elif os.path.basename(item) in abreviaturas:
                        f.write("</pre><pre class='code'>(abreviado)</pre<br>")
                    elif str(os.path.basename(item)) in archivos.keys():
                        
                        if archivos[os.path.basename(item)] == content or archivos[os.path.basename(item)] == os.path.getsize(item):
                            f.write("</pre><pre class='code'>(sin cambios)</pre<br>")
                        else:
                            f.write("</pre>")
                            numerodelinea = 1
                            f.write("<pre class='code'>")
                            lines = content.splitlines()
                            lines2 = archivos[os.path.basename(item)].splitlines()
                            count = 0
                            # Strips the newline character
                            #f.write("long:"+str(len(lines))+"\n")
                            #f.write("long:"+str(len(lines2))+"\n")
                            f.write("<br>")

                            if len(lines) > len(lines2):
                                for i in range(0,len(lines)):
                                    try:
                                        if lines[i] == lines2[i]:
                                            f.write("<span class='numerodelinea'>"+str(numerodelinea)+"</span> "+"  "+lines[i].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")+"<br>")
                                        else:
                                            f.write("<span class='numerodelinea'>"+str(numerodelinea)+"</span> "+"<span class='plus'>+</span> "+lines[i].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")+"<br>")
                                    except:
                                        f.write("<span class='numerodelinea'>"+str(numerodelinea)+"</span> "+" "+lines[i].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")+"<br>")
                                        pass
                                    numerodelinea += 1
                            else:
                                for i in range(0,len(lines2)):
                                    try:
                                        if lines[i] == lines2[i]:
                                            f.write("<span class='numerodelinea'>"+str(numerodelinea)+"</span> "+"  "+lines[i].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")+"<br>")
                                        else:
                                            f.write("<span class='numerodelinea'>"+str(numerodelinea)+"</span> "+"<span class='plus'>+</span> "+lines[i].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")+"<br>")
                                    except:
                                        f.write("<span class='numerodelinea'>"+str(numerodelinea)+"</span> "+" "+lines[i].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")+"<br>")
                                        pass
                                    numerodelinea += 1
                            f.write("<br>")
                            #f.write(str(count)+"\n\r\n\r")
                            if "acomment" in item:
                                pass
                           
                            else:
                            
                                archivos[os.path.basename(item)] = content
                            f.write("</pre>")
                            if not os.path.exists(item):
                                print("escribo")
                                #f2 = open("C:\\prueba\\prueba.txt", 'w+')
                                #f2.write("a")
                                #f2.close()
                    else:
                            numerodelinea = 1
                            if "console" in item:
                                if os.stat(item).st_size != 0:
                                    f.write("</pre><pre class='code console'>")
                            elif "zzactividad" in item:
                                if os.stat(item).st_size != 0:
                                    f.write("</pre><pre class='code actividad'>")
                            else:
                                f.write("</pre><pre class='code'>")
                            #print("nuevo")
                            
                            f.write("<br>")
                            lines = content.splitlines()
                            for i in range(0,len(lines)):
                                f.write("<span class='numerodelinea'>"+str(numerodelinea)+"</span> "+lines[i].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")+"<br>")
                                numerodelinea += 1
                            f.write("<br>")
                            f.write("</pre>")
                            archivos[os.path.basename(item)] = content
                            
                                
                    f.write("</pre>")
            
        except Exception as e:
            #print(item)
            print(e)
            #print("------------------------")
            print("error")
            pass
    
                
    f.write('''
</div>
    <div id="pageFooter">Page </div>
    <div id="prueba"></div>
        </main>
        
        <footer>[pagina]</footer>
        </body>
        
        
        </html>
    ''')
    fpower.write('''
</div>
    <div id="pageFooter">Page </div>
    <div id="prueba"></div>
        </main>
        
        <footer>[pagina]</footer>
        </body>
        
        <script src="generadorapuntes/diapositivas.js"></script>
        </html>
    ''')
    f.close()
    fpower.close()
    print("ok hecho")



root = tk.Tk()
root.title("Hola chicos")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)


# Create the ComboBox
folder_combobox = ttk.Combobox(frame)

# Set the width of the ComboBox
folder_combobox.config(width=50)

# Get the list of folders
folder_list = get_folder_list('../')

# Set the values of the ComboBox
folder_combobox['values'] = folder_list

# Place the ComboBox on the window
folder_combobox.pack()



button = tk.Button(frame, text="Vamos alla", command=get_selected_value)
button.pack()

root.mainloop()

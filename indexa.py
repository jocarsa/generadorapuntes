import os
import html
import json
import tkinter as tk






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

def apuntes(carpeta):

    excepciones = ['jquery-3.7.0.js','jquery-3.7.0.min.js','jquery-3.6.0.min.js']
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
    except:
        pass


    file_list = get_files_and_folders(directory_path)
    try:
        os.remove(directory_path+".html")
    except:
        pass
    f = open(directory_path+".html", "a", encoding='utf-8-sig')

    f.write('''
        <!doctype html>
        <html>
            <head>
                <style>
                    @import url('https://fonts.googleapis.com/css2?family=Ubuntu&display=swap');
                    body{
                        font-family:Ubuntu;
                    }
                    main{
                        font-family:Ubuntu;
                        
                        background:white;
                        display: table;
                    }
                    @media only screen {
                    html{
                        background:grey;
                    }
                        main{
                        font-family:Ubuntu;
                        max-width:800px;
                        margin:auto;
                        
                        background:white;
                        padding:50px;
                        }
                    }
                    pre{
                        padding:14px;
                        background:rgb(240,240,240);
                        border-radius:0px 0px 10px 10px;
                        margin-top:0px;
                        white-space: pre-wrap;
                        font-size:11px;
                        
                    }
                    .code,.captura{
                    }
                    .nombrearchivo{
                        background:rgb(230,230,230);
                        border-radius:5px 5px 0px 0px;
                        font-size:14px;
                        padding:5px;
                        text-align:center;
                        clear:both;
                        margin-top:10px;
                        border-bottom:1px solid rgb(220,220,220);
                    }
                    .plus{
                        width:10px;
                        height:10px;
                        border-radius:10px;
                        font-size:10px;
                        font-weight:bold;
                        background:rgb(220,220,220);
                        color:black;
                        display:inline-block;
                        line-height:10px;
                        text-align:center;
                    }
                    .carpeta{
                    width:20px;
                    }
                    .negrita{
                        font-weight:bold;
                    }
                    a{color:inherit;text-decoration:none;}
                    .indice1{padding:0px;margin:0px;padding-left:20px;}
                    .indice2{padding:0px;margin:0px;padding-left:40px;}
                    .indice3{padding:0px;margin:0px;padding-left:60px;}
                    .indice4{padding:0px;margin:0px;padding-left:80px;}
                    .indice5{padding:0px;margin:0px;padding-left:100px;}
                    .indice6{padding:0px;margin:0px;padding-left:120px;}
                    #titulo{font-weight:bold;font-size:60px;text-align:center;}
                    #subtitulo{font-weight:bold;font-size:40px;text-align:center;}
                    #autor{font-weight:bold;font-size:30px;text-align:center;}
                   p{text-align:justify;font-size:14px;}
                     @media only print {
                     h1{
                     padding-top:200px;
                        page-break-after  :always;
                        page-break-before :always;
                        text-align:center;
                        font-size:60px;
                    }
                     }
                     @media print {
                      div.divFooter {
                        position: fixed;
                        bottom: 0;
                      }
                    }
                    header{position:fixed;top:0px;border-bottom:1px solid grey;width:100%;text-align:center;}
                    footer{position:fixed;bottom:0px;border-top:1px solid grey;width:100%;text-align:center;}
                    .nocode{background:white;font-family:Ubuntu;}
                     
                        
                        .ruptura{
                            page-break-after  :always;
                        page-break-before :always;
                        }
                        #titulo{
                        padding-top:100px;}
                        .boton{float:left;margin:4px;width:15px;height:15px;border-radius:20px;}
                        .rojo{background:#ff5f57;}
                        .amarillo{background:#ffbd2d;}
                        .verde{background:#29ca41;}
                        .captura{text-align:center;background:white;border:1px solid rgb(220,220,220);border-top:none;}
                        .captura img{width:100%;}
                        .url{width:50%;height:20px;border-radius:5px;background:white;margin:auto;}
                        .numerodelinea{color:grey;width:20px;text-align:right;display:inline-block;}
                        .nocode img{
                        max-width:100%;text-align:center;margin:auto;}
                        @page  
                        { 
                            size: auto;   /* auto is the initial value */ 

                            /* this affects the margin in the printer settings */ 
                            margin: 15mm 15mm 15mm 15mm; 
                        #pageFooter {
                            display: table-footer-group;
                        }

                        #pageFooter:after {
                            counter-increment: page;
                            content: counter(page);
                        }
                        }
                        @page:first
                        { 
                            size: auto;   /* auto is the initial value */ 

                            /* this affects the margin in the printer settings */ 
                            margin: 15mm 15mm 15mm 15mm; 
                        #pageFooter {
                            display: none;
                        }

                        #pageFooter:after {
                            counter-increment: page;
                            content: counter(page);
                        }
                        }
                </style>
                
            </head>
            <body>
            <header>Cabecera de página</header>
            <main>
            <div id="pageFooter">Page </div>
            <div id="titulo">'''+titulo+'''</div>
            <div id="subtitulo">'''+subtitulo+'''</div>
            <div id="autor">'''+autor+'''</div>
            <div class="ruptura"></div>
            <div id="tabladecontenido">Tabla de contenido</div>
    ''')
    ###################################INDICE

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
                nivel1+=1
                f.write("<a href='#"+item+"'><p class='indice"+str(depth+1)+"'> "+str(nivel1)+"."+"-"+item.split('\\')[-1].split('-')[-1]+"</p></a>")
                
                nivel2 = 1
                nivel3 = 1
                nivel4 = 1
                nivel5 = 1
                nivel6 = 1
            elif depth  == 1 and not("royecto" in item):
                nivel2+=1
                f.write("<a href='#"+item+"'><p class='indice"+str(depth+1)+"'> "+str(nivel1)+"."+str(nivel2-1)+"."+"-"+item.split('\\')[-1].split('-')[-1]+"</p></a>")
                

                nivel3 = 1
                nivel4 = 1
                nivel5 = 1
                nivel6 = 1
            elif depth  == 2 and not("royecto" in item):
                nivel3+=1
                f.write("<a href='#"+item+"'><p class='indice"+str(depth+1)+"'> "+str(nivel1)+"."+str(nivel2-1)+"."+str(nivel3-1)+"."+"-"+item.split('\\')[-1].split('-')[-1]+"</p></a>")
                
                
                nivel4 = 1
                nivel5 = 1
                nivel6 = 1
            elif depth  == 3 and not("royecto" in item):
                nivel4+=1
                f.write("<a href='#"+item+"'><p class='indice"+str(depth+1)+"'> "+str(nivel1)+"."+str(nivel2-1)+"."+str(nivel3-1)+"."+str(nivel4-1)+"."+"-"+item.split('\\')[-1].split('-')[-1]+"</p></a>")
                
                nivel5 = 1
                nivel6 = 1
            elif depth  == 4 and not("royecto" in item):
                nivel5+=1
                f.write("<a href='#"+item+"'><p class='indice"+str(depth+1)+"'> "+str(nivel1)+"."+str(nivel2-1)+"."+str(nivel3-1)+"."+str(nivel4-1)+"."+str(nivel5-1)+"."+"-"+item.split('\\')[-1].split('-')[-1]+"</p></a>")
                

                nivel6 = 1
            elif depth  == 5 and not("royecto" in item):
                f.write("<p class='indice"+str(depth+1)+"'> "+str(nivel1)+"."+str(nivel2-1)+"."+str(nivel3-1)+"."+str(nivel4-1)+"."+str(nivel5-1)+"."+str(nivel6-1)+"."+"-"+item.split('\\')[-1].split('-')[-1]+"</p></a>")
                nivel6+=1                   
                
           
        
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
                nivel2+=1
                #f.write("<h2> </h2>")
                f.write("<h2> "+str(nivel1)+"."+str(nivel2-1)+"."+"-"+"Estructura del directorio</h2>")
                nivel3 = 1
                nivel4 = 1
                nivel5 = 1
                nivel6 = 1
                file_list2 = get_files_and_folders(item)
                estructura = ""
                for item2,depth2 in file_list2:
                    sub = False
                    for i in range(0,depth2):
                        sub = True
                        estructura += "<img src='vacio.svg' class='carpeta' style='margin-left:5px;'>"
                    if sub == True:
                        estructura += "<img src='nodocarpeta.svg' class='carpeta' style='margin-left:5px;'>"
                    if os.path.isfile(item2):
                       estructura += "<img src='archivo.svg' class='carpeta'>"
                    else:
                        estructura += "<img src='carpeta.svg' class='carpeta'>"
                    estructura += item2.split('\\')[-1].split('-')[-1]+"<br>"
                f.write(estructura)
                #f.write("<h2> Contenido:</h2>")
                #f.write("<h3>Directorio raíz:</h3>")
        else:

            if "comentario" in item:
                f.write("<p class='negrita'>"+item.split('\\')[-1].split('-')[-1].split('.')[0]+"</p>")
                
            else:
                
                #f.write("<div class='nombrearchivo'>"+os.path.basename(item).split('\\')[-1]+"</div>")
                partido = item.split('\\')
                micadena = ""
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
                else:
                    f.write("<div class='nombrearchivo'><div class='boton rojo'></div><div class='boton amarillo'></div><div class='boton verde'></div>"+micadena+"</div>")
        
               
                    
        try:
            if "comentario" in item:
                f.write("</pre><pre class='nocode'>")
                f.write("<p>")
                file_path = item
                with open(file_path, 'r', encoding='utf-8-sig') as file:
                    content = file.read()
                    #f.write(content)
                    lines = content.splitlines()
                    
                    for i in range(0,len(lines)):
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
                                        f.write("<span class='numerodelinea'>"+str(numerodelinea)+"</span> "+"<span class='plus'>+</span>"+lines[i].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")+"<br>")
                                    numerodelinea += 1
                            else:
                                for i in range(0,len(lines2)):
                                    try:
                                        if lines[i] == lines2[i]:
                                            f.write("<span class='numerodelinea'>"+str(numerodelinea)+"</span> "+"  "+lines[i].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")+"<br>")
                                        else:
                                            f.write("<span class='numerodelinea'>"+str(numerodelinea)+"</span> "+"<span class='plus'>+</span> "+lines[i].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")+"<br>")
                                    except:
                                        f.write("<span class='numerodelinea'>"+str(numerodelinea)+"</span> "+"<span class='plus'>+</span> "+lines[i].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")+"<br>")
                                    numerodelinea += 1
                            f.write("<br>")
                            #f.write(str(count)+"\n\r\n\r")
                            if "png" in item or "jpg" in item:
                                archivos[os.path.basename(item)] = os.path.getsize(item)
                            else:    
                                archivos[os.path.basename(item)] = content
                            f.write("</pre>")
                            if not os.path.exists(item):
                                f2 = open(item+".acomment", 'w+')
                                f2.write("a")
                                f2.close()
                    else:
                            numerodelinea = 1
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
                            if not os.path.exists(item):
                                f2 = open(item+".acomment", 'w+')
                                f2.write("a")
                                f2.close()
                                
                    f.write("</pre>")
                
        except Exception as e:
            #print(item)
            #print(e)
            #print("------------------------")
            print("error")
            pass

    f.write('''
    <div id="pageFooter">Page </div>
        </main>
        <footer>Pie de pagina</footer>
        </body>
        </html>
    ''')
        
    f.close()
    print("ok hecho")

def button_click():
    value = entry.get()
    print("Button clicked with value:", value)
    apuntes(value)

root = tk.Tk()
root.title("Frame with Entry and Button")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

entry = tk.Entry(frame, width=30)
entry.pack(pady=10)

button = tk.Button(frame, text="Click Me", command=button_click)
button.pack()

root.mainloop()

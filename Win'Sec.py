import ctypes
import pyttsx3
import tkinter as tk
import os
import subprocess
import requests
import shutil
import wget
import zipfile
from tkinter import messagebox, Menu
from PIL import Image, ImageTk

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def tts(message):

    engine.say(message)
    engine.runAndWait()

def clean():

    os.system("cls")


def pause():

    os.system("pause > nul")

def path():

    return os.path.dirname(os.path.abspath(__file__))

def report(content, filename):

    report_path = os.path.join(path(), filename)

    if os.path.exists(report_path):

        report_exist = f"Le compte-rendu {filename} existe déjà !"
        
        tts(report_exist)
        messagebox.showwarning(title="Win'Sec :", message=report_exist)
    
    else:

        with open(report_path, "w") as file:
            
            file.write(content)
       
        report_create = f"Le compte-rendu {filename} vient d'être créé !"
        
        tts(report_create)
        messagebox.showinfo(title="Win'Sec :", message=report_create)

def winpmem():
    
    winpmem_path = os.path.join(path(), "winpmem.exe")

    if not os.path.exists(winpmem_path):
        
        wget.download("https://github.com/Velocidex/WinPmem/releases/download/v4.0.rc1/winpmem_mini_x64_rc2.exe", out=winpmem_path)
        clean()

        if os.path.exists(winpmem_path):
            
            winpmem_success = "WinPmem vient d'être téléchargé !"
            
            tts(winpmem_success)
            messagebox.showinfo(title="Win'Sec :", message=winpmem_success)
        
        else:
          
            winpmem_failed = "WinPmem n'a pas pu être téléchargé !"
           
            tts(winpmem_failed)
            messagebox.showwarning(title="Win'Sec :", message=winpmem_failed)
    else:
       
        winpmem_exist = "Vous avez déjà téléchargé WinPmem !"

        tts(winpmem_exist)
        messagebox.showwarning(title="Win'Sec :", message=winpmem_exist)

def volatility():
   
    volatility_zip = os.path.join(path(), "volatility.zip")
    volatility_path = os.path.join(path(), "vol.py")

    if os.path.exists(volatility_path):

        volatility_exist = "Vous avez déjà téléchargé Volatility !"

        tts(volatility_exist)
        messagebox.showwarning(title="Win'Sec :", message=volatility_exist)

    else:
        
        wget.download("https://github.com/volatilityfoundation/volatility3/archive/refs/heads/develop.zip", out=volatility_zip)

        if os.path.exists(volatility_zip):
          
            volatility_directory = os.path.join(path(), "volatility")

            with zipfile.ZipFile(volatility_zip, "r") as unzip:
                
                unzip.extractall(volatility_directory)

            volatility_folder = os.path.join(volatility_directory, "volatility3-develop")
            volatility_py = os.path.join(volatility_folder, "vol.py")

            if os.path.exists(volatility_py):
               
                shutil.copy(volatility_py, volatility_path)
                shutil.rmtree(volatility_directory)
               
                os.remove(volatility_zip)

                if os.path.exists(volatility_path):
                    
                    volatility_success = "Volatility vient d'être téléchargé !"
                    
                    tts(volatility_success)
                    messagebox.showinfo(title="Win'Sec :", message=volatility_success)
                
                else:
                   
                    volatility_failed = "Volatility n'a pas pu être téléchargé !"
                    
                    tts(volatility_failed)
                    messagebox.showwarning(title="Win'Sec :", message=volatility_failed)

def download():
    
    try:
        
        request = requests.get("https://www.google.com", timeout=5)
        statut = request.status_code

        if statut == 200:
            
            winpmem()
            volatility()

    except requests.ConnectionError:
        
        no_connection = "Vous ne pouvez pas télécharger les logiciels, veuillez vérifier votre connexion à Internet via votre réseau Wi-Fi !"
        
        tts(no_connection)
        messagebox.showwarning(title="Win'Sec :", message=no_connection)

def delete():
    
    winpmem_path = os.path.join(path(), "winpmem.exe")
    volatility_path = os.path.join(path(), "vol.py")
    
    if os.path.exists(winpmem_path):
        
        try:
            
            os.remove(winpmem_path)
            winpmem_success = "WinPmem vient d'être supprimé !"
            
            tts(winpmem_success)
            messagebox.showinfo(title="Win'Sec :", message=winpmem_success)
        
        except Exception:
            
            winpmem_failed = "WinPmem n'a pas pu être supprimé !"
            
            tts(winpmem_failed)
            messagebox.showerror(title="Win'Sec :", message=winpmem_failed)

    if os.path.exists(volatility_path):
        
        try:
            
            os.remove(volatility_path)
            volatility_success = "Volatility vient d'être supprimé !"
            
            tts(volatility_success)
            messagebox.showinfo(title="Win'Sec :", message=volatility_success)
        
        except Exception:
            
            volatility_failed = "Volatility n'a pas pu être supprimé !"
            
            tts(volatility_failed)
            messagebox.showerror(title="Win'Sec :", message=volatility_failed)
            
def memory():

    winpmem_path = os.path.join(path(), "winpmem.exe")

    if os.path.exists(winpmem_path):
      
        memory_path = os.path.join(path(), "memory.mem")

        if os.path.exists(memory_path):
           
            memory_exist = "Une image mémoire a déjà été créée !"
           
            tts(memory_exist)
            messagebox.showinfo(title="Win'Sec :", message=memory_exist)
       
        else:
            
            subprocess.run([winpmem_path, memory_path])
            
            memory_copy = "L'image mémoire vient d'être créée !"
            
            tts(memory_copy)
            messagebox.showinfo(title="Win'Sec :", message=memory_copy)
   
    else:

        warning_1 = "Vous ne disposez pas du logiciel permettant de créer l'image mémoire !"
        warning_2 = "Veuillez installer l'ensemble des logiciels !"

        tts(warning_1 + warning_2)

        messagebox.showwarning(title="Win'Sec :", message=warning_1)
        messagebox.showwarning(title="Win'Sec :", message=warning_2)

def config():
   
    volatility_path = os.path.join(path(), "vol.py")
    memory_path = os.path.join(path(), "memory.mem")

    paths = [volatility_path, memory_path]

    if all(os.path.exists(p) for p in paths):
            
            config_command = subprocess.Popen(["python.exe", volatility_path, "--save-config", "config.json", "-f", memory_path, "windows.info"], stdout=subprocess.PIPE)
            config_command.communicate()

            config_json = os.path.join(path(), "config.json")

            if os.path.exists(config_json):
               
                json_success = "Le fichier de configuration JSON vient d'être créé !"
                
                tts(json_success)
                messagebox.showinfo(title="Win'Sec :", message=json_success)
           
            else:
                
                json_failed = "Le fichier de configuration JSON n'a pas pu être créé !"
                
                tts(json_failed)
                messagebox.showwarning(title="Win'Sec :", message=json_failed)

    else:

       warning = "Veuillez télécharger l'ensemble des logiciels et créer une image mémoire !"

       tts(warning)
       messagebox.showwarning(title="Win'Sec :", message=warning)

def warning():

    softwares_warning = "Veuillez télécharger l'ensemble des logiciels, créer un fichier de configuration et une image mémoire !"

    tts(softwares_warning)
    messagebox.showwarning(title="Win'Sec :", message=softwares_warning)

def pslist():

    volatility_path = os.path.join(path(), "vol.py")
    config_json = os.path.join(path(), "config.json")
    memory_path = os.path.join(path(), "memory.mem")

    paths = [volatility_path, config_json, memory_path]

    if all(os.path.exists(p) for p in paths):
        
        pslist_process = subprocess.Popen(["python.exe", volatility_path, "-c", config_json, "-f", memory_path, "windows.pslist.PsList"], stdout=subprocess.PIPE)
        output, _ = pslist_process.communicate()
        output = output.decode("utf-8")

        print(output)
        
        pause()
        clean()

        pslist_file = "Souhaitez-vous enregistrer le résultat de l'analyse des processus exécutés ?"
        tts(pslist_file)

        pslit_window = tk.Tk()
        pslit_window.title("Enregistrer le résultat de l'analyse des processus exécutés :")
        pslit_window.iconbitmap(os.path.join(path(), "icon.ico"))
        pslit_window.geometry("600x120")
        pslit_window.resizable(False, False)

        label = tk.Label(pslit_window, text=pslist_file, padx=10, pady=10)
        label.pack()

        frame = tk.Frame(pslit_window)
        frame.pack(pady=10)

        yes_button = tk.Button(frame, text="Oui !", command=lambda: [report(output, "pslist.txt"), pslit_window.destroy()])
        yes_button.pack(side="left", padx=20)

        no_button = tk.Button(frame, text="Non !", command=pslit_window.destroy)
        no_button.pack(side="left", padx=20)

        pslit_window.mainloop()
    
    else:
       
        warning()


def pstree():
    
    volatility_path = os.path.join(path(), "vol.py")
    config_json = os.path.join(path(), "config.json")
    memory_path = os.path.join(path(), "memory.mem")

    paths = [volatility_path, memory_path]

    if all(os.path.exists(p) for p in paths):
        
        pstree = subprocess.Popen(["python.exe", volatility_path, "-c", config_json, "-f", memory_path, "windows.pstree.PsTree"], stdout=subprocess.PIPE)
        output, _ = pstree.communicate()
        output = output.decode("utf-8")

        print(output)
        
        pause()
        clean()

        pstree_file = "Souhaitez-vous enregistrer le résultat de l'analyse de l'arborescence des processus ?"
        tts(pstree_file)

        pstree_window = tk.Tk()
        pstree_window.title("Enregistrer le résultat de l'analyse de l'arborescence des processus :")
        pstree_window.iconbitmap(os.path.join(path(), "icon.ico"))
        pstree_window.geometry("600x120")
        pstree_window.resizable(False, False)

        label = tk.Label(pstree_window, text=pstree_file, padx=10, pady=10)
        label.pack()

        frame = tk.Frame(pstree_window)
        frame.pack(pady=10)

       
        yes_button = tk.Button(frame, text="Oui !", command=lambda: [report(output, "pstree.txt"), pstree_window.destroy()])
        yes_button.pack(side="left", padx=20)

        no_button = tk.Button(frame, text="Non !", command=pstree_window.destroy)
        no_button.pack(side="left", padx=20)

        pstree_window.mainloop()
    
    else:
        
        warning()

def dlllist():
    
    volatility_path = os.path.join(path(), "vol.py")
    config_json = os.path.join(path(), "config.json")
    memory_path = os.path.join(path(), "memory.mem")

    paths = [volatility_path, memory_path]

    if all(os.path.exists(p) for p in paths):
        
        dlllist = subprocess.Popen(["python.exe", volatility_path, "-c", config_json, "-f", memory_path, "dllist"], stdout=subprocess.PIPE)
        output, _ = dlllist.communicate()
        output = output.decode("utf-8")

        print(output)
        
        pause()
        clean()

        dlllist_file = "Souhaitez-vous enregistrer le résultat de l'ensemble des DLL qui ont été exécutées ?"
        tts(dlllist_file)

        dlllist_window = tk.Tk()
        dlllist_window.title("Enregistrer le résultat de l'ensemble des DLL exécutées :")
        dlllist_window.iconbitmap(os.path.join(path(), "icon.ico"))
        dlllist_window.geometry("600x120")
        dlllist_window.resizable(False, False)

        label = tk.Label(dlllist_window, text=dlllist_file, padx=10, pady=10)
        label.pack()

       
        frame = tk.Frame(dlllist_window)
        frame.pack(pady=10)

        yes_button = tk.Button(frame, text="Oui !", command=lambda: [report(output, "dlllist.txt"), dlllist_window.destroy()])
        yes_button.pack(side="left", padx=20)

        no_button = tk.Button(frame, text="Non !", command=dlllist_window.destroy)
        no_button.pack(side="left", padx=20)

        dlllist_window.mainloop()
  
    else:
        
        warning()

def netscan():
    
    volatility_path = os.path.join(path(), "vol.py")
    config_json = os.path.join(path(), "config.json")
    memory_path = os.path.join(path(), "memory.mem")

    paths = [volatility_path, memory_path]

    if all(os.path.exists(p) for p in paths):
        
        netscan = subprocess.Popen(["python.exe", volatility_path, "-c", config_json, "-f", memory_path, "netscan"], stdout=subprocess.PIPE)
        output, _ = netscan.communicate()
        output = output.decode("utf-8")

        print(output)
        
        pause()
        clean()

        netscan_file = "Souhaitez-vous enregistrer le résultat de l'analyse des connexions entrantes et sortantes ?"
        tts(netscan_file)

        netscan_window = tk.Tk()
        netscan_window.title("Enregistrer le résultat de l'analyse des connexions entrantes et sortantes :")
        netscan_window.iconbitmap(os.path.join(path(), "icon.ico"))
        netscan_window.geometry("600x120")
        netscan_window.resizable(False, False)

        label = tk.Label(netscan_window, text=netscan_file, padx=10, pady=10)
        label.pack()

        frame = tk.Frame(netscan_window)
        frame.pack(pady=10)

        yes_button = tk.Button(frame, text="Oui !", command=lambda: [report(output, "netscan.txt"), netscan_window.destroy()])
        yes_button.pack(side="left", padx=20)

        no_button = tk.Button(frame, text="Non !", command=netscan_window.destroy)
        no_button.pack(side="left", padx=20)

        netscan_window.mainloop()
    
   
    else:
        
        warning()

def cmdline():
    
    volatility_path = os.path.join(path(), "vol.py")
    config_json = os.path.join(path(), "config.json")
    memory_path = os.path.join(path(), "memory.mem")

    paths = [volatility_path, memory_path]

    if all(os.path.exists(p) for p in paths):
        
        cmdline = subprocess.Popen(["python.exe", volatility_path, "-c", config_json, "-f", memory_path, "windows.cmdline.CmdLine"], stdout=subprocess.PIPE)
        output, _ = cmdline.communicate()
        output = output.decode("utf-8")

        print(output)
        
        pause()
        clean()

        cmdline_file = "Souhaitez-vous enregistrer le résultat de l'analyse des processus ayant fait usage de commandes ?"
        tts(cmdline_file)

        cmdline_window = tk.Tk()
        cmdline_window.title("Enregistrer le résultat de l'analyse des processus ayant fait usage de commandes.")
        cmdline_window.iconbitmap(os.path.join(path(), "icon.ico"))
        cmdline_window.geometry("600x120")
        cmdline_window.resizable(False, False)

        label = tk.Label(cmdline_window, text=cmdline_file, padx=10, pady=10)
        label.pack()

        frame = tk.Frame(cmdline_window)
        frame.pack(pady=10)

        yes_button = tk.Button(frame, text="Oui !", command=lambda: [report(output, "cmdline.txt"), cmdline_window.destroy()])
        yes_button.pack(side="left", padx=20)

        no_button = tk.Button(frame, text="Non !", command=cmdline_window.destroy)
        no_button.pack(side="left", padx=20)

        cmdline_window.mainloop()
    
    else:
        
        warning()

def key():
   
    volatility_path = os.path.join(path(), "vol.py")
    config_json = os.path.join(path(), "config.json")
    memory_path = os.path.join(path(), "memory.mem")

    paths = [volatility_path, memory_path]

    if all(os.path.exists(p) for p in paths):
        
        key = subprocess.Popen(["python.exe", volatility_path, "-c", config_json, "-f", memory_path, "windows.registry.printkey.PrintKey"], stdout=subprocess.PIPE)
        output, _ = key.communicate()
        output = output.decode("utf-8")

        print(output)
        
        pause()
        clean()

        key_file = "Souhaitez-vous enregistrer le résultat des clés de registre sous une ruche ou une valeur de clé spécifique ?"
        tts(key_file)

        key_window = tk.Tk()
        key_window.title("Enregistrer le résultat des clés de registre sous une ruche ou une valeur de clé spécifique.")
        key_window.iconbitmap(os.path.join(path(), "icon.ico"))
        key_window.geometry("600x120")
        key_window.resizable(False, False)

        label = tk.Label(key_window, text=key_file, padx=10, pady=10)
        label.pack()

        frame = tk.Frame(key_window)
        frame.pack(pady=10)

        yes_button = tk.Button(frame, text="Oui !", command=lambda: [report(output, "key.txt"), key_window.destroy()])
        yes_button.pack(side="left", padx=20)

        no_button = tk.Button(frame, text="Non !", command=key_window.destroy)
        no_button.pack(side="left", padx=20)

        key_window.mainloop()
    
    else:
        
        warning()

def winsec():
    
    window = tk.Tk()
    window.title("Win'Sec :")
    window.iconbitmap(os.path.join(path(), "icon.ico"))
    window.geometry("1250x800")
    window.resizable(False, False)

    menu = Menu(window)
    window.config(menu=menu)

    menu.add_cascade(label="Télécharger l'ensemble des logiciels.", command=download)
    menu.add_cascade(label="Supprimer l'ensemble des logiciels.", command=delete)
    menu.add_cascade(label="Créer une image mémoire.", command=memory)
    menu.add_cascade(label="Créer un fichier de configuration.", command=config)

    analyze = Menu(menu, tearoff=0)
    menu.add_cascade(label="Analyser l'image mémoire.", menu=analyze)

    analyze.add_command(label="Afficher l'ensemble des processus en cours d'exécution.", command=pslist)
    analyze.add_command(label="Afficher l'arborescence des processus exécutés.", command=pstree)
    analyze.add_command(label="Afficher l'ensemble des DLL qui ont été exécutées.", command=dlllist)
    analyze.add_command(label="Afficher l'ensemble des connexions entrantes et sortantes.", command=netscan)
    analyze.add_command(label="Afficher l'ensemble des processus ayant fait usage de l'invite de commande.", command=cmdline)
    analyze.add_command(label="Afficher les clés de registre sous une ruche ou une valeur de clé spécifique.", command=key)

    icon_path = os.path.join(path(), "icon.ico")
    icon_image = Image.open(icon_path)
    icon_photo = ImageTk.PhotoImage(icon_image)

    background_label = tk.Label(window, image=icon_photo)
    background_label.image = icon_photo
    background_label.place(relx=0.5, rely=0.5, anchor="center")

    window.mainloop()

if __name__ == "__main__":
    
    ctypes.windll.kernel32.SetConsoleTitleW("Win'Sec :")

    if ctypes.windll.shell32.IsUserAnAdmin():
        
        clean()
        winsec()

    elif not ctypes.windll.shell32.IsUserAnAdmin():

        admin = "Veuillez exécuter ce logiciel dans l'invite de commande en mode administrateur afin de l'utiliser de manière optimale !"

        tts(admin)
        messagebox.showwarning(title="Win'Sec :", message=admin)

        quit()

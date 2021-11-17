import pyautogui
import time
import sys

def get_position() :
    pos = pyautogui.position()
    return pos[0], pos[1]

print("Bienvenue aux rickrollers")
time.sleep(1)

print("""Rendez vous sur la page d'édition du drapeau puis reclickez sur ce programme et appuyez sur ENTRER""")
input()
time.sleep(1)

print("Calibration")
time.sleep(1)

print("Mettez votre curseur (sans cliquer) au dessus d'un endroit sans interaction (bord gauche recommandé) du site et appuyez sur ENTRER")
input()
neutral_coord = get_position()
print(neutral_coord)
pyautogui.moveTo(neutral_coord)
pyautogui.click()
pyautogui.press('f5')
print("rafraichissement en cours et recliquez sur ce programme")
time.sleep(10)
print('appuyez sur ENTRER')
input()


print("Mettez votre curseur (sans cliquer) au dessus du bouton 'Editer le drapeau' et appuyez sur ENTRER")
input()
edit_coord = get_position()
print(edit_coord)
time.sleep(1)

print("Attention, phase de calibration en cours, veuillez ne toucher à rien pendant 20 secondes")
def setup() :
    global neutral_coord
    global edit_coord

    pyautogui.moveTo(neutral_coord)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('f5')
    time.sleep(10)
    pyautogui.moveTo(edit_coord)
    pyautogui.click()
    time.sleep(10)
    pyautogui.moveTo(neutral_coord)
    time.sleep(1)
    pyautogui.scroll(-1)
    time.sleep(1)
    pyautogui.scroll(-1)
    time.sleep(2)
        
setup()
print("Calibration 1/2 terminée")
time.sleep(1)
print("reclickez sur le programme et appuyez sur ENTRER")
input()

print("Mettez votre curseur (sans cliquer) au dessus de la boite de dialogue pour le X du pixel et appuyez sur ENTRER")
input()
x_coord = get_position()
print(x_coord)
time.sleep(1)

print("Mettez votre curseur (sans cliquer) au dessus de la boite de dialogue pour le Y du pixel et appuyez sur ENTRER")
input()
y_coord = get_position()
print(y_coord)
time.sleep(1)

print("Mettez votre curseur (sans cliquer) au dessus de la boite de dialogue pour la couleur du pixel et appuyez sur ENTRER")
input()
color_coord = get_position()
print(color_coord)
time.sleep(1)

print("Mettez votre curseur (sans cliquer) au dessus du bouton 'modifier la couleur' et appuyez sur ENTRER")
input()
submit_coord = get_position()
print(submit_coord)
time.sleep(1)

print("Maintenant, pour calibrer le bouton ok de la boite de dialogue, veuillez changer la couleur d'un pixel en cliquant sur le bouton 'modifier' sans cliquer sur la boite de dialogue après, puis recliquer sur ce programme. Mettez votre souris sur le bouton 'ok' (sans cliquer) puis appuyez sur ENTRER")
input()
ok_coord = get_position()
print(ok_coord)
time.sleep(1)
pyautogui.moveTo(ok_coord)
pyautogui.click()

with open("ma_calibration.py", 'w') as f :
    f.writelines(f"neutral_coord = {neutral_coord}\n")
    f.writelines(f"edit_coord = {edit_coord}\n")
    f.writelines(f"x_coord = {x_coord}\n")
    f.writelines(f"y_coord = {y_coord}\n")
    f.writelines(f"color_coord = {color_coord}\n")
    f.writelines(f"submit_coord = {submit_coord}\n")
    f.writelines(f"ok_coord = {ok_coord}\n")

    

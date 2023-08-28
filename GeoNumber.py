
import phonenumbers
from phonenumbers import geocoder
import os
from time import sleep
from colorama import init, Fore, Style, Back
init()



os.system("pip install phonenumbers")
os.system("clear")

print(Fore.GREEN+Style.BRIGHT+"""

:'######:::'########::'#######::                                
'##... ##:: ##.......::'##.... ##:                                
 ##:::..::: ##:::::::: ##:::: ##:                                
 ##::'####: ######::: ##:::: ##:                                
 ##::: ##:: ##...:::: ##:::: ##:                                
 ##::: ##:: ##::::::: ##:::: ##:                                
. ######::: ########:. #######::                                
:......::::.......:::.......:::                                
'##::: ##:'##::::'##:'##::::'##:'########::'####### #:'########::
 ###:: ##: ##:::: ##: ###::'###: ##.... ##: ##.......:: ##... .##:
 ####: ##: ##:::: ##: ####'####: ##:::: ##: ##::::::: ##::: :##:
 ## ## ##: ##:::: ##: ## ### ##: ########:: ######::: ####### #::
 ##. ####: ##:::: ##: ##. #: ##: ##.... ##: ##...:::: ##.. ##:::
 ##:. ###: ##:::: ##: ##:.:: ##: ##:::: ##: ##::::::: ##::. ##::
 ##::. ##:. #######:: ##:::: ##: ########:: ########: ##:::. ##:
..::::..:::.......:::..:::::..::.......:::.... .::..::::::..::



""")

titulo = """ 
         Created by: 1LUgarParaProgramar
         
         Author :  Hans saldias
         
         Script : GeoLocalizar numero telefonico
         
         """
         
for i in titulo:
         print(i, end="", flush=True)        
         sleep(0.1) 
         


def obtener_informacion_telefono(numero):
    try:
        numero_parsed = phonenumbers.parse(numero)
        codigo_pais = phonenumbers.region_code_for_number(numero_parsed)
        ubicacion = geocoder.description_for_number(numero_parsed, "es")
        
        print(Fore.YELLOW+Style.BRIGHT+"[ # ] Número de teléfono:", numero)
        print("\n[ ! ] Código de país:", codigo_pais)
        print("\n[ > ] Ubicación:", ubicacion)
        print("\n\nCreated by : H.saldias")
    except phonenumbers.phonenumberutil.NumberParseException:
        print("Número de teléfono no válido.")


numero_telefono = input("Ingrese el numero:  ")
obtener_informacion_telefono(numero_telefono)
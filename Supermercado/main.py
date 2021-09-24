#######################################
#            SUPERMERCADO             #
#     @author - Carranza Maxi         #
#             25/7/2021               #
#             version: 1              #
#######################################

import os
from paquete import db
import xlrd


productos = [['Precio','Nombre','Categoria']]


def main():
    while True:
        menu = """
        \t\t1 - Ingresar producto
        \t\t2 - Consultar producto
        \t\t3 - Categorias
        \t\t4 - Salir
        \t\tIngrese una Opcion: """

        opcion = input(menu)
        
        if opcion == '1':
            while True:
                productos2 = [] 
                precio = float(input('\t\t\tIngrese Precio del Producto: '))
                nombre = input('\t\t\tIngrese Nombre del Producto: ')
                categoria = input('\t\t\tIngrese Catagoria del Producto: ')
                productos2.append(precio)
                productos2.append(nombre)
                productos2.append(categoria)
                productos.append(productos2)
                print(productos)
                db.carga_db(productos)
                conti = input("\t\t\tDesea continuar cargando productos? S/N: ")
                if conti.upper() == 'S':
                    continue
                else:
                    break
        elif opcion == '2':
            #db.muestra_db()
            #for i in range(hoja.nrows):
                
                #print(hoja.cell_values(i,0),"           ",hoja.cell_value(i,1),"           ",hoja.cell_value(i,2))
            conti = input("\t\t\tDesea continuar? S/N: ")
            if conti.upper() == 'S':
                continue
            else:
                break
        elif opcion == '3':
            pass #Mostrar Categorias de los productos (ej: Bebidas, lacteos, carne, galletitas)
            conti = input("\t\t\tDesea continuar? S/N: ")
            if conti.upper() == 'S':
                continue
            else:
                break
        elif opcion == '4':
            print("\t\t\tCerrando Supermercado")
            break
        else:
            print("\t\t\tOpción incorrecta !!!")
            print("\t\t\tVuelva a ingresar la opción correcta")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if __name__ == '__main__':
    os.system("clear")

    print(bcolors.HEADER + '\t\t\t+#################################+')
    print(bcolors.HEADER + '\t\t\t#         "Supermercado"          #')
    print(bcolors.HEADER +  '\t\t\t#                                 #')
    print(bcolors.HEADER +  '\t\t\t#     %s -------------------%s        #' %(bcolors.FAIL,bcolors.HEADER))
    print(bcolors.HEADER +  '\t\t\t#     %s|    Bienvenido      |%s      #' %(bcolors.FAIL,bcolors.HEADER))
    print(bcolors.HEADER +  '\t\t\t#     %s -------------------%s        #' %(bcolors.FAIL,bcolors.HEADER))
    print(bcolors.WARNING +  '\t\t\t#                                 #')
    print(bcolors.WARNING +  '\t\t\t#-------------------------------  #')
    print(bcolors.WARNING +  '\t\t\t#                                 #')  
    print(bcolors.WARNING + '\t\t\t#   Solicitudes de productos      #')
    print(bcolors.WARNING + '\t\t\t#   Almacenamiento de informacion #')
    print(bcolors.WARNING + '\t\t\t#   Inventario del proveedor      #')
    print(bcolors.WARNING +  '\t\t\t#                                 #')
    print(bcolors.WARNING +  '\t\t\t#------------------------------   #')
    print(bcolors.WARNING +  '\t\t\t#                                 #')
    print(bcolors.WARNING +  '\t\t\t#    %s"Bienvenido al Super"%s        #'  %(bcolors.BOLD,bcolors.ENDC+bcolors.WARNING))
    print(bcolors.WARNING +  '\t\t\t#            :)                   #')
    print(bcolors.WARNING +  '\t\t\t#                                 #')
    print(bcolors.WARNING + '\t\t\t+#################################+')
    print(bcolors.ENDC)

    main()


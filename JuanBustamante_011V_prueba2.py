import os
clear = 'cls'
os.system(clear)

camiones=1
carga_camion=int(450)
kilo_gas_adicional=int(1700)
valor_transporte_uso_camion=int(100000)
cilindro_5kilos=0
cilindro_15kilos=0
cilindro_45kilos=0
pedido=0

while pedido!=1:
    menu=True
    try:
        nombre_Cliente = input('Ingresa tu nombre: ')
        if len(nombre_Cliente)>=3:
            print(f'tu nombre es: {nombre_Cliente}')
        else:
            print('nombre debe poseer al menos 3 letras')
    except ValueError:
        print('nombre debe poseer al menos 3 letras')
    try:
        telefono = input('Ingresa un numero de telefono: ')
        if len(telefono)>= 8:
            print(f'tu numero es: {telefono}')
            break
        else:
            print('telefono debe poseer entre 8 y 9 digitos')
    except ValueError:
        print('telefono debe poseer entre 8 y 9 digitos')
    pedido==1

while menu==True:
    try:
        cantidad_kilos=int(input('Ingrese cantidad de kilos: '))
        if cantidad_kilos>=0:
            cilindro_5kilos=int(input('Ingresa cantidad de cilindros de 5 kilos: '))
            cilindro_15kilos=int(input('Ingresa cantidad de cilindros de 15 kilos: '))
            cilindro_45kilos=int(input('Ingresa cantidad de cilindros de 45 kilos: '))
            break 
        else:
            print('Ingresa un valor mayor o igual a 0')
            menu==False 
    except ValueError:
        print('Ingresa un valor mayor o igual a 0')
        menu==False  
    
carga_actual=cilindro_5kilos*5+ cilindro_15kilos*15+cilindro_45kilos*45
print(f'Llevas la cantidad de {carga_actual}'' kilos')

if carga_actual>carga_camion:
    print('Necesitarás un nuevo camion')
    camiones+=1
    carga_sobrante=(cantidad_kilos-carga_camion)
    print('Te sobran: ',carga_sobrante , ' Kilos')

    valor_pedido= camiones*765000+carga_sobrante*kilo_gas_adicional+valor_transporte_uso_camion

    print(f'El precio del pedido es de: ${valor_pedido}')
else:
    print('Como no completaste el camion, deberás pagar 1.700 por kilo de gas, más $100.000 por transporte')
    valor_pedido=kilo_gas_adicional*carga_actual+valor_transporte_uso_camion
    print(f'Valor de pedido: ${valor_pedido}')

print('\nImpresion de boleta')
print(f'Cliente: {nombre_Cliente}')
print(f'Telefono: {telefono}')
print(f'Cantidad kilos: {cantidad_kilos}')
print(f'Camiones: {camiones}')
print(f'Total: {valor_pedido}')

nuevo_pedido=int(input('\n¿Desea hacer otro pedido?: 1 (si)/2 (no)'))

while nuevo_pedido==1:
    while menu==True:
        try:
            cantidad_kilos=int(input('Ingrese cantidad de kilos: '))
            if cantidad_kilos>=0:
                cilindro_5kilos=int(input('Ingresa cantidad de cilindros de 5 kilos: '))
                cilindro_15kilos=int(input('Ingresa cantidad de cilindros de 15 kilos: '))
                cilindro_45kilos=int(input('Ingresa cantidad de cilindros de 45 kilos: '))
                break 
            else:
                print('Ingresa un valor mayor o igual a 0')
                menu==False 
        except ValueError:
            print('Ingresa un valor mayor o igual a 0')
        menu==False  
    
    carga_actual=cilindro_5kilos*5+ cilindro_15kilos*15+cilindro_45kilos*45
    print(f'Llevas la cantidad de {carga_actual}'' kilos')

    if carga_actual>carga_camion:
        print('Necesitarás un nuevo camion')
        camiones+=1
        carga_sobrante=(cantidad_kilos-carga_camion)
        print('Te sobran: ',carga_sobrante , ' Kilos')

        valor_pedido= camiones*765000+carga_sobrante*kilo_gas_adicional+valor_transporte_uso_camion
        print(f'El precio del pedido es de: $ {valor_pedido}')
    else:
        print('Como no completaste el camion, deberás pagar 1.700 por kilo de gas, más $100.000 por transporte')
        valor_pedido=kilo_gas_adicional*carga_actual+valor_transporte_uso_camion
        print(f'Valor de pedido: ${valor_pedido}')

    print('\nImpresion de boleta')
    print(f'Cliente: {nombre_Cliente}')
    print(f'Telefono: {telefono}')
    print(f'Cantidad kilos: {cantidad_kilos}')
    print(f'Camiones: {camiones}')
    print(f'Total: {valor_pedido}')
    nuevo_pedido=int(input('\n¿Desea hacer otro pedido?: 1 (si)/2 (no)'))
else:
    if nuevo_pedido==2:
        print('Muchas gracias por su compra')
        menu==False










    



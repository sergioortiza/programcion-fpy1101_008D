import os
import time
cls= "cls"
sw=1
pkr=4500
otkr=5000
pvn=5200
angel=4800
totalap=0
totalap1=0
totalap2=0
totalap3=0
totalap4=0
desc= "soyotaku"
totaldesc= 0 
cantidad= 0
cantidad1= 0
cantidad2= 0
cantidad3=0
cantidad4= 0
totalapd= 0


while sw==1:
    print("Bienvenido a Otaku Sushii :3 porfavor seleciona una opcion")
    print("1. Pikachu Roll $4500")
    print("2. Otaku Roll $5000")
    print("3. Pulpo Venenoso Roll $5200")
    print("4. Anguila Eléctrica Roll $4800")
    print("5. Salir")
    op=int(input("Porvafor selecciona una opcion: "))
    try:
        if (op>0 and op< 6):
            if op==1:
                cantidad1=int(input("Cuantos Pikachu Rolls deseas?: "))
                cantidad=(cantidad1+cantidad)
                totalap1=(cantidad1*pkr)
                totalap=(totalap+totalap1)
                print(f"El total a pagar es: ${totalap}")
                continu=int(input("Deseas proceder al pago? 1)cancelar pedido 3)pagar: "))
                if continu== 1:
                    print("Cierre exitoso no se hizo ningun cobro")
                    sw=0
                elif continu==2:
                    sw=3
            if op==2:
                cantidad2=int(input("Cuantos Otaku Rolls deseas?: "))
                cantidad=(cantidad2+cantidad)
                totalap2=(cantidad2*otkr)
                totalap=(totalap+totalap2)
                print(f"El total a pagar es: ${totalap}")
                continu=int(input("Deseas proceder al pago? 1)candelar pedido 3)pagar: "))
                if continu== 1:
                    print("Cierre exitoso no se hizo ningun cobro")
                    sw=0
                elif continu==2:
                    sw=3
            if op== 3:
                cantidad3=int(input("Cuantos Pulpos Venenosos Rolls deseas?: "))
                cantidad=(cantidad3+cantidad)
                totalap3=(cantidad3*pvn)
                totalap=(totalap+totalap3)
                print(f"El total a pagar es: ${totalap}")
                continu=int(input("Deseas proceder al pago? 1)cancelar pedido 2)pagar: "))
                if continu== 1:
                    print("Cierre exitoso no se hizo ningun cobro")
                    sw=0
                elif continu==2:
                    sw=3
            if op==4:
                cantidad4=int(input("Cuantos Anguilas Electricas Rolls deseas?: "))
                cantidad=(cantidad4+cantidad)
                totalap4=(cantidad4*angel)
                totalap=(totalap+totalap4)
                print(f"El total a pagar es: ${totalap}")
                continu=int(input("Deseas proceder al pago? 1)cancelar pedido 2)pagar: "))
                if continu== 1:
                    print("Cierre exitoso no se hizo ningun cobro")
                    sw=0
                elif continu==2:
                    sw=3
            if op==5: 
                print("Cierre exitoso no se realizo ningun cobro adios ;)")
                sw= 0
    except:
        print("Valor erroneo intenta nuevamente")
    continu=int(input("Desea realizar otra compra? si/1 no/0 "))
    if continu==1:
        sw=1
    else:
        continu==0
        print("Procediendo al pago:3")
        break


while sw==3:
    print(f"El total a pagar es ${totalap}")
    op=int(input("Tienes descuento? si/1 no /0: "))
    try:
        if op==1:
            descuento=input("Porfavor ingresa el codigo de descuento: ")
            if descuento == desc:
                totaldesc= round(totalap*0.10)
                totalapd= round(totalap-totaldesc)
                print("Se ha realizado un descuento del 10% :3")
                sw=4
            else:
                descuento != desc
                print("Codigo incorrecto")
                continu=(input("Desea intentar otra vez? si/y no/x "))
                if continu== "x":
                    print("No se realizo ningun descuento :c")
                    totalapd=(totalap+totalapd)
                    sw=4
        if op==0: 
            print("No se realizo ningun descuento :c")
            totalapd=(totalap+totalapd)
            sw=4
    except:
        ("Valor erroneo intenta nuevamente")

time.sleep(3)
os.system(cls)

while sw==4:
    print("*"*30)
    print(f"Toral productos {cantidad}")
    print("*"*30)
    print(f"canitdad Pikachu Roll= {cantidad1}")
    print(f"Cantidad Otaku roll= {cantidad2}")
    print(f"Canridad Pulpos Venenosos= {cantidad3}")
    print(f"Cantidad Anguilas Electricas= {cantidad4}")
    print("*"*30)
    print(f"subtotal= {totalap}")
    print(f"total descuento {totaldesc}")
    print(f"Total final= {totalapd}")
    sw=5



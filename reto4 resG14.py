def CrearDiccionarioEstudiante(Informacion: str) -> dict:
    
    Estudiantes = Informacion.split('%')
    Diccionario = {}
    TodoSeparado = Estudiantes[0].split(';')
    for i in Estudiantes[1:]:
        Estudiante = {}
        TodaLaInfo = i.split(';')
        for j in range(1,len(TodoSeparado)):
            if TodoSeparado[j] == 'Promedio':
                TodaLaInfo[j] = float(TodaLaInfo[j])
            Estudiante[TodoSeparado[j]] = TodaLaInfo[j]
        Diccionario[TodaLaInfo[0]] = Estudiante
        
    return Diccionario 
   
def PromedioMayorMenor(DiccionarioEstudiante: list)->str:
    
    NotaMayor = 0
    NotaMenor = 234234
    
    Suma = 0
    for i in DiccionarioEstudiante:
        if(DiccionarioEstudiante[i]['Promedio'] > NotaMayor):
            NotaMayor = DiccionarioEstudiante[i]['Promedio']
            
        if(DiccionarioEstudiante[i]['Promedio'] < NotaMenor):
            NotaMenor = DiccionarioEstudiante[i]['Promedio']
            
        Suma += DiccionarioEstudiante[i]['Promedio']
    
        
    Promedio = Suma /len(DiccionarioEstudiante)
    return f"El promedio de notas de los {len(DiccionarioEstudiante)} estudiantes es: {Promedio}, la nota mas alta es: {NotaMayor} y la nota menor es: {NotaMenor}"

def ImprimirLaInfo(DiccionarioEstudiante: dict )->str:
    for i in DiccionarioEstudiante:
        for key in DiccionarioEstudiante[i]:
            print(key, ":", DiccionarioEstudiante[i][key])
        print()
                

	
datos_estudiantes  = "TLI;Nombre;CC;Teléfono;Promedio%234jj234d2;Santiago Perez;1006614805;30139020352;4.5%fff342345d;Carol Martinez;111234882;3213213214;4.9%fgfg3333d2;Juan Felacio;11124992;3092404231;2.2"
datos_estudiantes2  = "TLI;Nombre;CC;Teléfono;Promedio%dg8288wj3;Alejandra Gonzales;11112342;3002431243;3.2%ee23553mmd;Andrea Garcia;1002341242;3013090222;1.2"
listaestudnates = [CrearDiccionarioEstudiante(datos_estudiantes), CrearDiccionarioEstudiante(datos_estudiantes2)]
infor = list(map(PromedioMayorMenor, listaestudnates))

ImprimirLaInfo(CrearDiccionarioEstudiante(datos_estudiantes))
ImprimirLaInfo(CrearDiccionarioEstudiante(datos_estudiantes2))

datos_estudiantes  = "TLI;Nombre;CC;Teléfono;Promedio%234jj234d2;Santiago Perez;1006614805;30139020352;4.5%fff342345d;Carol Martinez;111234882;3213213214;4.9%fgfg3333d2;Juan Felacio;11124992;3092404231;2.2"
datos_estudiantes2  = "TLI;Nombre;CC;Teléfono;Promedio%dg8288wj3;Alejandra Gonzales;11112342;3002431243;3.2%ee23553mmd;Andrea Garcia;1002341242;3013090222;1.2"
listaestudnates = [CrearDiccionarioEstudiante(datos_estudiantes), CrearDiccionarioEstudiante(datos_estudiantes2)]
infor = list(map(PromedioMayorMenor, listaestudnates))
print(infor)
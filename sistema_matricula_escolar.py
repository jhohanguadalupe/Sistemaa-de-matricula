# ------------------------
# FUNCIONES DEL SISTEMA
# ------------------------
# Pide una opción por teclado y repite hasta que esté dentro de opciones_validas
def pedir_opcion(mensaje, opciones_validas):
    while True:
        print(mensaje)
        entrada = input()
        if entrada in opciones_validas:
            return entrada
        print("[ERROR]: Entrada inválida. Elija una de las opciones mostradas.")

# Pide un texto y repite hasta que el usuario escriba algo (no vacío)
def pedir_texto_no_vacio(mensaje, mensaje_error):
    while True:
        print(mensaje)
        texto = input()
        if texto != "":
            return texto
        print(mensaje_error)

# Devuelve True si el texto contiene únicamente caracteres del 0 al 9
def solo_digitos(texto):
    for caracter in texto:
        if caracter < "0" or caracter > "9":
            return False
    return True


# Pide un número (solo dígitos) cuya longitud esté entre largo_min y largo_max
# 'nombre' se usa en los mensajes de error (ej: "El DNI")
def pedir_numero(mensaje, nombre, largo_min, largo_max):
    while True:
        print(mensaje)
        numero = input()
        longitud = len(numero)
        if not solo_digitos(numero):
            print(f"[ERROR]: {nombre} debe contener únicamente números.")
        elif longitud < largo_min or longitud > largo_max:
            if largo_min == largo_max:
                print(f"[ERROR]: {nombre} debe tener exactamente {largo_min} dígitos. (Ingresaste: {longitud})")
            else:
                print(f"[ERROR]: {nombre} debe tener entre {largo_min} y {largo_max} dígitos. (Ingresaste: {longitud})")
        else:
            return numero

# Imprime la ficha de matrícula exitosa con los datos del alumno y del responsable
def mostrar_ficha(apellidos_est, nombres_est, tipo_doc_est, num_doc_est,
                  fecha_nac_est, sexo_est, grado_nivel_est, colegio_proc_est,
                  apellidos_resp, nombres_resp, parentesco_resp,
                  telefono_resp, correo_resp, direccion_resp, distrito_resp,
                  vacantes_disponibles):
    print(" ESTADO DE MATRÍCULA: [ EXITOSA ]")
    print("------------------------------------------------------")
    print(f" Alumno:      {apellidos_est}, {nombres_est}")
    print(f" Doc. Alumno: {tipo_doc_est} - {num_doc_est}")
    print(f" F. Nac:      {fecha_nac_est} | Sexo: {sexo_est}")
    print(f" Grado/Nivel: {grado_nivel_est}")
    print(f" Procedencia: {colegio_proc_est}")
    print("------------------------------------------------------")
    print(f" Responsable: {apellidos_resp}, {nombres_resp} ({parentesco_resp})")
    print(f" Contacto:    Tel: {telefono_resp}")
    print(f" Correo:      {correo_resp}")
    print(f" Ubicación:   {direccion_resp} - {distrito_resp}")
    print("------------------------------------------------------")
    print(f" Vacantes escolares restantes: {vacantes_disponibles}")

# ------------------------
# VARIABLES DEL SISTEMA
# ------------------------
vacantes_disponibles = 5   # Cupos disponibles en el colegio
numero_estudiante = 1      # Número correlativo del estudiante que se registra
estudiantes = []           # Lista con los estudiantes matriculados
 
# --------------------------------
# ENCABEZADO DEL SISTEMA
# --------------------------------
print("========================================")
print("--- SISTEMA DE MATRÍCULA ESCOLAR ---")
print(" Registrando al estudiante número:", numero_estudiante)
print("========================================")
print(" ")

# --------------------------------
# SECCIÓN 1: DATOS DEL ESTUDIANTE
# --------------------------------
print("--------------------------")
print("1. DATOS DEL ESTUDIANTE")
print("--------------------------")
print(" ")
# Validación: Nombres no vacíos
nombres_est = pedir_texto_no_vacio("Ingrese los nombres completos del estudiante:", "[ERROR]: El nombre no puede quedar vacío.")

# Validación: Apellidos no vacíos
apellidos_est = pedir_texto_no_vacio("Ingrese los apellidos completos del estudiante:", "[ERROR]: El apellido no puede quedar vacío.")
 
# Menú: Tipo de documento Estudiante
print("\nSeleccione el tipo de documento del estudiante:")
print("  1. DNI")
print("  2. Pasaporte")

entrada_doc = pedir_opcion("Elija una opción (1 o 2):", ["1", "2"])
 
if entrada_doc == "1":
    tipo_doc_est = "DNI"
else:
    tipo_doc_est = "Pasaporte"
 
# Validación de documento Estudiante
print("")
if tipo_doc_est == "DNI":
    num_doc_est = pedir_numero(f"Ingrese el número de documento ({tipo_doc_est}):", f"El {tipo_doc_est}", 8, 8)
else:
    num_doc_est = pedir_numero(f"Ingrese el número de documento ({tipo_doc_est}):", f"El {tipo_doc_est}", 9, 9)
 
# Validación: Fecha de nacimiento básica
print("")
dato_valido = False
while not dato_valido:
    print("Ingrese la fecha de nacimiento (DD/MM/AAAA):")
    fecha_nac_est = input()
    # Primero validamos el tamaño para evitar errores si el usuario presiona ENTER vacío
    if len(fecha_nac_est) == 10 and fecha_nac_est[2] == "/" and fecha_nac_est[5] == "/":
        dato_valido = True
    else:
        print("[ERROR]: Formato incorrecto. Debe escribirlo exactamente como: DD/MM/AAAA")

# Nacionalidad del estudiante
print("\nIngrese la nacionalidad:")
nacionalidad_est = input()
 
# Menú: Sexo
print("\nSeleccione el sexo del estudiante:")
print("  1. Masculino (M)")
print("  2. Femenino (F)")
entrada_sexo = pedir_opcion("Elija una opción (1 o 2):", ["1", "2"])
 
if entrada_sexo == "1":
    sexo_est = "M"
else:
    sexo_est = "F"
 
# Grado y nivel al que postula
print("\nIngrese el grado y nivel al que postula (ej: 1ro Primaria):")
grado_nivel_est = input()
print("")
# Colegio de procedencia (opcional: vacío se guarda como "No aplica")
print("Ingrese el colegio de procedencia (si no aplica, presione ENTER):")
colegio_proc_est = input()
if colegio_proc_est == "":
    colegio_proc_est = "No aplica"
print("")
 
# ----------------------------------------------
# SECCIÓN 2: DATOS DEL PADRE, MADRE O APODERADO
# ----------------------------------------------
print("----------------------------------------")
print("2. DATOS DEL PADRE, MADRE O APODERADO")
print("----------------------------------------")
 
# Menú: Parentesco
print("Seleccione el parentesco con el estudiante:")
print("  1. Madre")
print("  2. Padre")
print("  3. Apoderado / Tutor Legal")

entrada_parentesco = pedir_opcion("Elija una opción (1, 2 o 3):", ["1", "2", "3"])
# Define el parentesco y el artículo para los mensajes siguientes
if entrada_parentesco == "1":
    parentesco_resp = "Madre"
    articulo = "de la"
elif entrada_parentesco == "2":
    parentesco_resp = "Padre"
    articulo = "del"
elif entrada_parentesco == "3":
    parentesco_resp = "Apoderado"
    articulo = "del/de la"

 # Validación: Nombres del responsable no vacíos
print("")
nombres_resp = pedir_texto_no_vacio(f"Ingrese los nombres completos {articulo} {parentesco_resp} responsable:", "[ERROR]: El nombre del responsable no puede quedar vacío.")

# Validación: Apellidos del responsable no vacíos
print("")
apellidos_resp = pedir_texto_no_vacio(f"Ingrese los apellidos completos {articulo} {parentesco_resp} responsable:", "[ERROR]: El apellido del responsable no puede quedar vacío.")
 
# Menú: Selección de documento del Responsable
print("\nSeleccione el tipo de documento del responsable:")
print("  1. DNI")
print("  2. Carné de Extranjería / Pasaporte")
entrada_doc = pedir_opcion("Elija una opción (1 o 2):", ["1", "2"])
if entrada_doc == "1":
    tipo_doc_resp = "DNI"
else:
    tipo_doc_resp = "CE/Pasaporte"
 
# VALIDACIÓN DEL DOCUMENTO DEL RESPONSABLE
print("")
if tipo_doc_resp == "DNI":
    num_doc_resp = pedir_numero(f"Ingrese el número de documento ({tipo_doc_resp}):", "El DNI", 8, 8)
else:
    num_doc_resp = pedir_numero(f"Ingrese el número de documento ({tipo_doc_resp}):", "El documento", 8, 12)
 
# Validación de teléfono celular
print("")
telefono_resp = pedir_numero("Ingrese el teléfono / celular de contacto (9 dígitos):", "El teléfono", 9, 9)

# Validación: Correo electrónico con '@' obligado
print("\nIngrese el correo electrónico:")
dato_valido = False
while not dato_valido:
    correo_resp = input()
    if "@" in correo_resp:
        dato_valido = True
    else:
        print("")
        print("[ERROR]: Correo inválido. Debe contener obligatoriamente un símbolo \"@\". Reintente:")
# Dirección y distrito del responsable
print("Ingrese la dirección domiciliaria actual:")
direccion_resp = input()
print("Ingrese el distrito / provincia:")
distrito_resp = input()
print("")
 
# ------------------------------------------
# SECCIÓN 3: VERIFICACIÓN DE REQUISITOS
# ------------------------------------------
print("------------------------------------------------------")
print("¿Cuenta con todos los documentos físicos requeridos?")
print("  1. Sí, tengo todo")
print("  2. No, me faltan documentos")
print("------------------------------------------------------")
print("")
entrada_requisitos = pedir_opcion("Elija una opción (1 o 2):", ["1", "2"])
# True si el responsable entregó todos los documentos físicos
if entrada_requisitos == "1":
    tiene_documentos = True
else:
    tiene_documentos = False

# --------------------------------------------
# SECCIÓN 4: FICHA FINAL Y REGISTRO
# --------------------------------------------
print("\n======================================================")
print("            FICHA OFICIAL DE REVISIÓN                 ")
print("======================================================")

# Con documentos completos: se descuenta una vacante, se muestra la ficha y se guarda al estudiante
if tiene_documentos:
    vacantes_disponibles = vacantes_disponibles - 1
    mostrar_ficha(apellidos_est, nombres_est, tipo_doc_est, num_doc_est,
                  fecha_nac_est, sexo_est, grado_nivel_est, colegio_proc_est,
                  apellidos_resp, nombres_resp, parentesco_resp,
                  telefono_resp, correo_resp, direccion_resp, distrito_resp,
                  vacantes_disponibles)
    estudiante = [numero_estudiante, apellidos_est, nombres_est, tipo_doc_est,
                  num_doc_est, fecha_nac_est, sexo_est, grado_nivel_est,
                  colegio_proc_est, apellidos_resp, nombres_resp, parentesco_resp,
                  telefono_resp, correo_resp, direccion_resp, distrito_resp]
    estudiantes.append(estudiante)
# Sin documentos completos: la matrícula se rechaza y no se guarda
else:
    print(" ESTADO DE MATRÍCULA: [ RECHAZADA / OBSERVADA ]")
    print("------------------------------------------------------")
    print(" [MOTIVO]: El expediente físico está incompleto.")
    print(" El postulante no puede registrarse sin los requisitos.")

print("======================================================\n")

# Resumen de estudiantes registrados
print("Estudiantes guardados:", len(estudiantes))
for e in estudiantes:
    print(e[0], "-", e[1], e[2], "-", e[4])

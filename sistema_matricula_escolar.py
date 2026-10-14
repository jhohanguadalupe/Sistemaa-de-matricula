# ------------------------
# VARIABLES DEL SISTEMA
# ------------------------
vacantes_disponibles = 5
numero_estudiante = 1
 
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
dato_valido = False
while not dato_valido:
    print("Ingrese los nombres completos del estudiante:")
    nombres_est = input()
    if nombres_est != "":
        dato_valido = True
    else:
        print("[ERROR]: El nombre no puede quedar vacío.")

# Validación: Apellidos no vacíos
print("")
dato_valido = False
while not dato_valido:
    print("Ingrese los apellidos completos del estudiante:")
    apellidos_est = input()
    if apellidos_est != "":
        dato_valido = True
    else:
        print("[ERROR]: El apellido no puede quedar vacío.")
 
# Menú: Tipo de documento Estudiante
print("\nSeleccione el tipo de documento del estudiante:")
print("  1. DNI")
print("  2. Pasaporte")
dato_valido = False
while not dato_valido:
    print("Elija una opción (1 o 2):")
    entrada_doc = input()
    if entrada_doc == "1" or entrada_doc == "2":
        dato_valido = True
    else:
        print("[ERROR]: Entrada inválida. Coloque 1 o 2.")
 
if entrada_doc == "1":
    tipo_doc_est = "DNI"
else:
    tipo_doc_est = "Pasaporte"
 
# Validación de documento Estudiante
print("")
doc_valido = False
while not doc_valido:
    print("Ingrese el número de documento (", tipo_doc_est, "):")
    num_doc_est = input()
    longitud_doc = len(num_doc_est)
    dato_valido = True
    for i in range(1, longitud_doc + 1):
        caracter_actual = num_doc_est[i - 1]
        if caracter_actual < "0" or caracter_actual > "9":
            dato_valido = False
 
    if not dato_valido:
        print("[ERROR]: El documento debe contener únicamente números.")
    else:
        if tipo_doc_est == "DNI":
            if longitud_doc == 8:
                doc_valido = True
            else:
                print("[ERROR]: El DNI debe tener exactamente 8 dígitos. (Ingresaste: ", longitud_doc, ")")
        else:
            if longitud_doc == 9:
                doc_valido = True
            else:
                print("[ERROR]: El Pasaporte debe tener exactamente 9 dígitos. (Ingresaste: ", longitud_doc, ")")
 
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

print("\nIngrese la nacionalidad:")
nacionalidad_est = input()
 
# Menú: Sexo
print("\nSeleccione el sexo del estudiante:")
print("  1. Masculino (M)")
print("  2. Femenino (F)")
dato_valido = False
while not dato_valido:
    print("Elija una opción (1 o 2):")
    entrada_sexo = input()
    if entrada_sexo == "1" or entrada_sexo == "2":
        dato_valido = True
    else:
        print("[ERROR]: Entrada inválida. Coloque 1 o 2.")
 
if entrada_sexo == "1":
    sexo_est = "M"
else:
    sexo_est = "F"
 
print("\nIngrese el grado y nivel al que postula (ej: 1ro Primaria):")
grado_nivel_est = input()
print("")
print("Ingrese el colegio de procedencia (si no aplica, presione ENTER):")
colegio_proc_est = input()
if colegio_proc_est == "":
    colegio_proc_est = "No aplica"
print("")
 
# ----------------------------------------------
# DATOS DEL PADRE, MADRE O APODERADO
# ----------------------------------------------
print("----------------------------------------")
print("2. DATOS DEL PADRE, MADRE O APODERADO")
print("----------------------------------------")
 
# Menú: Parentesco
print("Seleccione el parentesco con el estudiante:")
print("  1. Madre")
print("  2. Padre")
print("  3. Apoderado / Tutor Legal")
dato_valido = False
while not dato_valido:
    print("Elija una opción (1, 2 o 3):")
    entrada_parentesco = input()
    if entrada_parentesco == "1" or entrada_parentesco == "2" or entrada_parentesco == "3":
        dato_valido = True
    else:
        print("[ERROR]: Entrada inválida. Elija 1, 2 o 3.")
 
if entrada_parentesco == "1":
    parentesco_resp = "Madre"
    articulo = "la"
elif entrada_parentesco == "2":
    parentesco_resp = "Padre"
    articulo = "el"
elif entrada_parentesco == "3":
    parentesco_resp = "Apoderado"
    articulo = "la/el"

 # Validación: Nombres del responsable no vacíos
print("")
dato_valido = False
while not dato_valido:
    print(f"Ingrese los nombres completos de {articulo} {parentesco_resp} responsable:")
    nombres_resp = input()
    if nombres_resp != "":
        dato_valido = True
    else:
        print("[ERROR]: El nombre del responsable no puede quedar vacío.")

# Validación: Apellidos del responsable no vacíos
print("")
dato_valido = False
while not dato_valido:
    print(f"Ingrese los apellidos completos de {articulo} {parentesco_resp} responsable:")
    apellidos_resp = input()
    if apellidos_resp != "":
        dato_valido = True
    else:
        print("[ERROR]: El apellido del responsable no puede quedar vacío.")
 
# Menú: Selección de documento del Responsable
print("\nSeleccione el tipo de documento del responsable:")
print("  1. DNI")
print("  2. Carné de Extranjería / Pasaporte")
dato_valido = False
while not dato_valido:
    print("Elija una opción (1 o 2):")
    entrada_doc = input()
    if entrada_doc == "1" or entrada_doc == "2":
        dato_valido = True
    else:
        print("[ERROR]: Entrada inválida. Coloque 1 o 2.")
 
if entrada_doc == "1":
    tipo_doc_resp = "DNI"
else:
    tipo_doc_resp = "CE/Pasaporte"
 
# VALIDACIÓN DEL DOCUMENTO DEL RESPONSABLE
print("")
doc_valido = False
while not doc_valido:
    print("Ingrese el número de documento (", tipo_doc_resp, "):")
    num_doc_resp = input()
    longitud_doc = len(num_doc_resp)
    dato_valido = True
    for i in range(1, longitud_doc + 1):
        caracter_actual = num_doc_resp[i - 1]
        if caracter_actual < "0" or caracter_actual > "9":
            dato_valido = False
 
    if not dato_valido:
        print("[ERROR]: El documento debe contener únicamente números.")
    else:
        if tipo_doc_resp == "DNI":
            if longitud_doc == 8:
                doc_valido = True
            else:
                print("[ERROR]: El DNI debe tener exactamente 8 dígitos. (Ingresaste: ", longitud_doc, ")")
        else:
            if longitud_doc >= 8 and longitud_doc <= 12:
                doc_valido = True
            else:
                print("[ERROR]: Documento inválido. Debe tener entre 8 y 12 dígitos.")
 
# Validación de teléfono celular
print("")
dato_valido = False
while not dato_valido:
    print("Ingrese el teléfono / celular de contacto (9 dígitos):")
    telefono_resp = input()
    longitud_doc = len(telefono_resp)
    doc_valido = True
    for i in range(1, longitud_doc + 1):
        caracter_actual = telefono_resp[i - 1]
        if caracter_actual < "0" or caracter_actual > "9":
            doc_valido = False
 
    if not doc_valido:
        print("[ERROR]: El teléfono no debe contener letras ni espacios.")
    else:
        if longitud_doc == 9:
            dato_valido = True
        else:
            print("[ERROR]: El número celular debe tener exactamente 9 dígitos. (Ingresaste: ", longitud_doc, ")")
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
print("Ingrese la dirección domiciliaria actual:")
direccion_resp = input()
print("Ingrese el distrito / provincia:")
distrito_resp = input()
print("")
 
# -----------------------------
# VERIFICACIÓN Y TICKET FINAL
# -----------------------------
print("------------------------------------------------------")
print("¿Cuenta con todos los documentos físicos requeridos?")
print("  1. Sí, tengo todo")
print("  2. No, me faltan documentos")
print("------------------------------------------------------")
print("")
dato_valido = False
while not dato_valido:
    print("Elija una opción (1 o 2):")
    entrada_requisitos = input()
    if entrada_requisitos == "1" or entrada_requisitos == "2":
        dato_valido = True
    else:
        print("[ERROR]: Entrada inválida. Presione 1 o 2.")
 
if entrada_requisitos == "1":
    tiene_documentos = True
else:
    tiene_documentos = False

# --------------------------------------------
# IMPRESIÓN DEL REPORTE O TICKET ESTRUCTURADO
# --------------------------------------------
print("\n======================================================")
print("            FICHA OFICIAL DE REVISIÓN                 ")
print("======================================================")

if tiene_documentos:
    vacantes_disponibles = vacantes_disponibles - 1
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
    print(f" Correo:       {correo_resp}")
    print(f" Ubicación:   {direccion_resp} - {distrito_resp}")
    print("------------------------------------------------------")
    print(f" Vacantes escolares restantes: {vacantes_disponibles}")
else:
    print(" ESTADO DE MATRÍCULA: [ RECHAZADA / OBSERVADA ]")
    print("------------------------------------------------------")
    print(" [MOTIVO]: El expediente físico está incompleto.")
    print(" El postulante no puede registrarse sin los requisitos.")

print("======================================================\n")

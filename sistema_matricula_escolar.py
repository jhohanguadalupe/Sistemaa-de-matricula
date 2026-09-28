# ==========================================================================
# SISTEMA DE MATRÍCULA ESCOLAR (BASADO EN FICHA)
# Traducción literal del pseudocódigo de PSeInt "Matricula_Colegio_Ficha_Oficial"
# a Python. No se modifica la lógica ni el orden del algoritmo original,
# solo se traduce la sintaxis de PSeInt a sintaxis de Python.
#
# Nota: en PSeInt hay que "Definir" cada variable con su tipo antes de
# usarla (Como Cadena, Como Entero, Como Lógico). En Python NO se declaran
# las variables ni su tipo: una variable existe desde el momento en que se
# le asigna un valor por primera vez. Por eso las líneas "Definir ..." del
# pseudocódigo no tienen una línea equivalente aquí.
# ==========================================================================

# --------------------------------------------------------------------
# VARIABLES DEL SISTEMA (equivalen a: vacantes_disponibles, numero_estudiante)
# --------------------------------------------------------------------
vacantes_disponibles = 5
numero_estudiante = 1

print('--- SISTEMA DE MATRÍCULA ESCOLAR (BASADO EN FICHA) ---')
print('Registrando al estudiante número: ', numero_estudiante)
print('------------------------------------------------------')

# --------------------------------------------------------------------
# SECCIÓN 1: DATOS DEL ESTUDIANTE
# --------------------------------------------------------------------
print('1. DATOS DEL ESTUDIANTE')
print('Ingrese los nombres completos del estudiante:')
nombres_est = input()
print('Ingrese los apellidos completos del estudiante:')
apellidos_est = input()

# Menú: Tipo de documento Estudiante
print('Seleccione el tipo de documento del estudiante:')
print('1. DNI')
print('2. Pasaporte')
dato_valido = False
# Nota: "Mientras NO dato_valido Hacer" en PSeInt equivale a
# "while not dato_valido:" en Python. La palabra "not" niega el valor
# lógico, igual que "NO" en PSeInt.
while not dato_valido:
    print('Elija una opción (1 o 2):')
    entrada_doc = input()
    if entrada_doc == '1' or entrada_doc == '2':
        dato_valido = True
    else:
        print('[ERROR]: Entrada inválida. Coloque 1 o 2.')

if entrada_doc == '1':
    tipo_doc_est = 'DNI'
else:
    tipo_doc_est = 'Pasaporte'

# Validación de documento Estudiante
doc_valido = False
while not doc_valido:
    print('Ingrese el número de documento (', tipo_doc_est, '):')
    num_doc_est = input()
    longitud_doc = len(num_doc_est)  # Longitud(...) en PSeInt equivale a len(...) en Python
    dato_valido = True
    # Nota: Subcadena(cadena, i, i) en PSeInt es 1-indexado (el primer
    # caracter está en la posición 1). En Python los strings son
    # 0-indexados, por eso se usa num_doc_est[i - 1] para obtener el
    # mismo caracter que Subcadena(num_doc_est, i, i).
    for i in range(1, longitud_doc + 1):
        caracter_actual = num_doc_est[i - 1]
        if caracter_actual < '0' or caracter_actual > '9':
            dato_valido = False

    if not dato_valido:
        print('[ERROR]: El documento debe contener únicamente números.')
    else:
        if tipo_doc_est == 'DNI':
            if longitud_doc == 8:
                doc_valido = True
            else:
                print('[ERROR]: El DNI debe tener exactamente 8 dígitos. (Ingresaste: ', longitud_doc, ')')
        else:
            if longitud_doc == 9:
                doc_valido = True
            else:
                print('[ERROR]: El Pasaporte debe tener exactamente 9 dígitos. (Ingresaste: ', longitud_doc, ')')

print('Ingrese la fecha de nacimiento (DD/MM/AAAA):')
fecha_nac_est = input()
print('Ingrese la nacionalidad:')
nacionalidad_est = input()

# Menú: Sexo
print('Seleccione el sexo del estudiante:')
print('1. Masculino (M)')
print('2. Femenino (F)')
dato_valido = False
while not dato_valido:
    print('Elija una opción (1 o 2):')
    entrada_sexo = input()
    if entrada_sexo == '1' or entrada_sexo == '2':
        dato_valido = True
    else:
        print('[ERROR]: Entrada inválida. Coloque 1 o 2.')

if entrada_sexo == '1':
    sexo_est = 'M'
else:
    sexo_est = 'F'

print('Ingrese el grado y nivel al que postula (ej: 1ro Primaria):')
grado_nivel_est = input()
print('Ingrese el colegio de procedencia (si no aplica, presione ENTER):')
colegio_proc_est = input()
if colegio_proc_est == '':
    colegio_proc_est = 'No aplica'

print('')

# --------------------------------------------------------------------
# SECCIÓN 2: DATOS DEL PADRE, MADRE O APODERADO
# --------------------------------------------------------------------
print('2. DATOS DEL PADRE, MADRE O APODERADO')

# Menú: Parentesco
print('Seleccione el parentesco con el estudiante:')
print('1. Madre')
print('2. Padre')
print('3. Apoderado / Tutor Legal')
dato_valido = False
while not dato_valido:
    print('Elija una opción (1, 2 o 3):')
    entrada_parentesco = input()
    if entrada_parentesco == '1' or entrada_parentesco == '2' or entrada_parentesco == '3':
        dato_valido = True
    else:
        print('[ERROR]: Entrada inválida. Elija 1, 2 o 3.')

# Nota: "Según ... Hacer / FinSegún" en PSeInt es un selector de casos
# (parecido a "switch" en otros lenguajes). Python no tiene una
# instrucción "Según", así que se traduce como una cadena de
# if / elif / else, evaluando la misma variable en cada caso.
if entrada_parentesco == '1':
    parentesco_resp = 'Madre'
    articulo = 'la'
elif entrada_parentesco == '2':
    parentesco_resp = 'Padre'
    articulo = 'el'
elif entrada_parentesco == '3':
    parentesco_resp = 'Apoderado'
    articulo = 'la/el'

print('Ingrese los nombres y apellidos de ', articulo, ' ', parentesco_resp, ' responsable:')
nombre_resp = input()

# ==================================================
# NUEVO MENÚ: SELECCIÓN DE DOCUMENTO DEL RESPONSABLE
# ==================================================
print('Seleccione el tipo de documento del responsable:')
print('1. DNI')
print('2. Carné de Extranjería / Pasaporte')
dato_valido = False
while not dato_valido:
    print('Elija una opción (1 o 2):')
    entrada_doc = input()
    if entrada_doc == '1' or entrada_doc == '2':
        dato_valido = True
    else:
        print('[ERROR]: Entrada inválida. Coloque 1 o 2.')

if entrada_doc == '1':
    tipo_doc_resp = 'DNI'
else:
    tipo_doc_resp = 'CE/Pasaporte'

# VALIDACIÓN DEL DOCUMENTO DEL RESPONSABLE
doc_valido = False
while not doc_valido:
    print('Ingrese el número de documento (', tipo_doc_resp, '):')
    num_doc_resp = input()
    longitud_doc = len(num_doc_resp)
    dato_valido = True
    for i in range(1, longitud_doc + 1):
        caracter_actual = num_doc_resp[i - 1]
        if caracter_actual < '0' or caracter_actual > '9':
            dato_valido = False

    if not dato_valido:
        print('[ERROR]: El documento debe contener únicamente números.')
    else:
        if tipo_doc_resp == 'DNI':
            if longitud_doc == 8:
                doc_valido = True
            else:
                print('[ERROR]: El DNI debe tener exactamente 8 dígitos. (Ingresaste: ', longitud_doc, ')')
        else:
            # Para Carné de extranjería o Pasaporte aceptamos longitudes comunes (ej: de 9 a 12 dígitos)
            if longitud_doc >= 8 and longitud_doc <= 12:
                doc_valido = True
            else:
                print('[ERROR]: Documento inválido. Debe tener entre 8 y 12 dígitos.')

# Validación de teléfono celular
dato_valido = False
while not dato_valido:
    print('Ingrese el teléfono / celular de contacto (9 dígitos):')
    telefono_resp = input()
    longitud_doc = len(telefono_resp)
    doc_valido = True
    for i in range(1, longitud_doc + 1):
        caracter_actual = telefono_resp[i - 1]
        if caracter_actual < '0' or caracter_actual > '9':
            doc_valido = False

    if not doc_valido:
        print('[ERROR]: El teléfono no debe contener letras ni espacios.')
    else:
        if longitud_doc == 9:
            dato_valido = True
        else:
            print('[ERROR]: El número celular debe tener exactamente 9 dígitos. (Ingresaste: ', longitud_doc, ')')

print('Ingrese el correo electrónico:')
correo_resp = input()
print('Ingrese la dirección domiciliaria actual:')
direccion_resp = input()
print('Ingrese el distrito / provincia:')
distrito_resp = input()

print('')

# --------------------------------------------------------------------
# VERIFICACIÓN Y TICKET FINAL
# --------------------------------------------------------------------
print('¿Cuenta con todos los documentos físicos requeridos?')
print('1. Sí, tengo todo')
print('2. No, me faltan documentos')
dato_valido = False
while not dato_valido:
    print('Elija una opción (1 o 2):')
    entrada_requisitos = input()
    if entrada_requisitos == '1' or entrada_requisitos == '2':
        dato_valido = True
    else:
        print('[ERROR]: Entrada inválida. Presione 1 o 2.')

if entrada_requisitos == '1':
    tiene_documentos = True
else:
    tiene_documentos = False

if tiene_documentos == True:
    if numero_estudiante < 10:
        # Concatenar(...) en PSeInt une textos; en Python se hace con el
        # operador "+". ConvertirATexto(...) equivale a str(...).
        ticket_formato = '0' + str(numero_estudiante)
    else:
        ticket_formato = str(numero_estudiante)

    print('')
    print('==================================================================')
    print('                 TICKET DE CONFIRMACIÓN DE FICHA                  ')
    print('==================================================================')
    print(' Nro. Matrícula       : ', ticket_formato)
    print(' Estado               : MATRÍCULA CONFIRMADA')
    print('------------------------------------------------------------------')
    print(' 1. DATOS DEL ESTUDIANTE:')
    print(' Nombres y Apellidos  : ', nombres_est, ' ', apellidos_est)
    print(' Documento            : ', tipo_doc_est, ' - ', num_doc_est)
    print(' Fecha Nac. / Nac.    : ', fecha_nac_est, ' / ', nacionalidad_est)
    print(' Sexo                 : ', sexo_est)
    print(' Grado y Nivel        : ', grado_nivel_est)
    print(' Col. Procedencia     : ', colegio_proc_est)
    print('------------------------------------------------------------------')
    print(' 2. DATOS DEL PADRE, MADRE O APODERADO:')
    print(' Responsable          : ', nombre_resp, ' (', parentesco_resp, ')')
    print(' Documento            : ', tipo_doc_resp, ' - ', num_doc_resp)
    print(' Contacto             : ', telefono_resp, ' | ', correo_resp)
    print(' Dirección / Ubicación: ', direccion_resp, ' - ', distrito_resp)
    print('==================================================================')
    print('¡Ficha registrada y procesada con éxito!')
else:
    print('[ERROR]: Matrícula rechazada. Falta presentar los documentos físicos.')

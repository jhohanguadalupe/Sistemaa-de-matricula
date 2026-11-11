import os
from datetime import datetime
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAPACIDAD_TOTAL = 5
ARCHIVO_BD = os.path.join(BASE_DIR, "estudiantes.txt")
ARCHIVO_EXCEL = os.path.join(BASE_DIR, "estudiantes_matricula.xlsx")

# -------------------------------------------------------------
# Utilidades de Entrada y Validación
# -------------------------------------------------------------

def pedir_opcion(mensaje, opciones_validas):
    while True:
        print(mensaje)
        opcion = input().strip()
        if opcion in opciones_validas:
            return opcion
        print("[ERROR]: Entrada inválida. Elija una de las opciones mostradas.")


def pedir_opcion_con_salida(mensaje, opciones_validas):
    while True:
        print(mensaje)
        opcion = input().strip()
        if opcion == "0":
            return None
        if opcion in opciones_validas:
            return opcion
        print("[ERROR]: Entrada inválida. Elija una de las opciones mostradas.")


def pedir_texto_no_vacio(mensaje, error):
    while True:
        print(mensaje)
        texto = input().strip()
        if texto == "0":
            return None
        if texto:
            return texto
        print(error)


def pedir_numero(mensaje, nombre, min_len, max_len):
    while True:
        print(mensaje)
        num = input().strip()
        if num == "0":
            return None
        if not num.isdigit():
            print(f"[ERROR]: {nombre} debe contener únicamente números.")
        elif not (min_len <= len(num) <= max_len):
            if min_len == max_len:
                print(f"[ERROR]: {nombre} debe tener exactamente {min_len} dígitos. (Ingresaste: {len(num)})")
            else:
                print(f"[ERROR]: {nombre} debe tener entre {min_len} y {max_len} dígitos. (Ingresaste: {len(num)})")
        else:
            return num


def validar_fecha(fecha_str):
    try:
        f = datetime.strptime(fecha_str, "%d/%m/%Y")
        return 1900 <= f.year <= 2026
    except ValueError:
        return False


def ocultar_documento(num_doc):
    num_str = str(num_doc)
    return ("*" * (len(num_str) - 4) + num_str[-4:]) if len(num_str) > 4 else num_str


def calcular_vacantes(estudiantes):
    ocupadas = sum(1 for e in estudiantes if len(e) > 17 and e[17] == "ACTIVO")
    return max(0, CAPACIDAD_TOTAL - ocupadas)


# -------------------------------------------------------------
# Gestión de Archivos y Excel
# -------------------------------------------------------------

def exportar_excel(estudiantes):
    wb = openpyxl.Workbook()
    ws = wb.active
    if ws is None:
        ws = wb.create_sheet("Matrículas")
    assert ws is not None
    ws.title = "Matrículas"

    # Título principal
    ws.merge_cells("A1:S1")
    t = ws["A1"]
    t.value = "SISTEMA DE MATRÍCULA ESCOLAR - REGISTRO GENERAL"
    t.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    t.fill = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
    t.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 36

    # Resumen de estados
    activos = sum(1 for e in estudiantes if len(e) > 17 and e[17] == "ACTIVO")
    traslados = sum(1 for e in estudiantes if len(e) > 17 and e[17] == "TRASLADADO")
    retiros = sum(1 for e in estudiantes if len(e) > 17 and e[17] == "RETIRADO")

    ws.merge_cells("A2:S2")
    sub = ws["A2"]
    sub.value = f"Total registrados: {len(estudiantes)}  |  Activos: {activos}  |  Trasladados: {traslados}  |  Retirados: {retiros}"
    sub.font = Font(name="Calibri", size=10, italic=True, color="1F4E79")
    sub.fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    sub.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[2].height = 22

    encabezados = [
        "N°", "Apellidos Estudiante", "Nombres Estudiante", "Tipo Doc.",
        "N° Documento", "F. Nacimiento", "Nacionalidad", "Sexo",
        "Grado / Nivel", "Colegio Procedencia", "Apellidos Responsable",
        "Nombres Responsable", "Parentesco", "Teléfono Contacto",
        "Correo Electrónico", "Dirección", "Distrito / Provincia", "Estado",
        "Fecha de Inscripción"
    ]

    fill_cabecera = PatternFill(start_color="2F5597", end_color="2F5597", fill_type="solid")
    font_cabecera = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    borde_cabecera = Border(
        left=Side(style="thin", color="FFFFFF"),
        right=Side(style="thin", color="FFFFFF"),
        top=Side(style="medium", color="1F4E79"),
        bottom=Side(style="medium", color="1F4E79")
    )

    ws.row_dimensions[3].height = 28
    for col_idx, enc in enumerate(encabezados, start=1):
        c = ws.cell(row=3, column=col_idx, value=enc)
        c.font = font_cabecera
        c.fill = fill_cabecera
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = borde_cabecera

    fill_par = PatternFill(start_color="F2F5F9", end_color="F2F5F9", fill_type="solid")
    fill_impar = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
    font_datos = Font(name="Calibri", size=10)
    borde_datos = Border(
        left=Side(style="thin", color="D9D9D9"),
        right=Side(style="thin", color="D9D9D9"),
        top=Side(style="thin", color="D9D9D9"),
        bottom=Side(style="thin", color="D9D9D9")
    )

    estilos_estado = {
        "ACTIVO": (PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid"), Font(name="Calibri", size=10, bold=True, color="375623")),
        "TRASLADADO": (PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid"), Font(name="Calibri", size=10, bold=True, color="7F6000")),
        "RETIRADO": (PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid"), Font(name="Calibri", size=10, bold=True, color="C65911"))
    }
    cols_centradas = {1, 4, 5, 6, 7, 8, 9, 13, 14, 18, 19}

    for row_idx, e in enumerate(estudiantes, start=4):
        ws.row_dimensions[row_idx].height = 22
        fill_fila = fill_par if (row_idx % 2 == 0) else fill_impar
        for col_idx, val in enumerate(e, start=1):
            c = ws.cell(row=row_idx, column=col_idx, value=str(val))
            c.border = borde_datos
            if col_idx == 18 and str(val) in estilos_estado:
                c.fill, c.font = estilos_estado[str(val)]
                c.alignment = Alignment(horizontal="center", vertical="center")
            else:
                c.fill = fill_fila
                c.font = font_datos
                c.alignment = Alignment(horizontal="center" if col_idx in cols_centradas else "left", vertical="center")

    for col in ws.columns:
        col_letter = get_column_letter(int(col[0].column or 1))
        max_len = max((len(str(cell.value or "")) for cell in col[2:]), default=0)
        ws.column_dimensions[col_letter].width = max(max_len + 4, 12)

    ws.freeze_panes = "A4"
    try:
        wb.save(ARCHIVO_EXCEL)
    except PermissionError:
        print("\n[AVISO]: No se pudo actualizar el Excel porque el archivo está abierto en otro programa.")


def guardar_estudiantes(estudiantes):
    with open(ARCHIVO_BD, "w", encoding="utf-8") as f:
        for e in estudiantes:
            f.write("|".join(str(campo) for campo in e) + "\n")
    exportar_excel(estudiantes)


def cargar_estudiantes():
    estudiantes = []
    try:
        with open(ARCHIVO_BD, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split("|")
                num_corr = int(partes[0]) if partes[0].isdigit() else len(estudiantes) + 1
                registro = [num_corr] + partes[1:]
                # Compatibilidad de versiones
                if len(registro) == 17:
                    registro.extend(["ACTIVO", datetime.now().strftime("%d/%m/%Y %H:%M")])
                elif len(registro) == 18:
                    registro.append(datetime.now().strftime("%d/%m/%Y %H:%M"))
                estudiantes.append(registro)
    except FileNotFoundError:
        pass
    return estudiantes


# -------------------------------------------------------------
# Impresión de Reportes
# -------------------------------------------------------------

def imprimir_ficha(e, vacantes=None):
    f_ins = e[18] if len(e) > 18 else "No registrada"
    estado = e[17] if len(e) > 17 else "ACTIVO"
    print("------------------------------------------------------")
    print(f" F. Inscrip.:  {f_ins}")
    print(f" Alumno:       {e[1]}, {e[2]}")
    print(f" Documento:    {e[3]} - {e[4]}")
    print(f" F. Nac:       {e[5]} | Sexo: {e[7]}")
    print(f" Nacionalidad: {e[6]}")
    print(f" Grado/Nivel:  {e[8]}")
    print(f" Procedencia:  {e[9]}")
    print(f" Responsable:  {e[10]}, {e[11]} ({e[12]})")
    print(f" Teléfono:     {e[13]}")
    print(f" Correo:       {e[14]}")
    print(f" Dirección:    {e[15]} - {e[16]}")
    print(f" Estado:       [{estado}]")
    if vacantes is not None:
        print(f" Vacantes escolares restantes: {vacantes}")
    print("------------------------------------------------------")


# -------------------------------------------------------------
# Matrícula de Alumno
# -------------------------------------------------------------

def matricular_alumno(estudiantes, vacantes_disponibles):
    num_est = len(estudiantes) + 1
    print("\n========================================")
    print("      REGISTRO DE NUEVO ESTUDIANTE")
    print(f"      Estudiante N.° {num_est}")
    print("   (Escriba 0 para volver al menú)")
    print("========================================\n")

    if vacantes_disponibles <= 0:
        print("[AVISO]: No hay vacantes disponibles.")
        input("\nPresione ENTER para volver...")
        return vacantes_disponibles

    print("--- 1. DATOS DEL ESTUDIANTE ---")
    nombres_est = pedir_texto_no_vacio("Nombres completos del estudiante:", "[ERROR]: El nombre no puede estar vacío.")
    if nombres_est is None:
        return vacantes_disponibles

    apellidos_est = pedir_texto_no_vacio("Apellidos completos del estudiante:", "[ERROR]: El apellido no puede estar vacío.")
    if apellidos_est is None:
        return vacantes_disponibles

    print("\nTipo de documento del estudiante:\n  1. DNI\n  2. Pasaporte")
    opc_doc = pedir_opcion_con_salida("Elija una opción (1 o 2) [0 = volver]:", ["1", "2"])
    if opc_doc is None:
        return vacantes_disponibles
    tipo_doc_est = "DNI" if opc_doc == "1" else "Pasaporte"

    num_doc_est = pedir_numero(f"\nNúmero de documento ({tipo_doc_est}):", tipo_doc_est, 8 if tipo_doc_est == "DNI" else 9, 8 if tipo_doc_est == "DNI" else 9)
    if num_doc_est is None:
        return vacantes_disponibles

    while any(e[4] == num_doc_est and e[3] == tipo_doc_est for e in estudiantes):
        print("[ERROR]: Este documento ya está registrado en el sistema.")
        num_doc_est = pedir_numero(f"Ingrese otro número ({tipo_doc_est}) [0 = volver]:", tipo_doc_est, 8 if tipo_doc_est == "DNI" else 9, 8 if tipo_doc_est == "DNI" else 9)
        if num_doc_est is None:
            return vacantes_disponibles

    while True:
        print("\nFecha de nacimiento (DD/MM/AAAA) [0 = volver]:")
        fecha_nac = input().strip()
        if fecha_nac == "0":
            return vacantes_disponibles
        if validar_fecha(fecha_nac):
            break
        print("[ERROR]: Fecha inválida. Debe ser una fecha real en formato DD/MM/AAAA.")

    nacionalidad = pedir_texto_no_vacio("\nNacionalidad:", "[ERROR]: Ingrese una nacionalidad válida.")
    if nacionalidad is None:
        return vacantes_disponibles

    print("\nSexo del estudiante:\n  1. Masculino (M)\n  2. Femenino (F)")
    opc_sexo = pedir_opcion_con_salida("Elija una opción (1 o 2) [0 = volver]:", ["1", "2"])
    if opc_sexo is None:
        return vacantes_disponibles
    sexo = "M" if opc_sexo == "1" else "F"

    grado = pedir_texto_no_vacio("\nGrado y nivel al que postula (ej: 1ro Primaria):", "[ERROR]: El grado no puede estar vacío.")
    if grado is None:
        return vacantes_disponibles

    print("\nColegio de procedencia (ENTER si no aplica) [0 = volver]:")
    col_proc = input().strip()
    if col_proc == "0":
        return vacantes_disponibles
    col_proc = col_proc if col_proc else "No aplica"

    print("\n--- 2. DATOS DEL RESPONSABLE ---")
    print("Parentesco:\n  1. Madre\n  2. Padre\n  3. Apoderado / Tutor Legal")
    opc_par = pedir_opcion_con_salida("Elija una opción (1, 2 o 3) [0 = volver]:", ["1", "2", "3"])
    if opc_par is None:
        return vacantes_disponibles
    parentesco = "Madre" if opc_par == "1" else ("Padre" if opc_par == "2" else "Apoderado")

    nombres_resp = pedir_texto_no_vacio(f"\nNombres del responsable ({parentesco}):", "[ERROR]: Ingrese los nombres.")
    if nombres_resp is None:
        return vacantes_disponibles

    apellidos_resp = pedir_texto_no_vacio(f"Apellidos del responsable ({parentesco}):", "[ERROR]: Ingrese los apellidos.")
    if apellidos_resp is None:
        return vacantes_disponibles

    print("\nTipo de documento del responsable:\n  1. DNI\n  2. CE / Pasaporte")
    opc_doc_r = pedir_opcion_con_salida("Elija una opción (1 o 2) [0 = volver]:", ["1", "2"])
    if opc_doc_r is None:
        return vacantes_disponibles
    tipo_doc_resp = "DNI" if opc_doc_r == "1" else "CE/Pasaporte"

    num_doc_resp = pedir_numero(f"\nNúmero de documento ({tipo_doc_resp}):", tipo_doc_resp, 8, 8 if tipo_doc_resp == "DNI" else 12)
    if num_doc_resp is None:
        return vacantes_disponibles

    telefono_resp = pedir_numero("\nTeléfono o celular de contacto (9 dígitos):", "El teléfono", 9, 9)
    if telefono_resp is None:
        return vacantes_disponibles

    while True:
        print("\nCorreo electrónico de contacto [0 = volver]:")
        correo_resp = input().strip()
        if correo_resp == "0":
            return vacantes_disponibles
        if "@" in correo_resp:
            break
        print("[ERROR]: Correo inválido. Debe contener '@'.")

    print("\nDirección domiciliaria [0 = volver]:")
    direccion_resp = input().strip()
    if direccion_resp == "0":
        return vacantes_disponibles

    print("Distrito / Provincia [0 = volver]:")
    distrito_resp = input().strip()
    if distrito_resp == "0":
        return vacantes_disponibles

    print("\n¿Cuenta con todos los documentos físicos requeridos?\n  1. Sí, expediente completo\n  2. No, faltan documentos")
    docs_ok = pedir_opcion_con_salida("Elija una opción (1 o 2) [0 = volver]:", ["1", "2"])
    if docs_ok is None:
        return vacantes_disponibles

    if docs_ok == "1":
        fecha_registro = datetime.now().strftime("%d/%m/%Y %H:%M")
        nuevo = [
            num_est, apellidos_est, nombres_est, tipo_doc_est, num_doc_est,
            fecha_nac, nacionalidad, sexo, grado, col_proc, apellidos_resp,
            nombres_resp, parentesco, telefono_resp, correo_resp, direccion_resp,
            distrito_resp, "ACTIVO", fecha_registro
        ]
        estudiantes.append(nuevo)
        guardar_estudiantes(estudiantes)
        vacantes_disponibles = calcular_vacantes(estudiantes)

        print("\n======================================================")
        print("          FICHA OFICIAL DE MATRÍCULA                  ")
        print(" ESTADO DE MATRÍCULA: [ EXITOSA ]")
        imprimir_ficha(nuevo, vacantes_disponibles)
        print("[OK] Alumno registrado y datos sincronizados en Excel y texto.")
    else:
        print("\n======================================================")
        print(" ESTADO DE MATRÍCULA: [ RECHAZADA / OBSERVADA ]")
        print(" [MOTIVO]: El expediente físico está incompleto.")
        print("======================================================")

    if vacantes_disponibles > 0:
        print("\n¿Desea registrar a otro estudiante ahora?\n  1. Sí, registrar a otro\n  2. Volver al menú principal")
        if pedir_opcion("Elija una opción (1 o 2):", ["1", "2"]) == "1":
            return matricular_alumno(estudiantes, vacantes_disponibles)
    else:
        print("\n[AVISO]: Se han completado todas las vacantes.")
        input("Presione ENTER para volver...")

    return vacantes_disponibles


# -------------------------------------------------------------
# Visualización y Gestión de Alumnos
# -------------------------------------------------------------

def ver_alumnos(estudiantes, vacantes_disponibles):
    while True:
        print("\n========================================")
        print("           ALUMNOS INSCRITOS")
        print("========================================")

        if not estudiantes:
            print("\nNo hay alumnos inscritos todavía.")
            input("\nPresione ENTER para volver al menú...")
            return vacantes_disponibles

        ordenados = sorted(estudiantes, key=lambda x: str(x[1]).lower())
        print(f"\nTotal inscritos: {len(ordenados)}\n")
        for idx, e in enumerate(ordenados, start=1):
            doc = ocultar_documento(e[4])
            est = e[17] if len(e) > 17 else "ACTIVO"
            print(f"  [{idx}] {e[1]}, {e[2]} | {e[3]}: {doc} | {e[8]} | [{est}]")

        print("\n------------------------------------------------------")
        print("Acciones:\n  1. Gestionar estudiante (Estado / Eliminar)\n  2. Volver al menú")
        print("------------------------------------------------------")
        if pedir_opcion("Elija una opción (1 o 2):", ["1", "2"]) == "2":
            return vacantes_disponibles

        opciones_idx = [str(i) for i in range(1, len(ordenados) + 1)] + ["0"]
        print("\nIngrese el número [N.°] del alumno a gestionar (o 0 para cancelar):")
        sel = pedir_opcion("Selección:", opciones_idx)
        if sel == "0":
            continue

        alumno = ordenados[int(sel) - 1]
        estado_actual = alumno[17] if len(alumno) > 17 else "ACTIVO"

        print("\n------------------------------------------------------")
        print(f" Alumno:        {alumno[1]}, {alumno[2]}")
        print(f" Documento:     {alumno[3]} - {alumno[4]}")
        print(f" Estado actual: [{estado_actual}]")
        print("------------------------------------------------------")
        print("Opciones de estado:")
        print("  1. Marcar como TRASLADADO (libera 1 vacante)")
        print("  2. Marcar como RETIRADO   (libera 1 vacante)")
        print("  3. Eliminar definitivamente (renumera lista)")
        print("  4. Reactivar a ACTIVO")
        print("  5. Cancelar")
        print("------------------------------------------------------")

        sub = pedir_opcion("Elija una opción (1-5):", ["1", "2", "3", "4", "5"])

        if sub in ("1", "2"):
            nuevo_est = "TRASLADADO" if sub == "1" else "RETIRADO"
            if estado_actual == nuevo_est:
                print(f"\n[AVISO]: El alumno ya se encuentra como {nuevo_est}.")
            else:
                alumno[17] = nuevo_est
                guardar_estudiantes(estudiantes)
                vacantes_disponibles = calcular_vacantes(estudiantes)
                print(f"\n[OK] Estado actualizado a {nuevo_est}. Vacantes disponibles: {vacantes_disponibles}")
            input("Presione ENTER para continuar...")

        elif sub == "3":
            print("\n¿Seguro que desea ELIMINAR al estudiante definitivamente?\n  1. Sí, eliminar y renumerar\n  2. No, cancelar")
            if pedir_opcion("Elija opción (1 o 2):", ["1", "2"]) == "1":
                estudiantes.remove(alumno)
                for i, e in enumerate(estudiantes, start=1):
                    e[0] = i
                guardar_estudiantes(estudiantes)
                vacantes_disponibles = calcular_vacantes(estudiantes)
                print(f"\n[OK] Alumno eliminado. Lista renumerada. Vacantes libres: {vacantes_disponibles}")
            else:
                print("\n[CANCELADO]: No se eliminó al estudiante.")
            input("Presione ENTER para continuar...")

        elif sub == "4":
            if estado_actual == "ACTIVO":
                print("\n[AVISO]: El estudiante ya está ACTIVO.")
            elif calcular_vacantes(estudiantes) <= 0:
                print("\n[ERROR]: No hay vacantes disponibles para reactivar la matrícula.")
            else:
                alumno[17] = "ACTIVO"
                guardar_estudiantes(estudiantes)
                vacantes_disponibles = calcular_vacantes(estudiantes)
                print(f"\n[OK] Matrícula reactivada. Vacantes restantes: {vacantes_disponibles}")
            input("Presione ENTER para continuar...")


# -------------------------------------------------------------
# Búsquedas
# -------------------------------------------------------------

def buscar_por_dni(estudiantes):
    print("\n========================================")
    print("        BUSCAR ALUMNO POR DNI")
    print("   (Escriba 0 para volver al menú)")
    print("========================================")
    print("\nIngrese el DNI a buscar:")
    dni = input().strip()
    if dni == "0":
        return

    encontrados = [e for e in estudiantes if str(e[4]).strip() == dni]
    if not encontrados:
        print(f"\nNo se encontró ningún estudiante con el documento: {dni}")
    else:
        for e in encontrados:
            imprimir_ficha(e)
    input("\nPresione ENTER para volver...")


def buscar_por_apellidos(estudiantes):
    print("\n========================================")
    print("     BUSCAR ALUMNO POR APELLIDOS")
    print("   (Escriba 0 para volver al menú)")
    print("========================================")
    print("\nIngrese el apellido (o parte del mismo):")
    apell = input().strip()
    if apell == "0":
        return

    encontrados = [e for e in estudiantes if apell.lower() in str(e[1]).lower()]
    if not encontrados:
        print(f"\nNo se encontraron coincidencias para: \"{apell}\"")
    else:
        print(f"\nSe encontraron {len(encontrados)} coincidencia(s):\n")
        for e in encontrados:
            imprimir_ficha(e)
    input("\nPresione ENTER para volver...")

# -------------------------------------------------------------
# Acceso y Menú Principal
# -------------------------------------------------------------

def login():
    import msvcrt
    import sys

    def pedir_oculto(prompt):
        print(prompt, end="", flush=True)
        resultado = ""
        while True:
            ch = msvcrt.getch()
            # Si presiona Enter, termina de leer
            if ch in (b"\r", b"\n"):
                print()
                break
            # Si presiona Backspace (Retroceso), borra el último carácter
            elif ch == b"\x08":
                if len(resultado) > 0:
                    resultado = resultado[:-1]
                    # Borra visualmente el asterisco de la consola
                    sys.stdout.write("\b \b")
                    sys.stdout.flush()
            # Si es un carácter válido, lo guarda y muestra un asterisco
            elif len(ch) == 1 and ord(ch) >= 32:
                resultado += ch.decode("utf-8", errors="ignore")
                print("*", end="", flush=True)
        return resultado

    print("========================================")
    print("     SISTEMA DE MATRÍCULA ESCOLAR")
    print("           Acceso al Sistema")
    print("========================================")
    while True:
        # El usuario y la contraseña se ocultan con asteriscos automáticamente
        usuario = input("\nUsuario: ").strip()
        clave = pedir_oculto("Contraseña: ").strip()
        if usuario == "grupo_dinamita_uwu" and clave == "fundamentos2026":
            print("\n[OK] Acceso autorizado. Bienvenido al sistema.")
            break
        print("[ERROR]: Credenciales incorrectas. Intente nuevamente.")

def main():
    login()
    estudiantes = cargar_estudiantes()
    vacantes = calcular_vacantes(estudiantes)

    if estudiantes:
        print(f"\nSe cargaron {len(estudiantes)} alumno(s) desde el registro.")
        guardar_estudiantes(estudiantes)
    else:
        print("\nNo se encontraron registros previos. Base de datos vacía.")

    while True:
        print("\n══════════════════════════════════════")
        print("     SISTEMA DE MATRÍCULA ESCOLAR")
        print("            MENÚ PRINCIPAL")
        print("══════════════════════════════════════")
        print(f"  1. Matricular alumno nuevo  (Vacantes: {vacantes})")
        print("  2. Ver alumnos inscritos (Gestión de estados)")
        print("  3. Buscar por DNI")
        print("  4. Buscar por apellidos")
        print("  5. Generar casos Prueba")
        print("  6. Salir")
        print("══════════════════════════════════════")

        opc = pedir_opcion("Elija una opción (1-6):", ["1", "2", "3", "4", "5", "6"])
        match opc:
            case "1":
                vacantes = matricular_alumno(estudiantes, vacantes)
            case "2":
                vacantes = ver_alumnos(estudiantes, vacantes)
            case "3":
                buscar_por_dni(estudiantes)
            case "4":
                buscar_por_apellidos(estudiantes)

            case "5":
                estudiantes = [
                    [
                        1, "Malca Moreno", "Patrick Josspeh", "DNI", "12345678",
                        "15/03/2009", "Peruana", "M", "1ro Primaria",
                        "I.E. San José", "Malca Moreno", "Papa 1", "Padre",
                        "987654321", "papa@gmail.com", "Av. Perú 123",
                        "Trujillo", "ACTIVO", datetime.now().strftime("%d/%m/%Y %H:%M")
                    ],
                    [
                        2, "Guadalupe Cusquipoma", "Jhohan Antoni", "DNI", "23456789",
                        "20/06/2000", "Peruana", "M", "2do Primaria",
                        "I.E. Libertad", "Guadalupe", "Papa 2", "Padre",
                        "912345678", "papa2@gmail.com", "Jr. Lima 456",
                        "Trujillo", "ACTIVO", datetime.now().strftime("%d/%m/%Y %H:%M")
                    ],
                    [
                        3, "Méndez Florian", "Anderson Elisban", "DNI", "34567890",
                        "10/08/2014", "Peruana", "M", "3ro Primaria",
                        "No aplica", "Méndez", "Papa 3", "Padre",
                        "923456789", "papa3@gmail.com", "Calle Sol 789",
                        "Trujillo", "ACTIVO", datetime.now().strftime("%d/%m/%Y %H:%M")
                    ],
                    [
                        4, "Ponce Guitierrez", "Darwin Yefry", "DNI", "45678901",
                        "05/11/2013", "Peruana", "M", "1ro Primaria",
                        "I.E. Miguel Grau", "Ponce", "Papa 4", "Padre",
                        "934567891", "papa4@gmail.com", "Av. América 321",
                        "Trujillo", "ACTIVO", datetime.now().strftime("%d/%m/%Y %H:%M")
                    ],
                    [
                        5, "Quezada Ruíz", "Anderson Miguel", "DNI", "56789012",
                        "22/01/2012", "Peruana", "M", "2do Primaria",
                        "No aplica", "Quezada", "Papa 5", "Padre",
                        "945678912", "padre5@gmail.com", "Jr. Unión 654",
                        "Trujillo", "ACTIVO", datetime.now().strftime("%d/%m/%Y %H:%M")
                    ]
                ]

                guardar_estudiantes(estudiantes)
                vacantes = calcular_vacantes(estudiantes)

                print("\n[OK] Se generaron 5 casos de prueba.")
                print(f"Total de datos por estudiante: {len(estudiantes[0])}")
                print(f"Vacantes disponibles: {vacantes}")
                input("\nPresione ENTER para continuar...")
            case "6":
                print("\nGracias por usar el sistema. Vuelva pronto :D Bebe uwu onichan")
                break


if __name__ == "__main__":
    main()

# Actividad 1.2 – Creación de Repositorio en GitHub (Trabajo en Equipo)

**Integrantes:**

- Apodaca Ramírez José Daniel - 23030500
- Kumagai Mendoza Yosichi - 23030674
- Vargas Medina Josué - 23030151

# Proyecto: Sistema de Reservaciones de Consultorio Médico

Descripción del proyecto: Se desarrollará una API para gestionar las citas en un consultorio médico. Las funcionalidades principales incluyen:

- Operaciones CRUD para pacientes (nombre, edad, datos de contacto, historial médico básico).
- Operaciones CRUD para doctores (especialidad, horario).
- Sistema de reservaciones: un paciente puede agendar una cita con un doctor en un horario específico.
- Validación de conflictos de horario.
- Consulta de citas pasadas y futuras.
- Implementación en SQLite3 con relaciones.

# Instalación de entorno virtual

Microsoft Windows [Versión 10.0.19045.5247]  
(c) Microsoft Corporation. Todos los derechos reservados.

```bash
C:\Users\01>cd Desktop
C:\Users\01\Desktop>cd Proyectos
C:\Users\01\Desktop\Proyectos>cd equipo2-consultorio
C:\Users\01\Desktop\Proyectos\equipo2-consultorio>cd equipo2-consultorio-main
C:\Users\01\Desktop\Proyectos\equipo2-consultorio\equipo2-consultorio-main>python -m venv .venv
C:\Users\01\Desktop\Proyectos\equipo2-consultorio\equipo2-consultorio-main>.venv\Scripts\activate
(.venv)> pip install flask
(.venv)> pip freeze > requirements.txt
(.venv)> python app.py
```

# Diagrama de clases Mermaid

classDiagram
class Paciente {
+String nombre
+int edad
+String contacto
}

    class Doctor {
        +String nombre
        +String especialidad
        +List horarios_disponibles
    }

    class Consultorio {
        +String nombre
        +String direccion
        +List doctores
    }

    class Cita {
        +Date fecha
        +Time hora
        +Paciente paciente
        +Doctor doctor
        +Consultorio consultorio
        +String motivo
    }

    Paciente --> Cita
    Doctor --> Cita
    Consultorio --> Cita
    Consultorio --> Doctor

pipeline {
    agent any

    environment {
        DESTINATARIO = credentials('correo-clinica')  // credencial configurada en Jenkins
    }

    stages {

        stage('Provisionar infraestructura') {
            steps {
                bat '''
                cd terraform
                terraform init
                terraform apply -auto-approve
                '''
            }
        }

        stage('Instalar dependencias') {
            steps {
                bat '"C:\\Users\\Nitro5\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Extraer y analizar datos desde API') {
            steps {
                bat '"C:\\Users\\Nitro5\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" main.py'
            }
        }

        stage('Enviar reporte por correo') {
            steps {
                script {
                    def resumen = readFile('datos/resumen.txt')
                    emailext(
                        subject: "Reporte de análisis clínico automatizado",
                        body: """Hola equipo clínico,
                        
Se completó el análisis de pacientes basado en datos extraídos de la API.
Adjunto se encuentra el reporte con los resultados.

${resumen}
                        
Saludos,
Sistema Jenkins - Clínica""",
                        to: "${DESTINATARIO}",
                        attachmentsPattern: "datos/reporte_pacientes.csv"
                    )
                }
            }
        }

        stage('Liberar infraestructura') {
            steps {
                bat '''
                cd terraform
                terraform destroy -auto-approve
                '''
            }
        }
    }
}

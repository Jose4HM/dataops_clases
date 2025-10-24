pipeline {
    agent any
    environment {
        DESTINATARIO = credentials('correo-clinica')  // credencial configurada en Jenkins
    }

    stages {
        stage('Provisionar infraestructura') {
            steps {
                sh '''
                cd terraform/
                terraform init
                terraform apply -auto-approve
                '''
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Extraer y analizar datos desde API') {
            steps {
                sh 'python3 main.py'
            }
        }

        stage('Enviar reporte por correo') {
            steps {
                emailext(
                    subject: "Reporte de análisis clínico automatizado",
                    body: """Hola equipo clínico,
                    
Se completó el análisis de pacientes basado en datos extraídos de la API.
Adjunto se encuentra el reporte con los resultados.

${readFile('datos/resumen.txt')}
                    
Saludos,
Sistema Jenkins - Clínica""",
                    to: "$DESTINATARIO",
                    attachmentsPattern: "datos/reporte_pacientes.csv"
                )
            }
        }

        stage('Provisionar infraestructura') {
    steps {
        sh '''
        cd terraform/
        terraform init
        terraform apply -auto-approve
        '''
    }
}

stage('Liberar infraestructura') {
    steps {
        sh '''
        cd terraform/
        terraform destroy -auto-approve
        '''
    }
}

    }
}

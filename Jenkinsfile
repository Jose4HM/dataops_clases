pipeline {
    agent any

    stages {

        stage('Preparar entorno') {
            steps {
                echo "Creando entorno virtual e instalando dependencias..."
                bat '"C:\\Users\\Nitro\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m venv venv'
                bat 'venv\\Scripts\\activate && pip install --upgrade pip && pip install -r requirements.txt'
            }
}

        stage('Ejecutar script') {
            steps {
                echo "Ejecutando script principal..."
                bat 'venv\\Scripts\\activate && python src\\main.py'
            }
        }
    }

    post {
        success {
            echo '✅ Análisis de pacientes completado exitosamente.'
        }
        failure {
            echo '❌ Error en la ejecución del análisis.'
        }
    }
}


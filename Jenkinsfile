pipeline {
    agent any

    stages {
        sstage('Clonar repositorio') {
    steps {
        deleteDir()
        git branch: 'main',
            url: 'https://github.com/Jose4HM/dataops_clases.git'
    }
}

        stage('Instalar dependencias') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Ejecutar análisis de pacientes') {
            steps {
                sh 'python3 main.py'
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

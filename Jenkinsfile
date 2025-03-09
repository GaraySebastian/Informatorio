pipeline {
    agent any

    environment {
        IMAGE_NAME = "django_app"
        CONTAINER_NAME = "django_app"
        REPO_URL = "https://github.com/GaraySebastian/Informatorio.git"
    }

    stages {
        stage('Clonar Repositorio') {
            steps {
                git branch: 'master', credentialsId: 'github-credentials', url: "${REPO_URL}"
            }
        }

        stage('Construir Imagen Docker') {
            steps {
                script {
                    sh 'docker-compose build'
                }
            }
        }

        stage('Verificar Contenedores Activos') {
            steps {
                script {
                    def containersRunning = sh(script: "docker ps -q --filter 'name=postgres_db' --filter 'name=django_app'", returnStdout: true).trim()
                    if (containersRunning) {
                        echo "Los contenedores ya están corriendo. No se levantarán nuevamente."
                    } else {
                        echo "Los contenedores no están corriendo. Se levantarán ahora."
                        sh 'docker-compose up -d'
                    }
                }
            }
        }

        stage('Ejecutar Tests') {
            steps {
                script {
                    sh 'docker-compose run --rm web python manage.py test'
                }
            }
        }
    }
}

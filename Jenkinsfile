pipeline {
    agent any

    environment {
        IMAGE_NAME = "django_app"
        CONTAINER_NAME = "django_app"
        DB_CONTAINER_NAME = "postgres_db"
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
                    // Construir la imagen de Docker directamente
                    sh 'docker build -t ${IMAGE_NAME}:${BUILD_TAG} .'
                }
            }
        }

        stage('Ejecutar Tests') {
            steps {
                script {
                    def containersRunning = sh(script: "docker ps -q --filter 'name=${CONTAINER_NAME}'", returnStdout: true).trim()
                    if (containersRunning) {
                        sh "docker exec ${CONTAINER_NAME} python manage.py test"
                    } else {
                        sh 'docker run --rm ${IMAGE_NAME}:${BUILD_TAG} python manage.py test'
                    }
                }
            }
        }
    }
}
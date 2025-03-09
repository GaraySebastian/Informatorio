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

        stage('Levantar Servicios') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Ejecutar Tests') {
            steps {
                script {
                    sh 'docker-compose run --rm django_app python manage.py test'
                }
            }
        }
    }
}

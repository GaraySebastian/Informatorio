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
                    sh 'docker compose build'
                }
            }
        }

        stage('Levantar Contenedores') {
            steps {
                script {
                    sh 'docker compose up -d'
                }
            }
        }

        stage('Verificar Contenedor') {
            steps {
                script {
                    sh 'docker ps | grep django_app'
                }
            }
        }
    }

    post {
        always {
            script {
                sh 'docker compose logs > logs.txt'
            }
        }
        failure {
            mail to: 'seba.c.garay@gmail.com', subject: 'Fallo en Jenkins', body: 'El despliegue falló. Verifica Jenkins.'
        }
    }
}
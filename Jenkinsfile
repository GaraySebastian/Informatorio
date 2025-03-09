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

        stage('Eliminar Contenedor Django') {
            steps {
                script {
                    sh 'docker rm -f django_app || true'
                }
            }
        }

        stage('Eliminar Contenedores Existentes') {
            steps {
                script {
                    sh 'docker rm -f postgres_db || true'
                }
            }
        }

        stage('Limpiar contenedores y redes') {
            steps {
                script {
                    sh 'docker system prune -f || true'
                }
            }
        }

        stage('Construir Imagen Docker') {
            steps {
                script {
                    sh 'docker-compose build'
                }
            }
        }

        stage('Levantar Contenedores') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Esperar PostgreSQL') {
            steps {
                script {
                    sh 'until docker exec postgres_db pg_isready -U postgres; do sleep 5; done'
                }
            }
        }

        stage('Verificar Contenedor') {
            steps {
                script {
                    sh 'docker ps -a | grep django_app'
                }
            }
        }

        stage('Verificar Logs del Contenedor') {
            steps {
                script {
                    sh 'docker logs django_app || true'
                }
            }
        }

        stage('Ejecutar Tests') {
            steps {
                script {
                    sh 'docker exec django_app python manage.py test'
                }
            }
        }
    }

    post {
        always {
            script {
                sh 'docker-compose logs > logs.txt'
            }
        }
        failure {
            mail to: 'seba.c.garay@gmail.com', subject: 'Fallo en Jenkins', body: 'El despliegue falló. Verifica Jenkins.'
        }
    }
}
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

        // stage('Verificar Contenedores Activos') {
        //     steps {
        //         script {
        //             // Verificar si los contenedores ya están corriendo
        //             def containersRunning = sh(script: "docker ps -q --filter 'name=${DB_CONTAINER_NAME}' --filter 'name=${CONTAINER_NAME}'", returnStdout: true).trim()
        //             if (containersRunning) {
        //                 echo "Los contenedores ya están corriendo. No se levantarán nuevamente."
        //             } else {
        //                 echo "Los contenedores no están corriendo. Se levantarán ahora."
        //                 // Levantar el contenedor de la base de datos (PostgreSQL)
        //                 sh 'docker run --name ${DB_CONTAINER_NAME} -d -e POSTGRES_DB=${DB_NAME} -e POSTGRES_USER=${DB_USER} -e POSTGRES_PASSWORD=${DB_PASSWORD} -p 5432:5432 postgres:15'
        //                 // Levantar el contenedor de la aplicación Django
        //                 sh 'docker run --name ${CONTAINER_NAME} --link ${DB_CONTAINER_NAME}:db -d -p 8000:8000 ${IMAGE_NAME}:${BUILD_TAG}'
        //             }
        //         }
        //     }
        // }

        stage('Ejecutar Tests') {
            steps {
                script {
                    // Ejecutar los tests dentro del contenedor ya levantado
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

    post {
        always {
            script {
                // Limpiar los contenedores después de los tests
                sh 'docker rm -f ${CONTAINER_NAME} ${DB_CONTAINER_NAME}'
            }
        }
        failure {
            mail to: 'seba.c.garay@gmail.com', subject: 'Fallo en Jenkins', body: 'El despliegue falló. Verifica Jenkins.'
        }
    }
}
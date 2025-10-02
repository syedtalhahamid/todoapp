pipeline {
    agent any

    environment {
        IMAGE_NAME = "todoapp"
        CONTAINER_NAME = "todoapp-container"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/your-username/todoapp.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:latest .
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                    # Stop old container if running
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true

                    # Run new container
                    docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}:latest
                '''
            }
        }
    }

    post {
        success {
            echo "✅ TodoApp is running at http://localhost:5000"
        }
        failure {
            echo "❌ Build or run failed!"
        }
    }
}

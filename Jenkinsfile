pipeline {
    agent any

   
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/syedtalhahamid/todoapp.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '''
                    docker build -t todoapp:latest .
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                bat '''
                    # Stop old container if running
                    docker stop todoapp-container || true
                    docker rm todoapp-container || true

                    # Run new container
                    docker run -d --name todoapp-container -p 5000:5000 todoapp:latest
                '''
            }
        }
    }

    post {
        success {
            echo " TodoApp is running at http://localhost:5000"
        }
        failure {
            echo " Build or run failed!"
        }
    }
}

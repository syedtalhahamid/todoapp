pipeline {
    agent any

    environment {
        APP_DIR = "todoapp"
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull code from GitHub repo
                git branch: 'master',
                    url: 'https://github.com/syedtalhahamid/todoapp.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run App') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    export FLASK_APP=app.py
                    export FLASK_ENV=development
                    nohup flask run --host=0.0.0.0 --port=5000 > flask.log 2>&1 &
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}

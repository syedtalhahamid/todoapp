pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/syedtalhahamid/todoapp.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat """
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run App') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate
                    set FLASK_APP=app.py
                    set FLASK_ENV=development
                    start /B flask run --host=0.0.0.0 --port=5000
                """
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}

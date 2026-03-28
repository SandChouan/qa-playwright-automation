pipeline {
    agent {
        docker {
            image 'mcr.microsoft.com/playwright/python:v1.58.0-jammy'
            args '-u root'
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
    }
}

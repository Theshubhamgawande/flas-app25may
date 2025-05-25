pipeline {
    agent {
        docker {
            image 'docker:20.10.24' // Docker CLI in Alpine
            args '-v /var/run/docker.sock:/var/run/docker.sock' // mount host Docker socket
        }
    }

    environment {
        IMAGE_NAME = "shubhamdoc15/yourimagename"
    }

    stages {
        stage('Clone Repo') {
            steps {
                checkout scm
            }
        }

        stage('Check Docker Version') {
            steps {
                sh 'docker version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh """
                        echo "$PASS" | docker login -u "$USER" --password-stdin
                        docker push $IMAGE_NAME
                    """
                }
            }
        }
    }
}


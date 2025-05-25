pipeline {
    agent {
        docker {
            image 'docker:20.10.24-dind'  // Docker CLI + Daemon inside
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        IMAGE_NAME = "shubhamdoc15/yourimagename"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker version'
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh '''
                        echo "$PASS" | docker login -u "$USER" --password-stdin
                        docker push $IMAGE_NAME
                    '''
                }
            }
        }
    }
}



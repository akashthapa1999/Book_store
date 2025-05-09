pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'bookstore-app'
        DOCKER_TAG = "${BUILD_NUMBER}"
        AWS_CREDENTIALS = credentials('aws-credentials')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    docker run --rm ${DOCKER_IMAGE}:${DOCKER_TAG} pytest
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh '''
                        echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin
                        docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_USERNAME}/${DOCKER_IMAGE}:${DOCKER_TAG}
                        docker push ${DOCKER_USERNAME}/${DOCKER_IMAGE}:${DOCKER_TAG}
                    '''
                }
            }
        }

        stage('Deploy to AWS') {
            steps {
                withAWS(credentials: 'aws-credentials', region: 'us-east-1') {
                    dir('terraform') {
                        sh '''
                            terraform init
                            terraform apply -auto-approve
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            sh 'docker system prune -f'
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
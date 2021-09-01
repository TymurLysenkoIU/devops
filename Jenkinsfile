pipeline {
  agent any

  environment {
    image_name = 'sitiritis/devops_lab_1-2'
  }

  stages {
    stage('Test and lint') {
      agent {
        docker {
          image 'python:3.9.6'
        }
      }
      steps {
        sh 'cd app_python'
        sh 'pip install -r requirements.txt -r requirements.dev.txt'
        sh 'pylama'
        sh 'mypy'
        sh 'pytest'
      }
    }

    stage('Build image and deploy') {
      steps {
        script {
          dockerImage = docker.build(image_name, 'app_python')
          docker.withRegistry('', 'docker-hub') {
            dockerImage.push('$BUILD_NUMBER')
            dockerImage.push('latest')
          }
        }
      }
    }

    stage('Remove built docker image locally') {
      steps {
        sh 'docker rmi $image_name:$BUILD_NUMBER'
        sh 'docker rmi $image_name:latest'
      }
    }
  }
}
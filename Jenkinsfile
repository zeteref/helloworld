pipeline {
  agent any
  stages {
    stage('hello') {
      agent {
        docker {
          image 'alpine'
        }

      }
      steps {
        sh 'echo hello world'
      }
    }

  }
}
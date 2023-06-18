pipeline {
  agent any
  stages {
    stage('hello') {
      parallel {
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

        stage('error') {
          agent {
            docker {
              image 'alpine'
            }

          }
          steps {
            sh 'cat /etc/os-release'
          }
        }

      }
    }

    stage('error') {
      agent {
        docker {
          image 'alpine'
        }

      }
      steps {
        sh 'ls /dupa'
      }
    }

  }
}
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

        stage('') {
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

    stage('') {
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
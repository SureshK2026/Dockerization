pipeline{
    agent any
    environment{
        IMAGE_NAME='Pythonself:$git-commit'
    }
    Stages{
        stage('git-checkout'){
            steps{
            git url:'https://github.com/SureshK2026/Dockerization.git', branch:'main'
            }
        }
        stage('build-stage'){
            steps{
                sh '''
                printenv
                docker build -t $(IMAGE_NAME) .
                '''
            }
        }
        stage('Run-stage'){
            steps{
                sh '''
                docker run -it -d --name selfapp -p 5000:5000 $(IMAGE_NAME)
                '''
            }
        }
    }
}
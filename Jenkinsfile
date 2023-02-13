pipeline{

    agent any

    environment{
        DOCKERHUB_USERNAME = "sudeepgowda55"
        APP_NAME = "anonymous_ftp_access"
        IMAGE_NAME = "${DOCKERHUB_USERNAME}"+ "/" + "${APP_NAME}" 
    }

    stages{
        stage('cleanup Workspace'){
           steps {
                cleanWs()
           }
        }

        stage("git checkout"){
            steps{
                git branch: "master", url: 'https://github.com/SudeepGowda55/python_devops.git'
            //    for private repository 
            //    git credentialsId: "<id>", branch: "master", url: 'https://github.com/SudeepGowda55/python_devops.git'
            }
        }

        stage("Build Docker Images"){
            steps{
                script{
                    sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} -t ${IMAGE_NAME}:latest ."
                }
            }
        }

        stage("Push Docker Images to Docker Registery"){
            steps{
                script{
                    sh "docker push ${IMAGE_NAME}:${BUILD_NUMBER}"
                    sh "docker push ${IMAGE_NAME}:latest"
                }
            }
        }
    }

}

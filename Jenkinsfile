pipeline{

    agent any

    environment{
        DOCKERHUB_USERNAME = "sudeepgowda55"
        APP_NAME = "python_devops"
        IMAGE_TAGNAME = "${BUILD_NUMBER}"
        IMAGE_NAME = "${DOCKERHUB_USERNAME}"+ "/" + "${APP_NAME}" 
        DOCKERHUB_CRED = "dockerhub"
    }

    stages{
        stage('cleanup Workspace'){
           steps {
                cleanWs()
           }
        }
        stage("git checkout"){
            steps{
                git branch: "master" url: 'https://github.com/SudeepGowda55/python_devops.git'
            //    for private repository 
            //    git credentialsId: "<id>" branch: "master" url: 'https://github.com/SudeepGowda55/python_devops.git'
            }
        }
        stage("Build Docker Images"){
            steps{
                docker_image = docker.build "${IMAGE_NAME}"
            }
        }
    }
}
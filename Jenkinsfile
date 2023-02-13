pipeline{

    agent any

    environment{
        DOCKERHUB_USERNAME = "sudeepgowda55"
        APP_NAME = "anonymous_ftp_access"
        IMAGE_TAGNAME = "${BUILD_NUMBER}"
        IMAGE_NAME = "${DOCKERHUB_USERNAME}"+ "/" + "${APP_NAME}" 
        DOCKERHUB_CRED_ID = "dockerhub"
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
            //    git credentialsId: "<id>" branch: "master" url: 'https://github.com/SudeepGowda55/python_devops.git'
            }
        }
        stage("Build Docker Images"){
            steps{
                script{
                    // docker_image = docker.build "${IMAGE_NAME}"
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }
        // stage("Push Docker Images to Docker Registery"){
        //     steps{
        //         script{
        //             docker.withRegistery('', DOCKERHUB_CRED_ID){
        //             docker_image.push("$BUILD_NUMBER")
        //             docker_image.push("latest")
        //         }
        //         }
        //     }
        // }
    }
}
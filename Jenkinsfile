pipeline{

    agent any

    environment{
        IMAGE_NAME = "sudeepgowda55"+ "/" + "anonymous_ftp_access" 
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

        stage('SonarQube analysis') {
            steps{
                withSonarQubeEnv('sonarqube-8.9') { 
                // If you have configured more than one global server connection, you can specify its name
//      sh "${scannerHome}/bin/sonar-scanner"
                   println "${env.SONAR_HOST_URL}"
                }
            }
        }

        // stage("Build Docker Images"){
        //     steps{
        //         script{
        //             sh "docker build -t ${IMAGE_NAME}:1.${BUILD_NUMBER} -t ${IMAGE_NAME}:latest ."
        //         }
        //     }
        // }

        // stage("Push Docker Images to Docker Registery"){
        //     steps{
        //         script{              
        //             withDockerRegistry([ credentialsId: "dockerhub", url: "https://index.docker.io/v1/" ]) {
        //                 sh "docker push ${IMAGE_NAME}:1.${BUILD_NUMBER}"
        //                 sh "docker push ${IMAGE_NAME}:latest"
        //             }   
        //         }  
        //     }
        // }

        // stage("Cleanup Workspace and docker images"){
        //     script{
        //         cleanWs()
        //         sh "docker rmi ${IMAGE_NAME}:1.${BUILD_NUMBER}"
        //         sh "docker rmi ${IMAGE_NAME}:latest"
        //     }
        // }
    }
}

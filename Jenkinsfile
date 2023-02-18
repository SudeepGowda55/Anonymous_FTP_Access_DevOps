pipeline{

    agent any

    environment{
        IMAGE_NAME = "sudeepgowda55"+ "/" + "anonymous_ftp_access" 
    }

    node {
         stage('SCM') {
            checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarQube-main-server';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}

    // stages{
    //     stage('cleanup Workspace'){
    //        steps {
    //             cleanWs()
    //        }
    //     }

    //     stage("git checkout"){
    //         steps{
    //             git branch: "master", url: 'https://github.com/SudeepGowda55/python_devops.git'
    //         //    for private repository 
    //         //    git credentialsId: "<id>", branch: "master", url: 'https://github.com/SudeepGowda55/python_devops.git'
    //         }
    //     }

    //     stage('SonarQube analysis') {
    //         // steps{
    //         //     withSonarQubeEnv('SonarQube-main-server') { 
    //         //        println "${env.SONAR_HOST_URL}"
    //         //     }
    //         // }
    //         def scannerHome = tool 'SonarQube-main-server';
    //             withSonarQubeEnv() {
    //             sh "${scannerHome}/bin/sonar-scanner"
    //         }
    //     }

    //     // stage("Build Docker Images"){
    //     //     steps{
    //     //         script{
    //     //             sh "docker build -t ${IMAGE_NAME}:1.${BUILD_NUMBER} -t ${IMAGE_NAME}:latest ."
    //     //         }
    //     //     }
    //     // }

    //     // stage("Push Docker Images to Docker Registery"){
    //     //     steps{
    //     //         script{              
    //     //             withDockerRegistry([ credentialsId: "dockerhub", url: "https://index.docker.io/v1/" ]) {
    //     //                 sh "docker push ${IMAGE_NAME}:1.${BUILD_NUMBER}"
    //     //                 sh "docker push ${IMAGE_NAME}:latest"
    //     //             }   
    //     //         }  
    //     //     }
    //     // }

    //     // stage("Cleanup Workspace and docker images"){
    //     //     script{
    //     //         cleanWs()
    //     //         sh "docker rmi ${IMAGE_NAME}:1.${BUILD_NUMBER}"
    //     //         sh "docker rmi ${IMAGE_NAME}:latest"
    //     //     }
    //     // }
    // }
}

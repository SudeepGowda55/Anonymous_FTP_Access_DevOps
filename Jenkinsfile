pipeline{

    agent any

    // environment{
    //     DOCKERHUB_USERNAME = "sudeepgowda55"
    //     APP_NAME = "python_devops"
    //     IMAGE_TAGNAME = "${BUILD_NUMBER}"
    //     IMAGE_NAME = "${DOCKERHUB_USERNAME}"+ "/" + "${APP_NAME}" 
    //     DOCKERHUB_CRED = "dockerhub"
    // }

    stages{
        stage('cleanup workspace'){
           steps {
            script {
                cleanWs()
            }
           }
        }
    }
}
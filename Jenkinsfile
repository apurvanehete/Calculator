pipeline
{
    environment
    {
        registry = "apurvanehete/softnauticsllp"
        registryCredential = 'Docker_ID'
        dockerimage = ''
    }
    agent any
    stages {
        stage('Cloning our Git')
        {
            steps
            {
                git branch: 'master', credentialsId: '872f84d6-0500-4d2d-ab78-ea58896914e0', url: 'https://github.com/apurvanehete/Calculator.git'
            }
        }
        stage('Building our image')
        {
            steps
            {
                script {
                     dockerimage = docker.build registry + ":$BUILD_NUMBER"
                     sh "docker run $dockerimage"

                }

            }
        }
        stage('Deploy our image')
        {
            steps
            {
                script {
                    docker.withRegistry( '', registryCredential ) {
                    dockerimage.push() }
                }
            }
        }
        stage('Cleaning up')
        {
            steps
            {
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
    }
}
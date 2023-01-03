pipeline
{
    environment
    {
        registry = "apurvanehete/softnauticsllp"
        registryCredential = 'Docker_ID'
        dockerImage = ''
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
                     dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }

            }
        }
        stage('Deploy our image')
        {
            steps
            {
                script {
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push() }
                    sh "docker run $dockerImage"
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
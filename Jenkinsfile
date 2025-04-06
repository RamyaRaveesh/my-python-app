pipeline {
    agent any

    environment {
        // Define environment variables like AWS keys, etc.
        GITHUB_REPO = 'https://github.com/RamyaRaveesh/my-ci-cd-repo.git'
        BRANCH_NAME = 'main'
        EC2_IP = '13.51.70.213'  // EC2 instance public IP address
        PEM_PATH = 'C:\\Users\\ravee\\Downloads\\my-sample-app.pem' 
    }
    triggers {
        githubPush() // This ensures the job triggers on GitHub push events
    }
    stages {
        stage('Checkout Code') {
            steps {
                 deleteDir()  
                sh 'git init'  
                git branch: 'main', url: GITHUB_REPO
            }
        }

       stage('Run Tests') {
            steps {
                script {
                    sh './venv/bin/pytest test_app.py'  // Adjust according to your test setup
                }
            }
        }

        stage('Deploy to AWS EC2') {
            steps {
                script {
                    // SSH and deploy to EC2 (replace with your deployment script or commands)
                    sh '''
                    ssh -o StrictHostKeyChecking=no -i ${PEM_PATH} ubuntu@${EC2_IP} << 'EOF'
                        cd /path/to/project
                        git pull origin main
                        sudo systemctl restart my-python-app
                    EOF
                    '''
                }
            }
        }
    }
post {
    always {
        // Send an email with the build status
        emailext(
            subject: "Jenkins Build Status: ${currentBuild.currentResult}",
            body: """
                <h3>Build Status: ${currentBuild.currentResult}</h3>
                <p>Job: ${env.JOB_NAME}</p>
                <p>Build Number: ${env.BUILD_NUMBER}</p>
                <p>Build URL: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                <p>Test Report: <a href="${env.BUILD_URL}testReport">${env.BUILD_URL}testReport</a></p>
            """,
            to: "ramyashridharmoger@gmail.com"  // Replace with the recipient's email address
        )
    }
}

}

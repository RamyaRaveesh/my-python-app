pipeline {
    agent any

    environment {
        GITHUB_REPO = 'https://github.com/RamyaRaveesh/my-python-app.git'
        BRANCH_NAME = 'main'
        EC2_IP = '51.21.197.126'
        PEM_PATH = '/tmp/my-sample-app.pem'
    }
    triggers {
        githubPush() // This ensures the job triggers on GitHub push events
    }
    stages {
        stage('Checkout Code') {
            steps {
                deleteDir()  // Clean workspace
                sh 'git init'  // Initialize git repository
                git branch: 'main', url: GITHUB_REPO  // Checkout the specified branch (main)
            }
        }

        stage('Set up Virtual Environment') {
            steps {
                script {
                    // Ensure the virtual environment is created
                    sh 'python3 -m venv venv'  // Create the virtual environment
                    // Activate the virtual environment and install dependencies
                    sh './venv/bin/pip install --upgrade pip'  // Upgrade pip in the virtual environment
                    sh './venv/bin/pip install -r requirements.txt'  // Install dependencies from requirements.txt
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Check if pytest is installed and run tests
                    sh './venv/bin/pytest test_app.py'  // Run tests with pytest inside the virtual environment
                }
            }
        }

        stage('Deploy to AWS EC2') {
            steps {
                script {
                    // Directly execute commands with SSH
                    sh """
                    ssh -o StrictHostKeyChecking=no -i ${PEM_PATH} ubuntu@${EC2_IP} '
                        # Check if directory exists, if not, create it and clone the repo
                        if [ ! -d "/home/ubuntu/my-python-app/.git" ]; then
                            # Directory does not exist or is not a Git repository, so clone
                            mkdir -p /home/ubuntu/my-python-app
                            cd /home/ubuntu/my-python-app
                            git clone ${GITHUB_REPO} .  # Clone the repo into the directory
                        else
                            # Directory is a Git repository, so pull the latest changes
                            cd /home/ubuntu/my-python-app
                            git pull origin ${BRANCH_NAME}  # Pull the latest changes
                        fi

                        # Restart the app
                        sudo systemctl restart my-python-app || echo "Service 'my-python-app' not found."
                    '
                    """
                }
            }
        }
    }
    post {
        always {
            script {
                emailext(
                    subject: "Jenkins Build Status: ${currentBuild.currentResult}",
                    body: """
                        <h3>Build Status: ${currentBuild.currentResult}</h3>
                        <p>Job: ${env.JOB_NAME}</p>
                        <p>Build Number: ${env.BUILD_NUMBER}</p>
                        <p>Build URL: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                        <p>Test Report: <a href="${env.BUILD_URL}testReport">${env.BUILD_URL}testReport</a></p>
                    """,
                    to: "ramyashridharmoger@gmail.com"
                )
            }
        }
    }
}

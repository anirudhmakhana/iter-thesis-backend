pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'whoami'
                sh 'docker-compose -f Docker-compose.prod.yml build'
            }
        }

        stage('Deploy') {
            steps {
                sh 'chmod +x /var/lib/jenkins/workspace/backend/iterthesisproject/entrypoint.prod.sh'
                sh 'docker-compose -f Docker-compose.prod.yml up -d'
            }
        }

        stage('Setting up Django') {
            steps {
                sh 'docker-compose -f Docker-compose.prod.yml exec -T web python manage.py makemigrations --noinput'
                sh 'docker-compose -f Docker-compose.prod.yml exec -T web python manage.py migrate --noinput'
                sh 'docker-compose -f Docker-compose.prod.yml exec -T web python manage.py collectstatic --no-input --clear'
            }
        }

        stage('Test Accounts') {
            steps {
                sh 'docker-compose -f Docker-compose.prod.yml exec -T web python manage.py test account'
            }
        }

        stage('Test Places') {
            steps {
                sh 'docker-compose -f Docker-compose.prod.yml exec -T web python manage.py test places'
            }
        }

        stage('SonarQube Analysis') {
            steps{
                script{
                    def scannerHome = tool 'sq1';
                    withSonarQubeEnv() {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }
    }
}
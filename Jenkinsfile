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
                sh 'docker-compose -f Docker-compose.prod.yml exec web python manage.py migrate --noinput'
                sh 'docker-compose -f Docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear'
            }
        }
    }
}
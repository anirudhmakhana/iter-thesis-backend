pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'sudo docker-compose -f docker-compose.yml build'
            }
        }

        stage('Deploy') {
            steps {
                sh 'sudo chmod +x /var/lib/jenkins/workspace/backend/iterthesisproject/entrypoint.prod.sh'
                sh 'sudo docker-compose -f docker-compose.yml up -d'
            }
        }

        stage('Setting up Django') {
            steps {
                sh 'sudo docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput'
                sh 'sudo docker-compose -f docker-compose.yml exec web python manage.py collectstatic --no-input --clear'
            }
        }
    }
}
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker-compose -f docker-compose.prod.yml build'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose -f docker-compose.prod.yml up -d'
            }
        }

        stage('Setting up Django') {
            steps {
                sh 'docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput'
                sh 'docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear'
            }
        }
    }
}
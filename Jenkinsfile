pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'sudo docker-compose -f Docker-compose.prod.yml build'
            }
        }

        stage('Deploy') {
            steps {
                sh 'sudo chmod +x entrypoint.prod.sh'
                sh 'sudo docker-compose -f Docker-compose.prod.yml up -d'
            }
        }

        stage('Setting up Django') {
            steps {
                sh 'sudo docker-compose -f Docker-compose.prod.yml exec web python manage.py migrate --noinput'
                sh 'sudo docker-compose -f Docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear'
            }
        }
    }
}
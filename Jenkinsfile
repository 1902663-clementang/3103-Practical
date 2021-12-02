pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python -m py_compile src/app.py ' 
                stash(name: 'compiled-results', includes: 'src/*.py*') 
            }
        }
		stage('Code Quality Check via SonarQube') {
			steps {
				 script {
				 def scannerHome = tool 'SonarQube';
				 withSonarQubeEnv('SonarQube') {
				 sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey='3103 Practical -Dsonar.sources=."
				 }
			}
		}
	}
 }
}

pipeline {
    agent none

    stages {
        stage('Parameters for pipeline'){
          agent {
                label 'master'
            }
          parameters: [[$class: 'LabelParameterValue', name: 'node', label: 'master']]
      }

}

}
               

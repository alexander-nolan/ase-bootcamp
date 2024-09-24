```yaml
variables:
  - name: environment
    value: 'dev' # Set to 'dev', 'staging', or 'prod' based on the deployment environment

steps:
  - task: AzureKeyVault@2
    inputs:
      azureSubscription: 'MyServiceConnection'
      KeyVaultName: 'MyKeyVault'
      SecretsFilter: 'databasePassword,wordpressAdminPassword'
      RunAsPreJob: true

  # Create Kubernetes Secret using retrieved values
  - script: |
      kubectl create secret generic wordpress-secrets \
      --from-literal=wordpressPassword=$(wordpressAdminPassword) \
      --from-literal=mariadbRootPassword=$(databasePassword) \
      --namespace $(environment) --dry-run=client -o yaml | kubectl apply -f -
    displayName: 'Create Kubernetes Secret'

  - task: HelmDeploy@0
    inputs:
      connectionType: 'AzureResourceManager'
      azureSubscription: 'MyServiceConnection'
      azureResourceGroup: 'myResourceGroup'
      kubernetesCluster: 'myAKSCluster'
      namespace: '$(environment)'
      command: 'upgrade'
      chartType: 'Name'
      chartName: 'bitnami/wordpress'
      releaseName: 'wordpress-release'
      overrideValues: |
        existingSecret=wordpress-secrets
      install: true
```
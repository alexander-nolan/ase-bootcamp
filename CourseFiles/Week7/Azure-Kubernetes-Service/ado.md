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

```sh
Starting: AzureKeyVault@2
==============================================================================
Task         : Azure Key Vault
Description  : Download Azure Key Vault secrets in a pipeline
Version      : 2.2.4
Author       : Microsoft Corporation
Help         : https://aka.ms/azurekeyvaulttroubleshooting
==============================================================================
##[command]Connecting to Azure Key Vault using 'MyServiceConnection'
##[command]Retrieving secrets from Key Vault 'MyKeyVault'
##[command]Successfully retrieved secret 'databasePassword' and added to pipeline variables
##[command]Successfully retrieved secret 'apiKey' and added to pipeline variables
Finishing: AzureKeyVault@2
```

```sh
# Command Line Task Log
Starting: CommandLine
==============================================================================
Task         : Command Line
Description  : Run a command line script using Bash on Linux and macOS and cmd.exe on Windows
Version      : 2.182.0
Author       : Microsoft Corporation
Help         : https://docs.microsoft.com/azure/devops/pipelines/tasks/utility/command-line
==============================================================================
##[command]echo "The retrieved database password is: $(databasePassword)"
The retrieved database password is: mySecurePassword123
##[command]echo "The retrieved API key is: $(apiKey)"
The retrieved API key is: abc123XYZ
Finishing: CommandLine
```

```sh
kubectl get secret wordpress-secrets -n dev -o yaml
```

```yaml
apiVersion: v1
data:
  mariadbRootPassword: bXlTZWNyZXRQYXNzd29yZA==
  wordpressPassword: c3VwZXJTZWNyZXRQYXNzd29yZA==
kind: Secret
metadata:
  name: wordpress-secrets
  namespace: dev
type: Opaque
```

```sh
kubectl get secret wordpress-secrets -n prod -o yaml
```

```yaml
apiVersion: v1
data:
  mariadbRootPassword: cHJvZFNlY3JldFBhc3N3b3==
  wordpressPassword: cHJvZFN1cGVyU2VjcmV0UG==
kind: Secret
metadata:
  name: wordpress-secrets
  namespace: dev
type: Opaque
```







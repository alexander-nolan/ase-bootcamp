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
### Command to Decode the Secret Values

To decode the Base64 encoded secret values for readability:
```sh
echo cHJvZFNlY3JldFBhc3M= | base64 --decode
```

This will output the decoded secret value:
```sh
prodSecretPass
```

```json
{
  "properties": {
    "displayName": "Enforce Network Policies for AKS Namespaces",
    "description": "Ensure that all AKS namespaces have network policies defined.",
    "policyType": "Custom",
    "mode": "Microsoft.Kubernetes.Data",
    "metadata": {
      "category": "Kubernetes"
    },
    "parameters": {},
    "policyRule": {
      "if": {
        "allOf": [
          {
            "field": "type",
            "equals": "Microsoft.Kubernetes/connectedClusters"
          },
          {
            "field": "Microsoft.Kubernetes/namespaces/podSecurityPolicyTemplateSpec.networkPolicies",
            "exists": "false"
          }
        ]
      },
      "then": {
        "effect": "deny"
      }
    }
  }
}
```

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: aks-admins-cluster-role-binding
subjects:
- kind: Group
  name: "AKS-Admins"  # This is the Azure AD group name
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: cluster-admin
  apiGroup: rbac.authorization.k8s.io
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: non-critical-workload
spec:
  tolerations:
  - key: "taintKey"
    operator: "Equal"
    value: "virtual-node"
    effect: "NoSchedule"
  containers:
  - name: non-critical-container
    image: nginx
```







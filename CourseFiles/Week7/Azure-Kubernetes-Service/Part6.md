# Step-by-Step Guide for Integrating Azure Key Vault with AKS

## **Set Up Azure Key Vault**
- Ensure your Azure Key Vault is created and contains the necessary secrets that your application will use.

## **Enable Managed Identity on Your AKS Cluster**
- Update your AKS cluster to enable Managed Identity. This will allow the cluster to authenticate with Azure resources without using secrets.
- *Hint: Use AZ CLI command to update the AKS cluster configuration.*

## **Assign Key Vault Administrator Role to Managed Identity**
1. Retrieve the managed identity object ID of your AKS cluster.
2. Assign the `Key Vault Administrator` role to this identity for your Key Vault resource.
- *Hint: Use Azure CLI commands to get the object ID and assign roles.*

## **Install Azure Key Vault Provider for Secrets Store CSI Driver**
```bash
helm repo add csi-secrets-store-provider-azure https://azure.github.io/secrets-store-csi-driver-provider-azure/charts
helm install csi-secrets-store-provider-azure/csi-secrets-store-provider-azure --generate-name
```

## **Create a SecretProviderClass**
- Define a `SecretProviderClass` resource in Kubernetes to specify how secrets will be accessed from Azure Key Vault. 
- *Hint: Use a YAML configuration file to set parameters such as Key Vault name and object details.*

## **Deploy Your Application**
- Update your Kubernetes deployment to reference the `SecretProviderClass`. This will allow the application to retrieve secrets from Key Vault and use them as environment variables or mounted files.
- *Hint: Modify your deployment YAML to include environment variables or volume mounts based on the secrets.*

## **Example Kubernetes Deployment YAML**

Here’s an example of how to configure your Kubernetes deployment to use secrets from Azure Key Vault:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: my-app-image:latest
        env:
        - name: MY_SECRET
          valueFrom:
            secretKeyRef:
              name: my-secret
              key: my-secret-key
        volumeMounts:
        - name: secrets-store-inline
          mountPath: "/mnt/secrets-store"
          readOnly: true
      volumes:
      - name: secrets-store-inline
        csi:
          driver: secrets-store.csi.k8s.io
          readOnly: true
          volumeAttributes:
            secretProviderClass: "azure-keyvault"
---
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque
data:
  my-secret-key: <base64-encoded-secret-value>
```

### **Deploy the SecretProviderClass Resource**
- Apply the `SecretProviderClass` YAML configuration using `kubectl` to define how secrets should be accessed and mounted in the pods.

### **Verify the Setup**
- Ensure that the secrets are successfully being pulled into your AKS pods from Azure Key Vault by checking the mounted volumes or environment variables in your pods.

### **Troubleshooting Tips**
- Check the logs of the CSI driver pods for any errors or warnings if secrets are not being pulled as expected.
- Verify that the managed identity has the necessary permissions to access the Key Vault.

This guide provides a detailed step-by-step approach to integrating Azure Key Vault with AKS, using managed identity and the Secrets Store CSI Driver.

### Lab Completion

Congratulations! You have successfully completed the lab. You have learned how to:

- Set up and configure an AKS cluster.
- Deploy applications and scale them within the AKS environment.
- Debug and resolve issues in Kubernetes deployments.
- Monitor and secure your applications using Azure's monitoring tools.
- Use Log Analytics to filter and analyze pod logs for troubleshooting.
- Integrated AKS with Azure Key Vault

Explore further labs or exercises to continue expanding your knowledge of AKS and Kubernetes.
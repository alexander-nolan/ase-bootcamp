### Part 1: Introduction and Setup  

#### 1. Introduction (15 minutes)  

##### **Overview of the Lab Objectives**  
- Set up an Azure Key Vault using Azure CLI.
- Store and manage secrets, keys, and certificates in the Key Vault.
- Apply best practices for securing and accessing the Key Vault.
- Integrate the Key Vault with other Azure services.

##### **Brief on the Key Vault Architecture**  
- **Azure Key Vault**: Centralized cloud service for storing application secrets, keys, and certificates securely.
- **Azure CLI**: Command-line tool for managing Azure resources.

##### **Tools and Technologies Required**  
- **Azure CLI**: Command-line tool for managing Azure resources.
- **Azure Subscription**: Required to create and manage Azure resources.
- **Key Vault**: Azure service for managing secrets, keys, and certificates.

#### 2. Environment Setup (30 minutes)  

##### **Install Azure CLI**  
1. **Azure CLI Installation**  
   - Follow the instructions from the official Azure website to install Azure CLI on your system:  
     - [Azure CLI for Windows](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows)  
     - [Azure CLI for Mac](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-macos)  
     - [Azure CLI for Linux](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-linux)  

##### **Verify Installation**  
- Open a terminal or command prompt and run:  
  ```bash  
  az --version

```markdown
- You should see output indicating the installed version of Azure CLI.  

##### **Login to Azure**  
- Use the Azure CLI to log in to your Azure account:  
  ```bash  
  az login  
  ```
- Follow the instructions to complete the login process.

##### **Create a Resource Group**  
- Create a resource group to hold your Key Vault:  
  ```bash  
  az group create --name myResourceGroup --location eastus  
  ```

##### **Create a Key Vault**  
- Create a Key Vault in the resource group:  
  ```bash  
  az keyvault create --name myKeyVault --resource-group myResourceGroup --location eastus  
  ```

##### **Store a Secret in the Key Vault**  
- Store a secret in the Key Vault:  
  ```bash  
  az keyvault secret set --vault-name myKeyVault --name mySecret --value "mySecretValue"  
  ```

##### **Retrieve a Secret from the Key Vault**  
- Retrieve the secret from the Key Vault:  
  ```bash  
  az keyvault secret show --vault-name myKeyVault --name mySecret  
  ```

### Overview of the Project Structure  
Create a root directory for the project:  
```bash  
mkdir azure-key-vault-setup  
cd azure-key-vault-setup  
```

The project structure will be:  
```plaintext  
azure-key-vault-setup/  
├── scripts/  
│   ├── create-key-vault.sh  
│   ├── store-secret.sh  
│   └── retrieve-secret.sh  
└── README.md  
```

- **scripts/**: Directory for shell scripts to automate Key Vault operations.
- **create-key-vault.sh**: Script to create a Key Vault.
- **store-secret.sh**: Script to store a secret in the Key Vault.
- **retrieve-secret.sh**: Script to retrieve a secret from the Key Vault.
- **README.md**: Documentation for the setup process.

### Next Steps  
Proceed to Part 2 where you will start building the automation scripts, beginning with creating the Key Vault.
```
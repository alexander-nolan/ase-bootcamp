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
  ```

- You should see output indicating the installed version of Azure CLI.  

##### **Login to Azure and Select Subscription**

\```bash
az login
\```

- Use the Azure CLI to log in to your Azure account. After logging in, you will see a list of available subscriptions and a prompt to select a subscription. Select the one specified by your instructor.

##### **Verify Current Tenant and Subscription**

\```bash
az account show
\```

- This command displays the details of the currently selected subscription and tenant. Verify that the correct subscription and tenant are selected.

##### **Create a Resource Group**  
- Create a resource group to hold your Key Vault:  
  ```bash  
  az group create --name myResourceGroup --location eastus  
  ```

##### **Create a Key Vault**  
# Create a Key Vault in the resource group. Note: Key Vault names must be globally unique, which means 
# no two Key Vaults in the world can have the same name. To ensure this, append your initials and a unique 
# number to the Key Vault name. For example:

```bash  
az keyvault create --name myKeyVaultAN01624 --resource-group myResourceGroup --location eastus --enable-rbac-authorization
```

# Instructions:
# - Replace `myKeyVaultAN01624` with a unique name by adding your initials and a number.
# - If the command fails due to the name being taken, modify the number or name slightly and try again.
# - Key Vault names can contain alphanumeric characters (letters and numbers) and hyphens, but they must 
#   start and end with a letter or number and be between 3 and 24 characters long.

##### **View the Key Vault in the Azure Portal**  
- Open the [Azure Portal](https://portal.azure.com/).
- Navigate to "Resource groups" in the left-hand menu.
- Select the resource group `myResourceGroup`.
- Click on the Key Vault `myKeyVault` to view its details.

![alt text](images/Part1.png)

### Next Steps  
Proceed to Part 2 where you will create and retrieve keys.
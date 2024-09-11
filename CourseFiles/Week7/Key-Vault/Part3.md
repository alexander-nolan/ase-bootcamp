### Part 3: Creating and Retrieving Secrets

#### 1. Create a Secret in the Key Vault

##### **Create a Secret**

  ```bash
az keyvault secret set --vault-name myKeyVault --name mySecretWithOptions --value "mySecretValue" --description "This is a test secret with additional options" --tags env=test --content-type "text/plain"
  ```
- This command creates a secret with the value mySecretValue, a description, tags it with env=test, and sets the content type to text/plain.

#### 2. Retrieve the Secret

##### **Retrieve the Secret**

  ```bash
  az keyvault secret show --vault-name myKeyVault --name mySecret
  ```

#### 3. Confirm Secret Creation in the Azure Portal

##### **View the Secret in the Azure Portal**
- Open the [Azure Portal](https://portal.azure.com/).
- Navigate to "Resource groups" in the left-hand menu.
- Select the resource group `myResourceGroup`.
- Click on the Key Vault `myKeyVault`.
- In the Key Vault, navigate to "Secrets" under the "Settings" section.
- Confirm that the secret `mySecret` is listed.
- Click on the secret `mySecret` to view its details.
- Under the "Properties" section, confirm that the description and tags are correctly set.

#### 4. Create a New Version of the Secret

##### **Create a New Version of the Secret**

  ```bash
  az keyvault secret set --vault-name myKeyVault --name mySecret --value "myNewSecretValue"
  ```
- This command creates a new version of the secret mySecret with the value myNewSecretValue.

#### 5. Confirm New Version in the Azure Portal

##### **View the New Version in the Azure Portal**
- Open the [Azure Portal](https://portal.azure.com/).
- Navigate to "Resource groups" in the left-hand menu.
- Select the resource group `myResourceGroup`.
- Click on the Key Vault `myKeyVault`.
- In the Key Vault, navigate to "Secrets" under the "Settings" section.
- Confirm that the secret `mySecret` is listed.
- Click on the secret `mySecret` to view its details.
- Click on the "Versions" tab to view all versions of the secret.
- Confirm that the new version with the value `myNewSecretValue` is listed.
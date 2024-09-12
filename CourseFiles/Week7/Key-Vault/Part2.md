### Part 2: Creating and Retrieving Keys

#### 1. Create a Key in the Key Vault

##### **Create a Key**

  ```bash
  az keyvault key create --vault-name myKeyVault --name myKey --protection software --kty RSA --size 2048 --ops encrypt decrypt sign verify
  ```
  - This command creates an RSA key with a size of 2048 bits and allows the operations: encrypt, decrypt, sign, and verify.

#### 2. Retrieve the Key

##### **Retrieve the Key**
- Use the Azure CLI to retrieve the key from the Key Vault:
  ```bash
  az keyvault key show --vault-name myKeyVault --name myKey
  ```

#### 3. Confirm Key Creation in the Azure Portal

##### **View the Key in the Azure Portal**
- Open the [Azure Portal](https://portal.azure.com/).
- Navigate to "Resource groups" in the left-hand menu.
- Select the resource group `myResourceGroup`.
- Click on the Key Vault `myKeyVault`.
- In the Key Vault, navigate to "Keys" under the "Settings" section.
- Confirm that the key `myKey` is listed.
- Click on the key `myKey` to view its details.
- Under the "Key operations" section, confirm that the operations `encrypt`, `decrypt`, `sign`, and `verify` are listed.

### Next Steps  
Proceed to Part 3 where you will create and retrieve keys.
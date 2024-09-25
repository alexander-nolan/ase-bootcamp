### Part 3: Creating and Retrieving Secrets

#### Introduction

##### **Overview of the Lab Objectives**
- Understand the role-based access control (RBAC) requirements for managing keys.
- Assign the appropriate RBAC role to the currently logged-in user.
- Successfully create and retrieve secrets from the Key Vault.
- Create a new version of your secret.

### Assign Roles

#### Assign the Appropriate RBAC Role

- Refer to the Azure documentation to identify the role that grants permissions to create Key Vault secrets.
  
- Use the Azure CLI to assign this role to your user account. Ensure that you adhere to the **Principle of Least Privilege** by selecting the minimal permissions required for your tasks.

**Note:** Always review and verify the permissions associated with each role to ensure secure and appropriate access control.

##### Verify Role Assignments

```bash
az role assignment list --assignee <user-object-id> --scope /subscriptions/<subscription-id>/resourceGroups/myResourceGroup/providers/Microsoft.KeyVault/vaults/<key-vault-name> --output table
```

- This command lists the role assignments for the specified user and scope, allowing you to verify that both the Key Vault Crypto Officer and Key Vault Secrets Officer roles have now been assigned.

### Create and Retrieve Secrets

- Use the Azure CLI to create a new secret in your Key Vault. Ensure that you specify the correct Key Vault name and secret value.

- Retrieve the secret using the Azure CLI to confirm it has been stored correctly. Make sure to handle the output securely and avoid exposing sensitive information.

##### Confirm Secret Creation in the Azure Portal
- Open the [Azure Portal](https://portal.azure.com/).
- Navigate to "Resource groups" in the left-hand menu.
- Select the resource group `myResourceGroup`.
- Click on the Key Vault.
- In the Key Vault, navigate to "Secrets" under the "Settings" section.
- Confirm that the secret `mySecret` is listed.
- Click on the secret `mySecret` to view its details.
- Click on the current version.
- Click `Show Secret Value`

![alt text](images/Part3-a.png)

### Secret Version Management

#### Create a New Version of the Secret

- Determine how to create a new version of your secret using either the Azure portal or the Azure CLI.
- Verify the creation of the new version by viewing both the current and previous versions of the secret in your Key Vault.
- Use the Azure CLI to retrieve the older version of the secret to confirm its availability and integrity.

#### Additional Secret Management Tasks

- **Backup:** Download a backup of your secret to ensure you have a copy available in case of accidental deletion.
- **Delete:** Remove the secret from your Key Vault using the Azure Portal. Confirm that it has been removed from the list of secrets.
- **Restore Attempt:** Attempt to restore the secret from the backup file. If this fails, investigate whether the secret has been permanently deleted or if other issues are preventing the restoration.
- **Restore:** Successfully restore the deleted secret using the backup, and verify that it appears correctly in the Key Vault.

**Tip:** Always verify the secret’s status and versions before and after performing management tasks to ensure data integrity and security.

### Next Steps  
Proceed to Part 4 where you will create and retrieve certificates.
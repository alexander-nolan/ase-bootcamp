### Part 5: Auditing Key Vault Activity

#### Introduction

##### **Overview of the Lab Objectives**
- Understand the importance of auditing Key Vault activity for security and compliance.
- Enable Azure Monitor for Key Vault to capture activity logs.
- Configure Diagnostic Logs for detailed insights into Key Vault operations.
- Analyze logs using Azure Monitor to identify and respond to potential security issues.

#### Create a Log Analytics Workspace

##### **Create a Log Analytics Workspace**

```bash
az monitor log-analytics workspace create --resource-group myResourceGroup --workspace-name myWorkspace --location eastus
```

- This command creates a Log Analytics workspace named `myWorkspace` in the resource group `myResourceGroup` and location `eastus`.

#### Enable Diagnostic Logging

##### **Enable Diagnostic Logging for Key Vault**

```bash
az monitor diagnostic-settings create \
  --resource /subscriptions/<subscription-id>/resourceGroups/myResourceGroup/providers/Microsoft.KeyVault/vaults/<key-vault-name> \
  --name "keyvault-diagnostics" \
  --logs '[{"category": "AuditEvent","enabled": true}]' \
  --workspace myWorkspace
```

- This command enables diagnostic logging for the Key Vault and sends the logs to the Log Analytics workspace `myWorkspace`.

#### View Audit Logs in Azure Portal

##### **View Audit Logs**

- Craft a kusto query in your log analytics workspace that outputs all key vault audit activity, but scope it specifically to the key vault you created.
- Backup and restore a key vault item. Rerun your query. Do you see any new events?
- Enable the 'Request' and 'Errors' log categories on the diagnostic setting you created. Generate new activity. Create keys, delete keys etc
- Rerun your query one more time but this time, scope it to a different log category.

### Next Steps  
Proceed to Part 6 where you will configure different network isolation options
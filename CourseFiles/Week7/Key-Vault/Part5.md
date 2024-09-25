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

### View Audit Logs in Azure Portal

#### View Audit Logs

- **Kusto Query:** Construct a Kusto query in your Log Analytics workspace that filters all Key Vault audit activity. Make sure to scope it specifically to the Key Vault you created to isolate relevant events.
  
- **Backup and Restore:** Perform a backup and restore operation on a Key Vault item. Rerun your query to check for any new events related to these activities.

- **Enable Log Categories:** Update the diagnostic settings for your Key Vault to include the 'Request' and 'Errors' log categories. Perform actions like creating or deleting keys to generate new log entries.

- **Refine Your Query:** Rerun your query, this time focusing on the new log categories. Observe and analyze the changes in log data to better understand how different activities are logged in Key Vault.

**Note:** Regularly review and update your diagnostic settings and queries to ensure comprehensive monitoring and auditing of Key Vault activities.

### Next Steps  
Proceed to Part 6 where you will configure different network isolation options
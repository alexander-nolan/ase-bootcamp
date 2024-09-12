### Part 5: Auditing Key Vault Activity

Auditing Key Vault activity is crucial for security and compliance. Azure Key Vault provides logging and monitoring capabilities through Azure Monitor, which includes Azure Activity Logs and Diagnostic Logs.

#### 1. Create a Log Analytics Workspace

##### **Create a Log Analytics Workspace**

```bash
az monitor log-analytics workspace create \
  --resource-group myResourceGroup \
  --workspace-name myWorkspace \
  --location eastus
```

- This command creates a Log Analytics workspace named `myWorkspace` in the resource group `myResourceGroup` and location `eastus`.

#### 2. Enable Diagnostic Logging

##### **Enable Diagnostic Logging for Key Vault**

```bash
az monitor diagnostic-settings create \
  --resource-id $(az keyvault show --name myKeyVault --query id -o tsv) \
  --name "keyvault-diagnostics" \
  --logs '[{"category": "AuditEvent","enabled": true}]' \
  --workspace $(az monitor log-analytics workspace show --resource-group myResourceGroup --workspace-name myWorkspace --query id -o tsv)
```

- This command enables diagnostic logging for the Key Vault `myKeyVault` and sends the logs to the Log Analytics workspace `myWorkspace`.

#### 3. View Audit Logs in Azure Portal

##### **View Audit Logs**

- Open the [Azure Portal](https://portal.azure.com/).
- Navigate to "Log Analytics workspaces" in the left-hand menu.
- Select the workspace `myWorkspace`.
- In the workspace, navigate to "Logs" under the "General" section.
- Use the following query to view Key Vault audit logs:

```kusto
AzureDiagnostics
| where ResourceType == "VAULTS" and Category == "AuditEvent"
| project TimeGenerated, OperationName, ResultType, CallerIpAddress, Identity, ResourceId
```

- This query filters the logs to show only Key Vault audit events and displays relevant information such as the time of the event, operation name, result type, caller IP address, identity, and resource ID.

#### 4. Set Up Alerts for Key Vault Activity

##### **Create an Alert Rule**

```bash
az monitor metrics alert create \
  --name "KeyVaultAccessAlert" \
  --resource-group myResourceGroup \
  --scopes $(az keyvault show --name myKeyVault --query id -o tsv) \
  --condition "total AuditEvent > 0" \
  --description "Alert for Key Vault access events" \
  --action-group myActionGroup
```

- This command creates an alert rule named `KeyVaultAccessAlert` that triggers when there is any Key Vault access event. The alert sends notifications to the specified action group `myActionGroup`.

#### 5. Confirm Alert Configuration

##### **View Alerts in Azure Portal**

- Open the [Azure Portal](https://portal.azure.com/).
- Navigate to "Monitor" in the left-hand menu.
- Select "Alerts" under the "Monitoring" section.
- Confirm that the alert rule `KeyVaultAccessAlert` is listed and configured correctly.
- Test the alert by accessing the Key Vault and verifying that the alert is triggered and notifications are sent.

This section guides users through creating a Log Analytics workspace, enabling diagnostic logging, viewing audit logs, setting up alerts, and confirming alert configurations for Azure Key Vault activity.
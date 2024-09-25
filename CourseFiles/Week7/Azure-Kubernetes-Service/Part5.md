### Part 5: Monitoring the AKS Workload

## Monitoring the Application

### **Access the Monitoring Dashboard**
- Retrieve the Log Analytics workspace associated with your AKS cluster.
- *Hint: Use AZ CLI to get the workspace resource ID.*

### **View Pod Error Logs in Azure Portal**
- Go to the [Azure Portal](https://portal.azure.com/).
- Navigate to **Log Analytics workspaces** and select the workspace linked to your AKS cluster.
- Under the "Logs" section, query your WordPress pod error logs by filtering for specific pod status reasons like `ImagePullBackOff` or `CrashLoopBackOff`.
- *Hint: Use Kusto Query Language (KQL) in the "Logs" section to filter and view pod errors.*
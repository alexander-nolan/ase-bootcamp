### Part 6: Network Isolation

Network isolation is essential for securing your Azure Key Vault by restricting access to specific virtual networks and IP addresses. This ensures that only authorized resources can access your Key Vault.

#### Disable Access from Public Networks

##### **Disable Public Network Access**

- Disable public access on your key vault
- Attempt to access some of the items you previously created.

##### **Get Public IP Address**

- Retrieve your public IP address.

##### **Enable Public Network Access With a default action of Deny**

- Use AZ CLI to enable public access, but only to your own IP address.
- Verify the configuration using the portal. You should see that only your IP is now allowed.
- Attempt to access your resources again. 

##### Delete your key vault

- Attempt to delete the key vault you created. 
- If you receive errors upon deletion, understand why. Work through the errors until your Key Vauly is deleted.

### Next Steps  
Proceed to Part 7 where you will use terraform to re-create your key vault
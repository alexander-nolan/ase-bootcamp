### Part 7: Key Vault creation with terraform

- Install terraform using your preferred method
- Create a storage account in Azure to use as your backend. This will store your state file.
- Create a key vault using the azurerm_key_vault resource.
- Once it's been created, enable purge protection using your existing terraform code. 
- Optonally create certificates, secrets and or keys with terraform. 
### Part 4: Creating and Retrieving Certificates

#### Introduction

##### **Overview of the Lab Objectives**
- Understand the role-based access control (RBAC) requirements for managing certificates.
- Assign the appropriate RBAC role to the currently logged-in user.
- Successfully create and retrieve certificates from the Key Vault.
- Create a new version of your certificate.

##### Assign The Appropriate RBAC Role

- Use Azure documentation to find the role that allows you to create Key Vault secrets.

- Use AZ CLI to assign the identified role to your user account. Keep the 'Prinicpal of least privilege' in mind when identifying and selecting your role. 

### **Verify Role Assignments**
- Check that the role has been correctly assigned to your user by listing their role assignments.

*Hint: Use commands to list role assignments and confirm the permissions.*


##### Create a policy.json file

```json
{
  "issuerParameters": {
    "name": "Self"
  },
  "keyProperties": {
    "exportable": true,
    "keySize": 2048,
    "keyType": "RSA",
    "reuseKey": true
  },
  "lifetimeActions": [
    {
      "action": {
        "actionType": "AutoRenew"
      },
      "trigger": {
        "daysBeforeExpiry": 30
      }
    }
  ],
  "secretProperties": {
    "contentType": "application/x-pem-file"
  },
  "x509CertificateProperties": {
    "extendedKeyUsage": ["1.3.6.1.5.5.7.3.1"],
    "keyUsage": [
      "cRLSign",
      "dataEncipherment",
      "digitalSignature",
      "keyEncipherment",
      "keyAgreement",
      "keyCertSign"
    ],
    "subject": "CN=example.com",
    "validityInMonths": 12
  }
}
```
- This policy file defines the properties of the certificate, including the key type, key size, subject, and validity period.

### **Retrieve the Certificate**
- Retrieve the certificate details from your Key Vault to verify its creation and configuration.

*Hint: Use Azure CLI commands to display certificate details.*

### **Verify the Certificate in the Azure Portal**
1. Go to the Azure Portal and navigate to your Key Vault.
2. Check the **Certificates** section to confirm that the certificate is listed and view its details.

#### Export the Certificate

##### **Export the Certificate**

- Use AZ CLI to export the certificate to your local machine in '.pem' format.

### **Convert the Certificate to PFX Format**
- Use OpenSSL or another tool to convert the PEM-formatted certificate to PFX format, commonly used for importing into various applications.

*Hint: Ensure you have the necessary tools installed for certificate conversion.*

### **Confirm the Exported Certificate**
- View the exported certificate file using a certificate management tool to ensure it matches the original properties set in the Key Vault.

### Next Steps  
Proceed to Part 5 where you will aufit key vault activity
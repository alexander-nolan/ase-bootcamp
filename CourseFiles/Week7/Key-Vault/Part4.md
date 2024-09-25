### Part 4: Creating and Retrieving Certificates

#### Introduction

##### **Overview of the Lab Objectives**
- Understand the role-based access control (RBAC) requirements for managing certificates.
- Assign the appropriate RBAC role to the currently logged-in user.
- Successfully create and retrieve certificates from the Key Vault.
- Create a new version of your certificate.

##### Assign The Appropriate RBAC Role

- Use Azure documentation to find the role that allows you to create Key Vault secrets.

- Use the Azure CLI to assign the identified role to your user account. Keep the 'Prinicpal of least privilege' in mind when identifying and selecting your role. 

##### Verify Role Assignments

- Use the Azure Portal to check the existing role assignments on your key vault.

#### Create and Retrieve Secrets

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

##### **Create a Certificate**

- Use AZ CLI to create a certificate file. Specify the policy file you created earlier.

##### **Retrieve the Certificate**

- Retrieve your certificate using both the CLI and the portal.

#### Export the Certificate

##### **Export the Certificate**

- Use AZ CLI to export the certificate to your local machine in '.pem' format.

##### **Convert the Certificate to PFX Format**

###### **Option 1: Using Bash**

- Use the tool of your choice to view the certificate information locally. 
- Convert the certificate to '.pfx' format
- Upload the '.pfx' formatted cert to key vault.

### Next Steps  
Proceed to Part 5 where you will aufit key vault activity
### Part 4: Creating and Retrieving Certificates

#### 1. Create a Certificate in the Key Vault

##### **Create a Certificate**

```bash
az keyvault certificate create --vault-name myKeyVault --name myCertificate --policy @policy.json
```

- This command creates a certificate named `myCertificate` in the Key Vault `myKeyVault` using the policy defined in the `policy.json` file.

##### **Example Policy File (policy.json)**

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

#### 2. Retrieve the Certificate

##### **Retrieve the Certificate**

```bash
az keyvault certificate show --vault-name myKeyVault --name myCertificate
```

- This command retrieves the details of the certificate named `myCertificate` from the Key Vault `myKeyVault`.

#### 3. Confirm Certificate Creation in the Azure Portal

##### **View the Certificate in the Azure Portal**
- Open the [Azure Portal](https://portal.azure.com/).
- Navigate to "Resource groups" in the left-hand menu.
- Select the resource group `myResourceGroup`.
- Click on the Key Vault `myKeyVault`.
- In the Key Vault, navigate to "Certificates" under the "Settings" section.
- Confirm that the certificate `myCertificate` is listed.
- Click on the certificate `myCertificate` to view its details.
- Under the "Properties" section, confirm that the certificate properties are correctly set.

#### 4. Create a New Version of the Certificate

##### **Create a New Version of the Certificate**

```bash
az keyvault certificate create --vault-name myKeyVault --name myCertificate --policy @policy.json
```

- This command creates a new version of the certificate `myCertificate` in the Key Vault `myKeyVault` using the same policy file.

#### 5. Confirm New Version in the Azure Portal

##### **View the New Version in the Azure Portal**
- Open the [Azure Portal](https://portal.azure.com/).
- Navigate to "Resource groups" in the left-hand menu.
- Select the resource group `myResourceGroup`.
- Click on the Key Vault `myKeyVault`.
- In the Key Vault, navigate to "Certificates" under the "Settings" section.
- Confirm that the certificate `myCertificate` is listed.
- Click on the certificate `myCertificate` to view its details.
- Click on the "Versions" tab to view all versions of the certificate.
- Confirm that the new version is listed.
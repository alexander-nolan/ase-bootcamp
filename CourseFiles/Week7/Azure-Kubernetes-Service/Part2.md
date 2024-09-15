### Part 2: Deploying a Sample Application with Helm

#### Introduction

##### **Overview of the Lab Objectives**
- Install Helm, a package manager for Kubernetes.
- Add a Helm repository.
- Deploy an open source sample application using Helm.
- Verify the deployment and explore the application.

#### Environment Setup

##### **Install Helm**
**Helm Installation**
   - Follow the instructions from the official Helm website to install Helm on your system:
     - [Helm for Windows](https://helm.sh/docs/intro/install/#from-the-binary-releases)
     - [Helm for Mac](https://helm.sh/docs/intro/install/#from-homebrew-macos)
     - [Helm for Linux](https://helm.sh/docs/intro/install/#from-snap-linux)

##### **Verify Installation**
- Open a terminal or command prompt and run:
  ```bash
  helm version
  ```

- You should see output indicating the installed version of Helm.

#### Add a Helm Repository

##### **Add the Bitnami Repository**

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
```

- This command adds the Bitnami repository to Helm, which contains a variety of open source Helm charts.

##### **Update Helm Repositories**

```bash
helm repo update
```

- This command updates the local Helm chart repository cache.

#### Deploy a Sample Application

##### **Deploy WordPress Using Helm**

```bash
helm install my-wordpress bitnami/wordpress
```

- This command deploys the WordPress application using the Bitnami Helm chart.

##### **Verify the Deployment**

```bash
kubectl get pods
```

- This command lists the pods in the default namespace, including the WordPress pods.
- This command may take a few minutes to complete. Wait until both pods reach `1/1 ready state` before continiuing to the next step.

##### **Get the Application URL**

```bash
kubectl get svc --namespace default my-wordpress
```

- This command retrieves the service details for the WordPress application, including the external IP address.

#### Explore the Application

##### **Access the WordPress Application**
- Open a web browser and navigate to the external IP address obtained in the previous step.
- You should see the WordPress sample application page.

![alt text](images/Part2-a.png)

### Next Steps
Proceed to Part 3 where you will learn how to scale and manage the deployed application in AKS.
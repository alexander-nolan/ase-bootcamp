### Part 3: Scaling the WordPress Application

#### Introduction

##### **Overview of the Lab Objectives**
- Manually scale the WordPress application deployed in Part 2.
- Understand the impact of scaling on application performance.
- Verify the scaling behavior of the application.

#### Environment Setup

##### **Prerequisites**
- Ensure you have completed Part 1 and Part 2 of the lab.
- Ensure `kubectl` and `helm` CLI tools are installed and configured.

##### **Enable Cluster Autoscaler**

```bash
az aks update --resource-group myResourceGroup --name myAKSCluster --enable-cluster-autoscaler --min-count 1 --max-count 5
```

- This command enables the cluster autoscaler for the AKS cluster, allowing it to automatically adjust the number of nodes based on the workload.
- The cluster autoscaler adjusts the number of nodes (virtual machines) in the AKS cluster. This is useful when the cluster needs more resources (CPU, memory) to run additional pods.

##### **Verify Autoscaling Configuration**

```bash
az aks show --resource-group myResourceGroup --name myAKSCluster --query "agentPoolProfiles[].{Name:name,MinCount:minCount,MaxCount:maxCount,EnableAutoScaling:enableAutoScaling}"
```

- This command verifies the autoscaling configuration for the AKS cluster, displaying the name, minimum count, maximum count, and autoscaling status of the node pools.

#### Scale the WordPress Application

##### **Check the Current Number of Pods**

```bash
kubectl get pods
```

##### **Scale the Deployment to 3 Replicas**

```bash
kubectl scale deployment my-wordpress --replicas=3
```

- This command scales the WordPress deployment to 3 replicas.

##### **Verify the Scaling**

```bash
kubectl get pods
```

- This command lists the pods in the default namespace, showing the increased number of WordPress pods.

##### **Scale the Deployment to 2 Replicas**

```bash
kubectl scale deployment my-wordpress --replicas=2
```

- This command scales the WordPress deployment to 2 replicas.

##### **Verify the Scaling Again**

```bash
kubectl get pods
```

- This command lists the pods in the default namespace, showing the decreased number of WordPress pods.

### Next Steps
Proceed to Part 4 where you will learn how to secure and monitor the scaled application in AKS.
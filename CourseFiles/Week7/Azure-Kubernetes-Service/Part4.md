# Part 4: Debugging the WordPress Application

## Introduction

### **Overview of the Lab Objectives**
- Simulate a failure in the WordPress deployment.
- Utilize debugging tools and techniques to identify and diagnose the issue.
- Resolve the problem and verify the solution.

## Environment Setup

### **Prerequisites**
- Complete Parts 1, 2, and 3 of the lab.
- Ensure that both `kubectl` and `helm` CLI tools are installed and properly configured.

## Simulate a Failure

### **Break the WordPress Deployment**

#### **Scale the Deployment to 0 Replicas**
- Reduce the WordPress deployment to zero replicas to stop all running pods. 
- *Hint: Use the `kubectl` command to scale down the deployment.*

#### **Edit the WordPress Deployment to Introduce an Error**
- Modify the deployment to use an invalid image name. 
- *Hint: Change the `image` tag under `spec.template.spec.containers`.*

#### **Scale the Deployment to 1 Replica**
- Scale up the deployment to one replica to initiate the pod creation with the invalid image. This will simulate the failure scenario.

## Debug the Application

### **Check the Status of the Pods**
- List the current status of the pods to verify if they are in a `CrashLoopBackOff` or `ImagePullBackOff` state.

### **Describe the Failing Pod**
- View detailed information about the failing pod, including events and error messages, to identify the issue.

### **Check the Logs of the Failing Pod**
- Retrieve and review the logs from the failing pod to further diagnose the problem. The logs will provide insights into why the pod is not starting correctly.
- *Hint: Use the `kubectl logs <pod-name>` command.*

### **Browse to the Application**
- Attempt to access the WordPress application using the service's external IP address. Confirm that the application is not available due to the simulated failure.

## Fix the Problem

### **Scale the Deployment to 0 Replicas**
- Scale down the WordPress deployment to zero replicas before making any changes.

### **Edit the WordPress Deployment to Correct the Error**
- Revert the image name to a valid value in the deployment configuration.

### **Scale the Deployment to 1 Replica**
- Scale up the deployment to one replica to start a new pod with the correct image.

### **Verify the Fix**

#### **Check the Status of the Pods**
- Confirm that the WordPress pods have reached a `Running` state, indicating the issue has been resolved.

#### **Check the Logs of the Fixed Pod**
- Verify the logs of the running pod to ensure the application is functioning correctly.

### **Browse to the Application**
- Access the WordPress application through the external IP to confirm that it is now running as expected.

### Next Steps
Proceed to Part 5 where you will learn how to monitor the application in Azure.
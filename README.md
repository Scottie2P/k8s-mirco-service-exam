# k8s-mirco-service-exam




These instructions will get you a copy of the project up and running testing and purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

I recommend `gcloud CLI` and `kubectl` manage your command environments.

https://cloud.google.com/sdk/docs/install 

https://kubernetes.io/docs/tasks/tools/



## Connect Cluster Kubernetes

   Download Lens install on your computer and add file k8s.config to Lens

    https://k8slens.dev/




   or Connect Kubernetes(GKE) on Google GCP


## Installing Kubernetes on GCP Cloud

  Create Network VPC On GCP 
  https://www.cloudskillsboost.google/focuses/7140?parent=catalog


Create Cluster Kubernetes On GCP 
  ```
  gcloud container clusters create my-k8s-cluster --num-nodes 2 --network vpc-k8s --zone asia-southeast1 --tags private --scopes=storage-rw,compute-ro
  ```


Create Node Pool
  ```
  gcloud container node-pools create engin-pool --cluster=my-k8s-cluster --enable-autorepair --enable-blue-green-upgrade --machine-type=g1-small --enable-autoscaling --num-nodes=1  --min-nodes=1 --max-nodes=3 --max-surge-upgrade=1 --max-unavailable-upgrade=1 --spot --zone=asia-southeast1
  ```


## Run API Docker 

run on local
 
 ```
   cd api-user 
  ```
or
 ```
   cd api-wallet
  ```

  ```
    docker build -t my_api .
  ```
  
  
   ```
    docker run -it --rm -p 5000:5000 my_api
  ```
  
  ## Run API Kubernetes 

run on CLuster
   cd k8smanifest
 
 ```
   kubectl apply --filename api-user-deployment+service.yaml
   kubectl apply --filename api-wallet-deployment+service.yaml
   kubectl apply --filename ingress.yaml
   
  ```


  



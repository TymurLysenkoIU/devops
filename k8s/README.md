# Kubernetes

## Running the app in kubernetes manually (no yml)

1. ```shell
   kubectl create deployment sitiritis-iu-devops-app --image=sitiritis/iu-devops:latest
   ```
2. ```shell
   kubectl expose deployment sitiritis-iu-devops-app --type=LoadBalancer --port=80
   ```
3. ```shell
   minikube service sitiritis-iu-devops-app
   ```

After this the output of `kubectl get pods,svc` looks like this:

```
NAME                                           READY   STATUS    RESTARTS   AGE
pod/sitiritis-iu-devops-app-675489dfcc-tqbrb   1/1     Running   0          27m

NAME                              TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/kubernetes                ClusterIP      10.96.0.1        <none>        443/TCP        37m
service/sitiritis-iu-devops-app   LoadBalancer   10.107.251.145   <pending>     80:31269/TCP   11m

```

## Running the app in kubernetes with the usage of yml files

1. ```shell
   kubectl apply -f ./deployment.yml -f ./service.yml 
   ```
2. ```shell
   minikube service sitiritis-iu-devops-app
   ```

After this the output of `kubectl get pods,svc` looks like this:

```
NAME                                           READY   STATUS    RESTARTS   AGE
pod/sitiritis-iu-devops-app-6544dfd8ff-9jxr5   1/1     Running   0          5m14s

NAME                              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/kubernetes                ClusterIP   10.96.0.1       <none>        443/TCP   59m
service/sitiritis-iu-devops-app   ClusterIP   10.102.79.246   <none>        80/TCP    5m14s

```

## Install helm chart

1. ```shell
   helm install sitiritis-iu-devops-app ./sitiritis-iu-devops-app 
   ```
2. ```shell
   minikube service sitiritis-iu-devops-app
   ```

After this the output of `kubectl get pods,svc` looks like this:

```
NAME                                          READY   STATUS    RESTARTS   AGE
pod/sitiritis-iu-devops-app-88f848cdc-q9gjn   1/1     Running   0          2m29s

NAME                              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/kubernetes                ClusterIP   10.96.0.1       <none>        443/TCP   3h6m
service/sitiritis-iu-devops-app   ClusterIP   10.109.175.34   <none>        80/TCP    2m29s

```

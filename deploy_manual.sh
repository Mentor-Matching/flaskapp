#!/bin/sh

if [ $# -lt 1 ]; then
    echo "Usage: $0 <image_name>:<commit_hash>"
    exit 0
fi

SERVICE_NAME=mentor-matching
ACR_NAME=mentormatching
RES_GROUP=$ACR_NAME
AKV_NAME=$ACR_NAME-vault
IMAGE=$1

# Stop running container
echo "\n=========== Deleting running container ==========="
az container delete --resource-group $RES_GROUP --name acr-tasks
if [ ! $? -eq 0 ]; then
    echo "ERROR: Failed to stop running container"
    exit 1
fi

# Deploy container instance
echo "\n=========== Creating Container ============"
az container create \
    --resource-group $RES_GROUP \
    --name acr-tasks \
    --image $ACR_NAME.azurecr.io/$IMAGE \
    --registry-login-server $ACR_NAME.azurecr.io \
    --registry-username $(az keyvault secret show --vault-name $AKV_NAME --name $ACR_NAME-pull-usr --query value -o tsv) \
    --registry-password $(az keyvault secret show --vault-name $AKV_NAME --name $ACR_NAME-pull-pwd --query value -o tsv) \
    --dns-name-label acr-tasks-$ACR_NAME \
    --query "{FQDN:ipAddress.fqdn}" \
    --output table \
    --ports 80 443
if [ ! $? -eq 0 ]; then
    echo "ERROR: Failed to deploy container - image: $ACR_NAME.azurecr.io/$IMAGE"
    exit 1
fi

# Verify deployment
az container attach --resource-group $RES_GROUP --name acr-tasks

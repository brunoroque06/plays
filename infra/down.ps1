$ErrorActionPreference = 'Stop'

$sub = 'ac8c58b9-a2e7-44c9-bcf2-4b1f930c59b8'
$ten = '802458a5-5f60-41a0-b729-c79de49878a2'

az login --tenant $ten
az group delete --name rg-main --subscription $sub

$ErrorActionPreference = 'Stop'

terraform init
terraform apply

docker push brunoroque06/reportus

#!/usr/bin/env bash

cert_data=/home/vagrant/cert.json

export VAULT_ADDR=http://127.0.0.1:8200
export VAULT_TOKEN=root

vault write -format=json pki_int/issue/example-dot-com common_name="test.example.com" ttl="750h" > $cert_data

cat $cert_data | jq -r .data.certificate > /etc/nginx/ssl/test.example.com.crt
cat $cert_data | jq -r .data.issuing_ca >> /etc/nginx/ssl/test.example.com.crt
cat $cert_data | jq -r .data.private_key > /etc/nginx/ssl/test.example.com.key

sudo service nginx restart

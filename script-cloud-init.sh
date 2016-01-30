#!/bin/bash

for i in $(seq 2 2);
do

   echo "
   instance-id: iid-$i
   network-interfaces: |
     iface eth0 inet static
     address 192.168.124.$i
     network 192.168.124.0
     netmask 255.255.255.0
     broadcast 192.168.124.255
     gateway 192.168.124.1
   local-hostname: node-$i" > meta-data

   printf "#cloud-config\npassword: passw0rd\nchpasswd: { expire: False }\nssh_pwauth: True\n" > user-data

   genisoimage -output init-$i.iso -volid cidata -joliet -rock user-data meta-data

   qemu-img create -f qcow2 -b f23-cloud-base.qcow2 f23-cloud-node-$i.qcow2

done

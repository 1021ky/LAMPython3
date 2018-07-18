# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"

  if Vagrant.has_plugin?("vagrant-proxyconf")
    config.proxy.http     = "http://{proxy_ip}:{proxy_port}"
    config.proxy.https    = "http://{proxy_ip}:{proxy_port}"
    config.proxy.no_proxy = "localhost,127.0.0.1"
  end

  config.vm.define "web" do |machine|
    machine.vm.hostname = "web"
    machine.vm.network :private_network, ip:"192.168.20.10"
    machine.vm.network "forwarded_port", guest: 80, host: 8880
    machine.vm.provider "virtualbox" do |vb|
      vb.memory = "1028"
      vb.cpus=1
    end
  end

  config.vm.define "db" do |machine|
    machine.vm.hostname = "db"
    machine.vm.network :private_network, ip:"192.168.20.11"
    machine.vm.network "forwarded_port", guest: 3606, host: 3606  
    machine.vm.provider "virtualbox" do |vb|
      vb.memory = "1028"
      vb.cpus=1
    end
  end

  config.vm.define "provisioner", autostart: true do |machine|
    machine.vm.network "private_network", ip: "192.168.20.100"
    # set file permissions so that only owner user can read the ssh private key.
    machine.vm.synced_folder ".", "/vagrant",  mount_options: ['dmode=700','fmode=700']
  end
end

# NSO Juniper packages for T-SDN

These packages add Junos support to T-SDN for the following services:

- SR-TE
- L3 VPN

## Pre-requisisites

- T-SDN Core Function Pack
- Juniper Junos NED

## Installation
Copy the juniper-junos NED, and the packages from this repository, to the NSO
packages directory and reload the packages:

    admin@ncs# packages reload
    ...
    reload-result {
        package flat-l3vpn-juniper
        result true
    }
    reload-result {
        package juniper-junos-nc-4.6
        result true
    }
    reload-result {
        package sr-te-juniper
        result true
    }
    ...

Load merge the `dynamic-device-mapping.xml` file from each package directory:

    admin@ncs# config
    Entering configuration mode terminal
    admin@ncs(config)# load merge packages/sr-te-juniper/dynamic-device-mapping.xml
    Loading.
    358 bytes parsed in 0.01 sec (26.44 KiB/sec)
    admin@ncs(config)# load merge packages/flat-l3vpn-juniper/dynamic-device-mapping.xml
    Loading.
    376 bytes parsed in 0.01 sec (31.85 KiB/sec)
    admin@ncs(config)# commit
    Commit complete.

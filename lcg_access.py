try:
    import requests
except Exception:
    raise Exception("Install the requests library using 'pip install requests'")

cisco_model = {
    "opts": {
        "lab_name": "L3VPN_EXAMPLE",
        "dev_name": "R1"
    },
    "data": {
        "node_type": "ios_rtr",
        "hostname": "R1-CA-CORE",
        "domain": "bits.local",
        "snmpv3": [
            {
                "mode": "noAuthNoPriv",
                "username": "CISCO_MGMT1",
                "group_name": "CISCO_MGMT_GRP1",
                "peer": "10.0.0.1"
            },
            {
                "mode": "AuthNoPriv",
                "username": "CISCO_MGMT2",
                "group_name": "CISCO_MGMT_GRP2",
                "peer": "10.0.0.1",

                "auth_alg": "md5",
                "auth_pw": "033bd94b1168d7e4f0d644c3c95e35bf"
            },
            {
                "mode": "AuthPriv",
                "username": "CISCO_MGMT3",
                "group_name": "CISCO_MGMT_GRP3",
                "peer": "10.0.0.1",
                "auth_alg": "md5",
                "auth_pw": "033bd94b1168d7e4f0d644c3c95e35bf",
                "priv_alg": "aes_192",
                "priv_pw": "033bd94b1168d7e4f0d644c3c95e35bf"
            }
        ],
        "snmpv2": [
            {
                "community": "BITS_RW",
                "group_type": "rw",
                "access_list": "CORE_MGMT"
            },
            {
                "community": "BITS_RO",
                "group_type": "ro"
            }
        ],
        "interfaces": [
            {
                "link_id": "lo0",
                "description": "MGMT Interface",
                "ipv4_addrs": [
                    {
                        "address": "10.0.0.50",
                        "netmask": "255.255.255.255"
                    },
                    {
                        "address": "10.0.1.1",
                        "netmask": "255.255.255.255"
                    }
                ],
                "ipv6_addrs": [
                    {
                        "ipv6_address": "2001::1/128"
                    }
                ]
            },
            {
                "link_id": "Gi1",
                "bandwidth": "50",
                "description": "R2",
                "mpls": {
                    "ldp": True,
                    "mpls_te": True
                },
                "ospf": {
                    "p_id": "1",
                    "area_id": "100",
                    "network_type": "point-to-point",
                    "priority": "0",
                    "auth": {
                        "message_digest": [
                            {
                                "key_id": "1",
                                "val": "033bd94b1168d7e4f0d644c3c95e35bf"
                            },
                            {
                                "key_id": "2",
                                "val": "033bd94b1168d7e4f0d644c3c95e35bf"
                            }
                        ]
                    }
                },
                "ipv4_addrs": [
                    {
                        "address": "10.1.2.1",
                        "netmask": "255.255.255.255"
                    }
                ],
                "ipv6_addrs": [
                    {
                        "ipv6_address": "2001:1:2::1/64"
                    }
                ]
            },
            {
                "link_id": "Gi2",
                "bandwidth": "75",
                "description": "R3",
                "mpls": {
                    "ldp": True,
                    "mpls_te": False
                },
                "ospf": {
                    "p_id": "1",
                    "area_id": "30",
                    "network_type": "point-to-multipoint",
                    "priority": "2",
                    "auth": {
                        "key_chain": "TEST_CHAIN"
                    }
                },
                "ipv4_addrs": [
                    {
                        "address": "10.1.3.155",
                        "netmask": "255.255.255.255"
                    }
                ],
                "ipv6_addrs": [
                    {
                        "eui_64": "2001:1:3::/64"
                    }
                ]
            },
            {
                "link_id": "Gi3",
                "bandwidth": "30",
                "description": "R4",
                "mpls": {
                    "ldp": False,
                    "mpls_te": True
                },
                "ospf": {
                    "p_id": "1",
                    "area_id": "30",
                    "network_type": "point-to-multipoint",
                    "priority": "2",
                    "auth": {
                        "is_null": True
                    }
                },
                "ipv4_addrs": [
                    {
                        "address": "10.1.4.1",
                        "netmask": "255.255.255.255"
                    }
                ],
                "ipv6_addrs": [
                    {
                        "link_local": "fe80::1"
                    }
                ]
            },
            {
                "link_id": "Gi4",
                "bandwidth": "45",
                "description": "R5",
                "ipv4_addrs": [
                    {
                        "address": "10.1.5.1",
                        "netmask": "255.255.255.255"
                    }
                ],
                "ipv6_addrs": [
                    {
                        "anycast": "2001:6500::1/64"
                    }
                ]
            },
            {
                "link_id": "Gi1.99",
                "dot1q": "99",
                "bandwidth": "50",
                "description": "R2",
                "mpls": {
                    "ldp": True,
                    "mpls_te": True
                },
                "ospf": {
                    "p_id": "1",
                    "area_id": "100",
                    "network_type": "point-to-point",
                    "priority": "0",
                    "auth": {
                        "message_digest": [
                            {
                                "key_id": "1",
                                "val": "033bd94b1168d7e4f0d644c3c95e35bf"
                            },
                            {
                                "key_id": "2",
                                "val": "033bd94b1168d7e4f0d644c3c95e35bf"
                            }
                        ]
                    }
                },
                "ipv4_addrs": [
                    {
                        "address": "10.1.2.1",
                        "netmask": "255.255.255.255"
                    }
                ],
                "ipv6_addrs": [
                    {
                        "ipv6_address": "2001:1:2::1/64"
                    }
                ]
            }
        ]
    }
}

if __name__ == "__main__":
    LCG_URL = "http://apps.cbaxterjr.com:8080/api/v1/lcg/config"

    response = requests.post(url=LCG_URL,
                             json=cisco_model,
                             # Although the data varible is of dict type, we use the "json" arg for the request because it will automaticly convert the python dicontary into an JSON str that can be serialized accross the wire.
                             headers={"Content-Type": "application/json"})

    resp_str = response.content.decode()  # We execute the decode method because the http response received from the server returns the content in byte format. This will conver it to UTF-8.
    print(resp_str)

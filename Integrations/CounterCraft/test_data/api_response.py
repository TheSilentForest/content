response_dsns = {
    "data": [
        {
            "ctime": 1517482321.529951,
            "cuid": 2,
            "data": {
                "manual": False,
                "use_proxy": False,
                "install_bc_endpoint": False,
                "install_dsn": True,
                "connection": {
                    "ssh_port": 22,
                    "username": "ubuntu",
                    "password": "1234",
                    "certificate_id": "",
                },
            },
            "description": "Remote DSN",
            "dtime": None,
            "duid": None,
            "hostname": "1.2.3.3",
            "id": 2,
            "last_event": 0,
            "mtime": None,
            "muid": None,
            "name": "Remote DSN",
            "port": 7080,
            "status_code": "ACTIVE",
            "tags": None,
            "uuid": "e9670165-3247-4014-aef4-c4f759e72df4",
            "vsn": 1,
        },
        {
            "ctime": 1517482321.51069,
            "cuid": 2,
            "data": {
                "manual": False,
                "install_bc_endpoint": False,
                "install_dsn": True,
                "use_proxy": False,
                "connection": {
                    "ssh_port": 22,
                    "username": "ubuntu",
                    "password": "1234",
                    "private_key": "",
                },
            },
            "description": "Local network",
            "dtime": None,
            "duid": None,
            "hostname": "thedsn",
            "id": 1,
            "last_event": "1970-01-01T00: 00: 00.000Z",
            "mtime": 1517482557.89498,
            "muid": None,
            "name": "Local network",
            "port": 7080,
            "status_code": "ACTIVE",
            "tags": None,
            "uuid": "324f129a-08c5-4e60-907f-e16fb27fb649",
            "vsn": 3,
        },
    ],
    "statistics": [],
    "total_count": 2,
}

response_providers = {
    "data": [
        {
            "ctime": 1509615826.053955,
            "cuid": 2,
            "data": {},
            "description": "Hosts that are manually created",
            "dtime": None,
            "duid": None,
            "id": 1,
            "mtime": None,
            "muid": None,
            "name": "ManualMachine",
            "status_code": "ACTIVE",
            "tags": None,
            "type_code": "MANUAL_MACHINE",
            "vsn": 1,
            "provider_id": 1,
        },
        {
            "ctime": 1509615826.257955,
            "cuid": 2,
            "data": {},
            "description": "Hosts that are automatically created when activating breadcrumbs",
            "dtime": None,
            "duid": None,
            "id": 2,
            "mtime": None,
            "muid": None,
            "name": "CompanyProvider",
            "status_code": "ACTIVE",
            "tags": None,
            "type_code": "COMPANY_PROVIDER",
            "vsn": 1,
            "provider_id": 1,
        },
        {
            "ctime": 1509615826.288869,
            "cuid": 2,
            "data": {},
            "description": "Identities that are manually created",
            "dtime": None,
            "duid": None,
            "id": 3,
            "mtime": None,
            "muid": None,
            "name": "ManualIdentity",
            "status_code": "ACTIVE",
            "tags": None,
            "type_code": "MANUAL_IDENTITY",
            "vsn": 1,
            "provider_id": 1,
        },
        {
            "ctime": 1509615826.311929,
            "cuid": 2,
            "data": {},
            "description": "Routers that are manually created",
            "dtime": None,
            "duid": None,
            "id": 4,
            "mtime": None,
            "muid": None,
            "name": "ManualRouter",
            "status_code": "ACTIVE",
            "tags": None,
            "type_code": "MANUAL_ROUTER",
            "vsn": 1,
            "provider_id": 1,
        },
        {
            "ctime": 1509615826.322929,
            "cuid": 2,
            "data": {
                "api_key": "123",
                "misp_url": "https://www.test.com",
                " misp_verifycert": False,
            },
            "description": "",
            "dtime": None,
            "duid": None,
            "id": 5,
            "mtime": None,
            "muid": None,
            "name": "MISP Provider",
            "status_code": "ACTIVE",
            "tags": None,
            "type_code": "MISP_PROVIDER",
            "vsn": 1,
            "provider_id": 1,
        },
    ],
    "statistics": [],
    "total_count": 5,
}

response_campaigns = {
    "data": [
        {
            "ctime": 1507717890.821922,
            "cuid": 2,
            "description": "Campaign just to be used in devel",
            "dtime": None,
            "duid": None,
            "id": 1,
            "uuid": "eaae7ab5-55f3-4d25-acb4-15a4b126d890",
            "mtime": None,
            "muid": None,
            "name": "Devel Campaign",
            "status_code": "DESIGN",
            "role_code": "MANAGER",
            "tags": None,
            "vsn": 1,
        },
        {
            "ctime": 1507717890.838079,
            "cuid": 2,
            "description": "Campaign just to be used in devel 2",
            "dtime": None,
            "duid": None,
            "id": 2,
            "uuid": "3e0af461-bc74-44cb-b32f-06df2aad1dac",
            "mtime": None,
            "muid": None,
            "name": "2nd Campaign",
            "status_code": "DESIGN",
            "role_code": "MANAGER",
            "tags": None,
            "vsn": 1,
        },
    ],
    "statistics": [],
    "total_count": 2,
}

response_hosts = {
    "data": [
        {
            "deception_support_node_id": 2,
            "campaign_id": 2,
            "ctime": 1507717890.865759,
            "cuid": 2,
            "data": {
                "ip_address": "1.4.5.6",
                "os_family": "ubuntu_linux_16_04",
                "os_language": "en_EN",
                "port": 22,
                "username": "ubuntu",
                "password": "1234",
                "certificate_id": 1,
            },
            "description": "Linux machine in AWS",
            "dtime": None,
            "duid": None,
            "id": 1,
            "mtime": 1507717900.944572,
            "muid": None,
            "name": "Linux in AWS",
            "provider_id": 1,
            "status_code": "DESIGN",
            "tags": None,
            "instrumented": False,
            "fingerprint": None,
            "type_code": "MACHINE",
            "uuid": "61daa693-11cf-49a6-8fae-5111f630ee39",
            "vsn": 6,
        }
    ],
    "statistics": [],
    "total_count": 1,
}

response_services = {
    "data": [
        {
            "host_id": 2,
            "campaign_id": 1,
            "ctime": 1507717891.035867,
            "cuid": 2,
            "data": {
                "args": {
                    "cc_manual": False,
                    "cc_web_server_type": "nginx",
                    "cc_web_zip": "web.zip",
                },
            },
            "description": "<p>-</p>",
            "dtime": None,
            "duid": None,
            "id": 1,
            "mtime": 1507717894.407693,
            "muid": None,
            "name": "Employee web portal",
            "parent_id": None,
            "status_code": "ACTIVE",
            "tags": None,
            "type_code": "WEB_SERVER",
            "uuid": "74ebf088-0599-468d-804d-9229db18e0ef",
            "vsn": 2,
        },
        {
            "host_id": 1,
            "campaign_id": 1,
            "ctime": 1507717891.103787,
            "cuid": 2,
            "data": {
                "args": {
                    "cc_manual": True,
                    "cc_web_server_type": "apache2",
                    "web_zip": "web2.zip",
                },
            },
            "description": "<p>-</p>",
            "dtime": None,
            "duid": None,
            "id": 2,
            "mtime": 1507717894.63525,
            "muid": None,
            "name": "Test",
            "parent_id": None,
            "status_code": "DESIGN",
            "tags": None,
            "type_code": "WEB_SERVER",
            "uuid": "9ae5ad39-7820-4684-85e8-5751b9c7e68f",
            "vsn": 2,
        },
    ],
    "statistics": [],
    "total_count": 2,
}

response_breadcrumbs = {
    "data": [
        {
            "uuid": "6bd6e3f9-87f0-4dd0-8828-8c03656b1a58",
            "ctime": 1507717891.811903,
            "cuid": 2,
            "campaign_id": 1,
            "dsn_id": 1,
            "data": {
                "document_type": "xlsx",
                "lang": "es_ES",
                "url": "http://1.2.3.7/l65mc1aiufrpcmz4o",
            },
            "description": "<p>-</p>",
            "dtime": None,
            "duid": None,
            "id": 1,
            "mtime": 1507717895.749829,
            "muid": None,
            "name": "Fake Document",
            "services": [{"service_id": 1}, {"service_id": 2}],
            "hosts": [{"host_id": 1}],
            "status_code": "DESIGN",
            "tags": None,
            "type_code": "DOCUMENT",
            "vsn": 2,
        },
        {
            "uuid": "6bd6e3f9-87f0-4dd0-8828-8c03656b1a58",
            "ctime": 1507717891.871454,
            "cuid": 2,
            "campaign_id": 1,
            "dsn_id": 1,
            "data": {"mobileAppType": "public", "url": "http://1.2.3.4/jax9ij2w"},
            "description": "<p>-</p>",
            "dtime": None,
            "duid": None,
            "id": 2,
            "mtime": None,
            "muid": None,
            "name": "Fake Mobile App",
            "services": [{"service_id": 1}, {"service_id": 2}],
            "hosts": [],
            "status_code": "ACTIVE",
            "tags": None,
            "type_code": "MOBILE_APP",
            "vsn": 1,
        },
    ],
    "statistics": [],
    "total_count": 2,
}

response_incidents = {
    "data": [
        {
            "ctime": 1507718626.402509,
            "cuid": 2,
            "campaign_id": 1,
            "description": "Invalid auth incident.",
            "id": 1,
            "mtime": 1507718626.7619,
            "muid": None,
            "name": "Invalid auth",
            "status_code": "OPEN",
            "tlp_code": "GREEN",
            "tags": None,
            "vsn": 2,
            "objects": [1, 2, 3, 4],
            "events": [1, 2, 3, 4],
        }
    ],
    "statistics": [],
    "total_count": 1,
}

response_objects = {
    "data": [
        {
            "campaign_hits": [{"id": 2, "name": "Linux Campaign", "count": 5210}],
            "ctime": 1507718590.183822,
            "events_count": 168,
            "first_seen": 1507030039.331,
            "hits": 370,
            "id": 1411,
            "last_seen": 1507313997.703,
            "metadata": None,
            "mtime": None,
            "object_type_id": 5,
            "parent_id": None,
            "score": 0,
            "tags": None,
            "type_code": "CC_IP",
            "type_id": 1,
            "uuid": "ac4d5a93-00d9-45b0-941a-1bf198d8d87c",
            "value": "1.2.3.3",
            "vsn": 1,
        }
    ],
    "statistics": [],
    "total_count": 1,
}

response_events = {
    "data": [
        {
            "id": 7882,
            "vsn": 4,
            "ctime": 1570049656.121171,
            "mtime": 1570049656.49104,
            "campaign_id": 1,
            "event_category_id": 15,
            "type_code": "ValidAuth",
            "entity_id": 1,
            "log_message_id": "01DP740BW808VR898NAH095B78",
            "threat_actor_id": None,
            "event_date": 1570049630.0,
            "score": 100,
            "summary": "ubuntu",
            "data": {
                "event": "ValidAuth",
                "subject": "Login successful",
                "username": "ubuntu",
                "logon_type": -1,
                "process_basename": "su",
            },
            "event_category_entity_code": "INCIDENT",
            "event_category_type_code": "CC_FILE_ACTIVITY",
            "event_category_level_code": "MEDIUM",
            "service_id": 1,
            "service_name": "SYSTEM (Ubuntu18.04)",
            "host_id": 1,
            "host_name": "Ubuntu18.04",
            "campaign_name": "Linux Campaign",
            "tags": ["attack.T1078"],
        }
    ]
}

response_incidents = {
    "data": [
        {
            "ctime": 1580852613,
            "cuid": 2,
            "campaign_id": 1,
            "description": "Invalid auth incident.",
            "id": 1,
            "mtime": 1507718626.7619,
            "muid": None,
            "name": "Invalid auth",
            "status_code": "OPEN",
            "tlp_code": "GREEN",
            "tags": None,
            "vsn": 2,
            "objects": [1, 2, 3, 4],
            "events": [1, 2, 3, 4],
        }
    ]
}

response_alerts = {
    "data": [
        {
            "acknowledged": True,
            "campaign_id": 1,
            "campaign": {"id": 1, "name": "Campaign Test"},
            "ctime": 1580852613,
            "cuid": 1,
            "data": {
                "html": "LSASS process injection detected",
                "subject": "Possible mimikatz",
            },
            "event_ids": [7882],
            "id": 645,
            "mtime": None,
            "read": True,
            "tags": None,
            "rule": {"id": 3, "name": "Rule Test"},
            "rule_id": None,
            "vsn": 1,
        }
    ]
}

#!/usr/bin/python
from __future__ import absolute_import, division, print_function

# Copyright: (c) 2022 Fortinet
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

__metaclass__ = type

ANSIBLE_METADATA = {
    "status": ["preview"],
    "supported_by": "community",
    "metadata_version": "1.1",
}

DOCUMENTATION = """
---
module: fortios_wireless_controller_hotspot20_h2qp_advice_of_charge
short_description: Configure advice of charge in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify wireless_controller_hotspot20 feature and h2qp_advice_of_charge category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.0.0
version_added: "2.0.0"
author:
    - Link Zheng (@chillancezen)
    - Jie Xue (@JieX19)
    - Hongbin Lu (@fgtdev-hblu)
    - Frank Shen (@frankshen01)
    - Miguel Angel Munoz (@mamunozgonzalez)
    - Nicolas Thomas (@thomnico)
notes:
    - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

requirements:
    - ansible>=2.9
options:
    access_token:
        description:
            - Token-based authentication.
              Generated from GUI of Fortigate.
        type: str
        required: false
    enable_log:
        description:
            - Enable/Disable logging for task.
        type: bool
        required: false
        default: false
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        type: str
        default: root
    member_path:
        type: str
        description:
            - Member attribute path to operate on.
            - Delimited by a slash character if there are more than one attribute.
            - Parameter marked with member_path is legitimate for doing member operation.
    member_state:
        type: str
        description:
            - Add or delete a member under specified attribute path.
            - When member_state is specified, the state option is ignored.
        choices:
            - 'present'
            - 'absent'

    state:
        description:
            - Indicates whether to create or remove the object.
        type: str
        required: true
        choices:
            - 'present'
            - 'absent'
    wireless_controller_hotspot20_h2qp_advice_of_charge:
        description:
            - Configure advice of charge.
        default: null
        type: dict
        suboptions:
            aoc_list:
                description:
                    - AOC list.
                type: list
                elements: dict
                suboptions:
                    nai_realm:
                        description:
                            - NAI realm list name.
                        type: str
                    nai_realm_encoding:
                        description:
                            - NAI realm encoding.
                        type: str
                    name:
                        description:
                            - Advice of charge ID.
                        required: true
                        type: str
                    plan_info:
                        description:
                            - Plan info.
                        type: list
                        elements: dict
                        suboptions:
                            currency:
                                description:
                                    - Currency code.
                                type: str
                            info_file:
                                description:
                                    - Info file.
                                type: str
                            lang:
                                description:
                                    - Language code.
                                type: str
                            name:
                                description:
                                    - Plan name.
                                required: true
                                type: str
                    type:
                        description:
                            - Usage charge type.
                        type: str
                        choices:
                            - 'time-based'
                            - 'volume-based'
                            - 'time-and-volume-based'
                            - 'unlimited'
            name:
                description:
                    - Plan name.
                required: true
                type: str
"""

EXAMPLES = """
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure advice of charge.
    fortios_wireless_controller_hotspot20_h2qp_advice_of_charge:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      wireless_controller_hotspot20_h2qp_advice_of_charge:
        aoc_list:
         -
            nai_realm: "<your_own_value>"
            nai_realm_encoding: "<your_own_value>"
            name: "default_name_6"
            plan_info:
             -
                currency: "<your_own_value>"
                info_file: "<your_own_value>"
                lang: "<your_own_value>"
                name: "default_name_11"
            type: "time-based"
        name: "default_name_13"

"""

RETURN = """
build:
  description: Build number of the fortigate image
  returned: always
  type: str
  sample: '1547'
http_method:
  description: Last method used to provision the content into FortiGate
  returned: always
  type: str
  sample: 'PUT'
http_status:
  description: Last result given by FortiGate on last operation applied
  returned: always
  type: str
  sample: "200"
mkey:
  description: Master key (id) used in the last call to FortiGate
  returned: success
  type: str
  sample: "id"
name:
  description: Name of the table used to fulfill the request
  returned: always
  type: str
  sample: "urlfilter"
path:
  description: Path of the table used to fulfill the request
  returned: always
  type: str
  sample: "webfilter"
revision:
  description: Internal revision number
  returned: always
  type: str
  sample: "17.0.2.10658"
serial:
  description: Serial number of the unit
  returned: always
  type: str
  sample: "FGVMEVYYQT3AB5352"
status:
  description: Indication of the operation's result
  returned: always
  type: str
  sample: "success"
vdom:
  description: Virtual domain used
  returned: always
  type: str
  sample: "root"
version:
  description: Version of the FortiGate
  returned: always
  type: str
  sample: "v5.6.3"

"""
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import (
    FortiOSHandler,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import (
    check_legacy_fortiosapi,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import (
    schema_to_module_spec,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import (
    check_schema_versioning,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortimanager.common import (
    FAIL_SOCKET_MSG,
)
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.data_post_processor import (
    remove_invalid_fields,
)


def filter_wireless_controller_hotspot20_h2qp_advice_of_charge_data(json):
    option_list = ["aoc_list", "name"]

    json = remove_invalid_fields(json)
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def underscore_to_hyphen(data):
    if isinstance(data, list):
        for i, elem in enumerate(data):
            data[i] = underscore_to_hyphen(elem)
    elif isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            new_data[k.replace("_", "-")] = underscore_to_hyphen(v)
        data = new_data

    return data


def wireless_controller_hotspot20_h2qp_advice_of_charge(data, fos):
    vdom = data["vdom"]

    state = data["state"]

    wireless_controller_hotspot20_h2qp_advice_of_charge_data = data[
        "wireless_controller_hotspot20_h2qp_advice_of_charge"
    ]
    filtered_data = underscore_to_hyphen(
        filter_wireless_controller_hotspot20_h2qp_advice_of_charge_data(
            wireless_controller_hotspot20_h2qp_advice_of_charge_data
        )
    )

    if state == "present" or state is True:
        return fos.set(
            "wireless-controller.hotspot20",
            "h2qp-advice-of-charge",
            data=filtered_data,
            vdom=vdom,
        )

    elif state == "absent":
        return fos.delete(
            "wireless-controller.hotspot20",
            "h2qp-advice-of-charge",
            mkey=filtered_data["name"],
            vdom=vdom,
        )
    else:
        fos._module.fail_json(msg="state must be present or absent!")


def is_successful_status(resp):
    return (
        "status" in resp
        and resp["status"] == "success"
        or "http_status" in resp
        and resp["http_status"] == 200
        or "http_method" in resp
        and resp["http_method"] == "DELETE"
        and resp["http_status"] == 404
    )


def fortios_wireless_controller_hotspot20(data, fos):

    fos.do_member_operation("wireless-controller.hotspot20", "h2qp-advice-of-charge")
    if data["wireless_controller_hotspot20_h2qp_advice_of_charge"]:
        resp = wireless_controller_hotspot20_h2qp_advice_of_charge(data, fos)
    else:
        fos._module.fail_json(
            msg="missing task body: %s"
            % ("wireless_controller_hotspot20_h2qp_advice_of_charge")
        )

    return (
        not is_successful_status(resp),
        is_successful_status(resp)
        and (resp["revision_changed"] if "revision_changed" in resp else True),
        resp,
        {},
    )


versioned_schema = {
    "type": "list",
    "elements": "dict",
    "children": {
        "name": {
            "revisions": {
                "v7.4.0": True,
                "v7.2.4": True,
                "v7.2.2": True,
                "v7.2.1": True,
                "v7.2.0": True,
                "v7.0.8": True,
                "v7.0.7": True,
                "v7.0.6": True,
                "v7.0.5": True,
                "v7.0.4": True,
                "v7.0.3": True,
                "v7.0.2": True,
            },
            "type": "string",
            "required": True,
        },
        "aoc_list": {
            "type": "list",
            "elements": "dict",
            "children": {
                "name": {
                    "revisions": {
                        "v7.4.0": True,
                        "v7.2.4": True,
                        "v7.2.2": True,
                        "v7.2.1": True,
                        "v7.2.0": True,
                        "v7.0.8": True,
                        "v7.0.7": True,
                        "v7.0.6": True,
                        "v7.0.5": True,
                        "v7.0.4": True,
                        "v7.0.3": True,
                        "v7.0.2": True,
                    },
                    "type": "string",
                    "required": True,
                },
                "type": {
                    "revisions": {
                        "v7.4.0": True,
                        "v7.2.4": True,
                        "v7.2.2": True,
                        "v7.2.1": True,
                        "v7.2.0": True,
                        "v7.0.8": True,
                        "v7.0.7": True,
                        "v7.0.6": True,
                        "v7.0.5": True,
                        "v7.0.4": True,
                        "v7.0.3": True,
                        "v7.0.2": True,
                    },
                    "type": "string",
                    "options": [
                        {
                            "value": "time-based",
                            "revisions": {
                                "v7.4.0": True,
                                "v7.2.4": True,
                                "v7.2.2": True,
                                "v7.2.1": True,
                                "v7.2.0": True,
                                "v7.0.8": True,
                                "v7.0.7": True,
                                "v7.0.6": True,
                                "v7.0.5": True,
                                "v7.0.4": True,
                                "v7.0.3": True,
                                "v7.0.2": True,
                            },
                        },
                        {
                            "value": "volume-based",
                            "revisions": {
                                "v7.4.0": True,
                                "v7.2.4": True,
                                "v7.2.2": True,
                                "v7.2.1": True,
                                "v7.2.0": True,
                                "v7.0.8": True,
                                "v7.0.7": True,
                                "v7.0.6": True,
                                "v7.0.5": True,
                                "v7.0.4": True,
                                "v7.0.3": True,
                                "v7.0.2": True,
                            },
                        },
                        {
                            "value": "time-and-volume-based",
                            "revisions": {
                                "v7.4.0": True,
                                "v7.2.4": True,
                                "v7.2.2": True,
                                "v7.2.1": True,
                                "v7.2.0": True,
                                "v7.0.8": True,
                                "v7.0.7": True,
                                "v7.0.6": True,
                                "v7.0.5": True,
                                "v7.0.4": True,
                                "v7.0.3": True,
                                "v7.0.2": True,
                            },
                        },
                        {
                            "value": "unlimited",
                            "revisions": {
                                "v7.4.0": True,
                                "v7.2.4": True,
                                "v7.2.2": True,
                                "v7.2.1": True,
                                "v7.2.0": True,
                                "v7.0.8": True,
                                "v7.0.7": True,
                                "v7.0.6": True,
                                "v7.0.5": True,
                                "v7.0.4": True,
                                "v7.0.3": True,
                                "v7.0.2": True,
                            },
                        },
                    ],
                },
                "nai_realm_encoding": {
                    "revisions": {
                        "v7.4.0": True,
                        "v7.2.4": True,
                        "v7.2.2": True,
                        "v7.2.1": True,
                        "v7.2.0": True,
                        "v7.0.8": True,
                        "v7.0.7": True,
                        "v7.0.6": True,
                        "v7.0.5": True,
                        "v7.0.4": True,
                        "v7.0.3": True,
                        "v7.0.2": True,
                    },
                    "type": "string",
                },
                "nai_realm": {
                    "revisions": {
                        "v7.4.0": True,
                        "v7.2.4": True,
                        "v7.2.2": True,
                        "v7.2.1": True,
                        "v7.2.0": True,
                        "v7.0.8": True,
                        "v7.0.7": True,
                        "v7.0.6": True,
                        "v7.0.5": True,
                        "v7.0.4": True,
                        "v7.0.3": True,
                        "v7.0.2": True,
                    },
                    "type": "string",
                },
                "plan_info": {
                    "type": "list",
                    "elements": "dict",
                    "children": {
                        "name": {
                            "revisions": {
                                "v7.4.0": True,
                                "v7.2.4": True,
                                "v7.2.2": True,
                                "v7.2.1": True,
                                "v7.2.0": True,
                                "v7.0.8": True,
                                "v7.0.7": True,
                                "v7.0.6": True,
                                "v7.0.5": True,
                                "v7.0.4": True,
                                "v7.0.3": True,
                                "v7.0.2": True,
                            },
                            "type": "string",
                            "required": True,
                        },
                        "lang": {
                            "revisions": {
                                "v7.4.0": True,
                                "v7.2.4": True,
                                "v7.2.2": True,
                                "v7.2.1": True,
                                "v7.2.0": True,
                                "v7.0.8": True,
                                "v7.0.7": True,
                                "v7.0.6": True,
                                "v7.0.5": True,
                                "v7.0.4": True,
                                "v7.0.3": True,
                                "v7.0.2": True,
                            },
                            "type": "string",
                        },
                        "currency": {
                            "revisions": {
                                "v7.4.0": True,
                                "v7.2.4": True,
                                "v7.2.2": True,
                                "v7.2.1": True,
                                "v7.2.0": True,
                                "v7.0.8": True,
                                "v7.0.7": True,
                                "v7.0.6": True,
                                "v7.0.5": True,
                                "v7.0.4": True,
                                "v7.0.3": True,
                                "v7.0.2": True,
                            },
                            "type": "string",
                        },
                        "info_file": {
                            "revisions": {
                                "v7.4.0": True,
                                "v7.2.4": True,
                                "v7.2.2": True,
                                "v7.2.1": True,
                                "v7.2.0": True,
                                "v7.0.8": True,
                                "v7.0.7": True,
                                "v7.0.6": True,
                                "v7.0.5": True,
                                "v7.0.4": True,
                                "v7.0.3": True,
                                "v7.0.2": True,
                            },
                            "type": "string",
                        },
                    },
                    "revisions": {
                        "v7.4.0": True,
                        "v7.2.4": True,
                        "v7.2.2": True,
                        "v7.2.1": True,
                        "v7.2.0": True,
                        "v7.0.8": True,
                        "v7.0.7": True,
                        "v7.0.6": True,
                        "v7.0.5": True,
                        "v7.0.4": True,
                        "v7.0.3": True,
                        "v7.0.2": True,
                    },
                },
            },
            "revisions": {
                "v7.4.0": True,
                "v7.2.4": True,
                "v7.2.2": True,
                "v7.2.1": True,
                "v7.2.0": True,
                "v7.0.8": True,
                "v7.0.7": True,
                "v7.0.6": True,
                "v7.0.5": True,
                "v7.0.4": True,
                "v7.0.3": True,
                "v7.0.2": True,
            },
        },
    },
    "revisions": {
        "v7.4.0": True,
        "v7.2.4": True,
        "v7.2.2": True,
        "v7.2.1": True,
        "v7.2.0": True,
        "v7.0.8": True,
        "v7.0.7": True,
        "v7.0.6": True,
        "v7.0.5": True,
        "v7.0.4": True,
        "v7.0.3": True,
        "v7.0.2": True,
    },
}


def main():
    module_spec = schema_to_module_spec(versioned_schema)
    mkeyname = "name"
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "enable_log": {"required": False, "type": "bool", "default": False},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "member_path": {"required": False, "type": "str"},
        "member_state": {
            "type": "str",
            "required": False,
            "choices": ["present", "absent"],
        },
        "state": {"required": True, "type": "str", "choices": ["present", "absent"]},
        "wireless_controller_hotspot20_h2qp_advice_of_charge": {
            "required": False,
            "type": "dict",
            "default": None,
            "options": {},
        },
    }
    for attribute_name in module_spec["options"]:
        fields["wireless_controller_hotspot20_h2qp_advice_of_charge"]["options"][
            attribute_name
        ] = module_spec["options"][attribute_name]
        if mkeyname and mkeyname == attribute_name:
            fields["wireless_controller_hotspot20_h2qp_advice_of_charge"]["options"][
                attribute_name
            ]["required"] = True

    module = AnsibleModule(argument_spec=fields, supports_check_mode=False)
    check_legacy_fortiosapi(module)

    versions_check_result = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        if "access_token" in module.params:
            connection.set_option("access_token", module.params["access_token"])

        if "enable_log" in module.params:
            connection.set_option("enable_log", module.params["enable_log"])
        else:
            connection.set_option("enable_log", False)
        fos = FortiOSHandler(connection, module, mkeyname)
        versions_check_result = check_schema_versioning(
            fos, versioned_schema, "wireless_controller_hotspot20_h2qp_advice_of_charge"
        )

        is_error, has_changed, result, diff = fortios_wireless_controller_hotspot20(
            module.params, fos
        )

    else:
        module.fail_json(**FAIL_SOCKET_MSG)

    if versions_check_result and versions_check_result["matched"] is False:
        module.warn(
            "Ansible has detected version mismatch between FortOS system and your playbook, see more details by specifying option -vvv"
        )

    if not is_error:
        if versions_check_result and versions_check_result["matched"] is False:
            module.exit_json(
                changed=has_changed,
                version_check_warning=versions_check_result,
                meta=result,
                diff=diff,
            )
        else:
            module.exit_json(changed=has_changed, meta=result, diff=diff)
    else:
        if versions_check_result and versions_check_result["matched"] is False:
            module.fail_json(
                msg="Error in repo",
                version_check_warning=versions_check_result,
                meta=result,
            )
        else:
            module.fail_json(msg="Error in repo", meta=result)


if __name__ == "__main__":
    main()

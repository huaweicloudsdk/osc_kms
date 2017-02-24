#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#
import os

from kmclient.common import parsetypes
from kmclient.common.i18n import _
from osc_lib.cli import parseractions


class Key(object):

    @staticmethod
    def add_key_id_arg(parser, op):
        parser.add_argument(
            "key",
            metavar="<key-id>",
            help=_("Key to %s (ID)" % op)
        )

    @staticmethod
    def add_alias_arg(parser):
        parser.add_argument(
            "alias",
            metavar="<alias>",
            help=_("Key alias name, should match regex "
                   "'^[a-zAZ0-9:/_-]{1,255}$', and not end with '/default' "
                   "which has been used by system")
        )

    @staticmethod
    def add_realm_opt(parser):
        parser.add_argument(
            "--realm",
            metavar="<realm>",
            required=True,
            help=_("Realm which key belong to (example: cn-north-1)")
        )

    @staticmethod
    def add_desc_opt(parser):
        parser.add_argument(
            "--description",
            metavar="<description>",
            required=False,
            help=_("Key description (length 0-255)")
        )

    # @staticmethod
    # def add_policy_opt(parser):
    #     parser.add_argument(
    #         "--policy",
    #         metavar="<key-policy>",
    #         required=False,
    #         help=_("Key policy (length 0-255)")
    #     )
    #
    # @staticmethod
    # def add_usage_opt(parser):
    #     parser.add_argument(
    #         "--usage",
    #         metavar="<key-usage>",
    #         required=False,
    #         help=_("Key usage (default: Encrypt_Decrypt)")
    #     )
    #
    # @staticmethod
    # def add_type_opt(parser):
    #     parser.add_argument(
    #         "--type",
    #         metavar="<key-type>",
    #         required=False,
    #         help=_("Key type")
    #     )

    @staticmethod
    def add_days_opt(parser):
        parser.add_argument(
            "--days",
            metavar="<number>",
            required=True,
            type=parsetypes.int_range_type(7, 1096),
            help=_("Delete key after days (number range: 7-1096)")
        )


class Encryption(object):

    @staticmethod
    def add_context_opt(parser):
        parser.add_argument(
            "--context",
            metavar="<key:value>",
            required=False,
            action=parseractions.KeyValueAction,
            help=_("Encryption context "
                   "(Repeat option to set multiple context)")
        )

    @staticmethod
    def add_plain_text_opt(parser):
        parser.add_argument(
            "--plain-text",
            metavar="<text>",
            required=True,
            help=_("DEK plain text + sha256(plain text) in hex")
        )

    @staticmethod
    def add_cipher_text_opt(parser):
        parser.add_argument(
            "--cipher-text",
            metavar="<text>",
            required=True,
            help=_("DEK cipher text + sha256(cipher text) in hex")
        )

    @staticmethod
    def add_key_id_opt(parser):
        parser.add_argument(
            "--key",
            metavar="<key-id>",
            required=True,
            help=_("Key used for encrypt/decrypt (ID)")
        )

    @staticmethod
    def add_no_plain_text_opt(parser):
        parser.add_argument(
            "--no-plain-text",
            required=False,
            default=False,
            action="store_true",
            help=_("Do not show plain text")
        )
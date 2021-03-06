# -*-coding:utf-8-*-
#
# Copyright 2020. Huawei Technologies Co., Ltd. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from src import push_admin
import json
from src.push_admin import messaging
from examples import push_env

headers = {messaging.APNsHeader.HEAD_APNs_ID: "6532dc0e-f581-7bfb-e1ab-60ec3cecea73"}

apns_alert = messaging.APNsAlert(title="HMS Push Title",
                                 body="HMS Push Body",
                                 launch_image="Default.png",
                                 custom_data={"k1": "v1", "k2": "v2"})

apns_payload_aps = messaging.APNsAps(alert=apns_alert,
                                     badge=1,
                                     sound="wtewt.mp4",
                                     content_available=True,
                                     category="category",
                                     thread_id="id")

payload = messaging.APNsPayload(aps=apns_payload_aps,
                                acme_account="jane.appleseed@apple.com",
                                acme_message="message123456")

apns_hms_options = messaging.APNsHMSOptions(target_user_type=1)

apns_push_config = messaging.APNsConfig(headers=headers,
                                        payload=payload,
                                        apns_hms_options=apns_hms_options)


def send_apns_push_message():
    """
    a sample to show hwo to send web push message
    :return:
    """
    message = messaging.Message(
        apns=apns_push_config,
        token=[push_env.test_device_token]
    )

    try:
        response = messaging.send_message(message)
        print("response is ", json.dumps(vars(response)))
        assert (response.code == '80000000')
    except Exception as e:
        print(repr(e))


def init_app():
    """init sdk app"""
    app_id = push_env.app_id
    app_secret = push_env.app_secret
    push_admin.initialize_app(app_id, app_secret)


def main():
    init_app()
    send_apns_push_message()


if __name__ == '__main__':
    main()

import allure
import json


def attach_snapshot_result(snapshot: dict) -> None:
    try:
        allure.attach(json.dumps(snapshot, indent=4, ensure_ascii=False),
                      name='snapshot',
                      attachment_type=allure.attachment_type.JSON)
    except json.decoder.JSONDecodeError as err:
        print(err)

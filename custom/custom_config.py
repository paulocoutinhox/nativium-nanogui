import os


# -----------------------------------------------------------------------------
def run(params):
    return [
        {
            "type": "remove-dir",
            "path": os.path.join("modules", "tests"),
        },
        {
            "type": "remove-dir",
            "path": os.path.join("modules", "app-core"),
        },
        {
            "type": "remove-dir",
            "path": os.path.join("modules", "app-main"),
        },
        {
            "type": "remove-dir",
            "path": os.path.join("modules", "app-wasm"),
        },
        {
            "type": "symlink",
            "source": os.path.join("modules", "app-core"),
            "target": os.path.join("modules", "app-core"),
        },
        {
            "type": "symlink",
            "source": os.path.join("modules", "app-main"),
            "target": os.path.join("modules", "app-main"),
        },
        {
            "type": "copy-dir",
            "source": "targets",
            "target": "targets",
        },
        {
            "type": "replace-text",
            "path": "core/const.py",
            "list": [
                {
                    "old": 'BUCKET_NAME = "nativium"',
                    "new": 'BUCKET_NAME = "nativium-nanogui"',
                },
            ],
        },
        {
            "type": "replace-text",
            "path": "targets/linux/config/target.py",
            "list": [
                {
                    "old": '["Debug", "Release"]',
                    "new": '["Release"]',
                },
                {
                    "old": '"assets_dir": ""',
                    "new": '"assets_dir": "modules/app-main/resources"',
                },
            ],
        },
        {
            "type": "replace-text",
            "path": "targets/macos/config/target.py",
            "list": [
                {
                    "old": '["Debug", "Release"]',
                    "new": '["Release"]',
                },
                {
                    "old": '"assets_dir": ""',
                    "new": '"assets_dir": "modules/app-main/resources"',
                },
                {
                    "old": '"min_version": "10.9",',
                    "new": '"min_version": "10.15",',
                },
            ],
        },
        {
            "type": "replace-text",
            "path": "targets/windows/config/target.py",
            "list": [
                {
                    "old": '["Debug", "Release"]',
                    "new": '["Release"]',
                },
                {
                    "old": '"assets_dir": ""',
                    "new": '"assets_dir": "modules/app-main/resources"',
                },
            ],
        },
        {
            "type": "replace-text",
            "path": "targets/wasm/config/target.py",
            "list": [
                {
                    "old": '"product_name": "Nativium"',
                    "new": '"product_name": "Nativium - NanoGUI"',
                },
                {
                    "old": '["Debug", "Release"]',
                    "new": '["Release"]',
                },
                {
                    "old": '"publish_bucket_name": "nativium"',
                    "new": '"publish_bucket_name": "nativium-nanogui"',
                },
                {
                    "old": '"url": "https://nativium.',
                    "new": '"url": "https://nativium-nanogui.',
                },
            ],
        },
    ]

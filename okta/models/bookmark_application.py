# flake8: noqa
"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from okta.models.application\
    import Application
from okta.models import bookmark_application_settings\
    as bookmark_application_settings
from okta.models import ApplicationSignOnMode


class BookmarkApplication(
    Application
):
    """
    A class for BookmarkApplication objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.sign_on_mode = ApplicationSignOnMode("BOOKMARK")
            self.name = config["name"]\
                if "name" in config else "bookmark"
            if "settings" in config:
                if isinstance(config["settings"],
                              bookmark_application_settings.BookmarkApplicationSettings):
                    self.settings = config["settings"]
                elif config["settings"] is not None:
                    self.settings = bookmark_application_settings.BookmarkApplicationSettings(
                        config["settings"]
                    )
                else:
                    self.settings = None
            else:
                self.settings = None
        else:
            self.name = "bookmark"
            self.settings = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "name": self.name,
            "settings": self.settings
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format

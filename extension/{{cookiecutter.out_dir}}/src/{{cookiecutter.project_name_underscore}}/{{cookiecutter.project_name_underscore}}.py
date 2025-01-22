from enum import Enum
from typing import Any, Optional

from flet.core.constrained_control import ConstrainedControl
from flet.core.control import OptionalNumber

class {{cookiecutter.control_name}}(ConstrainedControl):
    """
    {{cookiecutter.control_name}} Control.
    """

    def __init__(
        self,
        #
        # Control
        #
        opacity: OptionalNumber = None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        data: Any = None,
        #
        # ConstrainedControl
        #
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        #
        # {{cookiecutter.control_name}} specific
        #
        value: Optional[str] = None,
    ):
        ConstrainedControl.__init__(
            self,
            tooltip=tooltip,
            opacity=opacity,
            visible=visible,
            data=data,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )

        self.value = value

    def _get_control_name(self):
        return "{{cookiecutter.project_name_underscore}}"

    # value
    @property
    def value(self):
        return self._get_attr("value")

    @value.setter
    def value(self, value):
        self._set_attr("value", value)

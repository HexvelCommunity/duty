from __future__ import annotations

import dataclasses
import os
import typing

import pretty_errors
import typing_extensions as tye

exceptions_storage: typing.Dict[int, typing.Type[APIError]] = {}

pretty_errors.configure(
    separator_character="#",
    display_timestamp=True,
    filename_display=pretty_errors.default_config.exception_color,
    line_number_first=True,
    display_link=True,
    lines_before=5,
    lines_after=2,
    line_color=pretty_errors.RED + "> " + pretty_errors.default_config.line_color,
    code_color="  " + pretty_errors.default_config.exception_color,
    truncate_code=True,
    display_locals=True,
)


class ExceptionWriter(pretty_errors.ExceptionWriter):
    def write_header(self):
        padding_symbol = "#"
        error_text = " API ERROR "
        terminal_width = os.get_terminal_size().columns
        total_length = len(error_text)
        padding_needed = (terminal_width - total_length) // 2
        centered_message = (
            pretty_errors.RED
            + (padding_symbol * padding_needed)
            + error_text
            + (padding_symbol * padding_needed)
        )

        if len(centered_message) < terminal_width:
            centered_message += padding_symbol

        self.output_text(pretty_errors.RED + centered_message)


pretty_errors.exception_writer = ExceptionWriter()


class _ParamsScheme(tye.TypedDict):
    key: str
    value: str


@dataclasses.dataclass
class APIError(Exception):
    description: str
    status_code: int
    request_params: typing.List[_ParamsScheme]
    extra_fields: dict

    def __class_getitem__(
        cls, code: typing.Union[int, typing.Tuple[int, Ellipsis]]
    ) -> typing.Tuple[typing.Type[APIError]]:
        result_classes = []
        codes = (code,) if isinstance(code, int) else code
        for code in codes:
            if code in exceptions_storage:
                result_classes.append(exceptions_storage[code])
            else:
                new_class = type(f"APIError [{code}]", (APIError,), {})
                new_class = typing.cast(typing.Type[APIError], new_class)
                exceptions_storage[code] = new_class
                result_classes.append(new_class)

        return tuple(result_classes)

    def __str__(self) -> str:
        return self.description

    def __repr__(self) -> str:
        return self.description

from __future__ import annotations

from typing import TYPE_CHECKING

from rich.align import Align
from rich.table import Table
from rich.pretty import Pretty
from rich.console import Console
from rich.progress import (
    Progress,
    BarColumn,
    TextColumn,
    SpinnerColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)


if TYPE_CHECKING:
    from collections.abc import Mapping, Iterable

    from rich.progress import ProgressType


class CustomConsole(Console):
    def track(
        self,
        sequence: Iterable[ProgressType],
        description: str = "Working...",
        total: int | None = None,
        transient: bool = False,
    ) -> Iterable[ProgressType]:
        columns = [
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn(
                "[progress.percentage]{task.completed}/{task.total:.0f} "
                "({task.percentage:>3.0f}%)",
            ),
            TextColumn("Elapsed:"),
            TimeElapsedColumn(),
            TextColumn("Remaining:"),
            TimeRemainingColumn(),
        ]
        progress = Progress(
            *columns,
            console=self,
            transient=transient,
        )

        with progress:
            yield from progress.track(sequence, total=total, description=description)

    def print_table(
        self,
        title: str,
        columns: list[str],
        rows: list[list[str]],
    ) -> None:
        table = Table(title=title)

        for idx, column in enumerate(columns):
            table.add_column(column, justify="left" if idx == 0 else "right")

        for row in rows:
            table.add_row(*row)

        self.print(Align.center(table))

    def print_dict(self, data: Mapping[str, str | float | int]) -> None:
        self.print(Pretty(data))

    def print_divider(self, title: str) -> None:
        self.print()
        self.print()
        self.rule(title)


console = CustomConsole(width=80)


"""Museum artifact catalog demonstration."""

import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE artifacts ("
    "id INTEGER PRIMARY KEY, title TEXT, era TEXT, "
    "value INTEGER, on_display INTEGER)"
)


def add_artifact(title, era, value, on_display=0):
    """Register a new artifact in the catalog."""
    conn.execute(
        "INSERT INTO artifacts (title, era, value, on_display) "
        "VALUES (?, ?, ?, ?)",
        (title, era, value, on_display)
    )
    conn.commit()


def display_status(artifact_id, _curator):
    """Return the display status of an artifact."""
    row = conn.execute(
        "SELECT on_display FROM artifacts WHERE id = ?",
        (artifact_id,)
    ).fetchone()

    if row[0] == 1:
        return "on display"
    return "in storage"


def total_value(era):
    """Calculate the total value of artifacts from an era."""
    total = 0
    for (value,) in conn.execute(
        "SELECT value FROM artifacts WHERE era = ?", (era,)
    ):
        total += value
    return total


def move_to_display(artifact_id):
    """Move an artifact onto display."""
    conn.execute(
        "UPDATE artifacts SET on_display = 1 WHERE id = ?",
        (artifact_id,)
    )
    conn.commit()


def backup_note():
    """Print a catalog backup notification."""
    print("catalog backup complete")


def main():
    """Run the museum catalog demonstration."""
    add_artifact("Bronze Mirror", "Chola", 120000)
    add_artifact("Palm Manuscript", "Vijayanagara", 80000, 1)
    add_artifact("Terracotta Lamp", "Chola", 15000)
    move_to_display(1)

    print(display_status(1, "Dr. Rao"))
    print(total_value("Chola"))
    backup_note()


if __name__ == "__main__":
    main()

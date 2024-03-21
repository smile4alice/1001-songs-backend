"""add song and genre tables

Revision ID: 64820a3923c0
Revises: bd48ab4069b5
Create Date: 2024-02-11 02:43:06.258338

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "64820a3923c0"
down_revision: Union[str, None] = "bd48ab4069b5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "genre",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("genre_name", sa.String(length=50), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "song",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("title", sa.String(length=200), nullable=True),
        sa.Column("recording_date", sa.Date(), nullable=True),
        sa.Column("performers", sa.String(length=200), nullable=True),
        sa.Column("collectors", sa.ARRAY(sa.String(length=100)), nullable=True),
        sa.Column("source", sa.String(length=200), nullable=True),
        sa.Column("archive", sa.String(length=255), nullable=True),
        sa.Column("researcher_comment", sa.String(length=1000), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "song_genre_association",
        sa.Column("song_id", sa.Integer(), nullable=False),
        sa.Column("genre_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["genre_id"],
            ["genre.id"],
        ),
        sa.ForeignKeyConstraint(
            ["song_id"],
            ["song.id"],
        ),
        sa.PrimaryKeyConstraint("song_id", "genre_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("song_genre_association")
    op.drop_table("song")
    op.drop_table("genre")
    # ### end Alembic commands ###
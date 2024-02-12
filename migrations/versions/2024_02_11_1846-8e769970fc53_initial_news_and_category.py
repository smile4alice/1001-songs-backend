"""initial news and category

Revision ID: 8e769970fc53
Revises: 263822c5246a
Create Date: 2024-02-11 18:46:31.340798

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8e769970fc53"
down_revision: Union[str, None] = "263822c5246a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "news_category",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "news",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=250), nullable=False),
        sa.Column("content", sa.String(length=10000), nullable=False),
        sa.Column("authors", sa.ARRAY(sa.String(length=100)), nullable=True),
        sa.Column("editors", sa.ARRAY(sa.String(length=100)), nullable=True),
        sa.Column("photographers", sa.ARRAY(sa.String(length=100)), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["category_id"],
            ["news_category.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("news")
    op.drop_table("news_category")
    # ### end Alembic commands ###

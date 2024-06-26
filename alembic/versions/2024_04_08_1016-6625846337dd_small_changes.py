"""Small Changes

Revision ID: 6625846337dd
Revises: 75f073ed97dd
Create Date: 2024-04-08 10:16:16.106632

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6625846337dd"
down_revision: Union[str, None] = "75f073ed97dd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("currency", sa.Column("symbol", sa.String(), nullable=False))
    op.drop_constraint("currency_name_key", "currency", type_="unique")
    op.create_index(
        op.f("ix_currency_symbol"), "currency", ["symbol"], unique=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_currency_symbol"), table_name="currency")
    op.create_unique_constraint("currency_name_key", "currency", ["name"])
    op.drop_column("currency", "symbol")
    # ### end Alembic commands ###

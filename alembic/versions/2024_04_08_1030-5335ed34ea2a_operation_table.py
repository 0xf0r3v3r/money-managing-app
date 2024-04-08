"""Operation Table

Revision ID: 5335ed34ea2a
Revises: 6625846337dd
Create Date: 2024-04-08 10:30:49.045078

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5335ed34ea2a"
down_revision: Union[str, None] = "6625846337dd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "operation",
        sa.Column("summ", sa.Float(), nullable=False),
        sa.Column("time_date", sa.DateTime(), nullable=False),
        sa.Column("type", sa.Boolean(), nullable=False),
        sa.Column("note", sa.String(), nullable=True),
        sa.Column("fk_account_id", sa.Integer(), nullable=False),
        sa.Column("fk_category_id", sa.Integer(), nullable=False),
        sa.Column("fk_sub_category_id", sa.Integer(), nullable=False),
        sa.Column("fk_user_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.ForeignKeyConstraint(
            ["fk_account_id"],
            ["account.id"],
        ),
        sa.ForeignKeyConstraint(
            ["fk_category_id"],
            ["category.id"],
        ),
        sa.ForeignKeyConstraint(
            ["fk_sub_category_id"],
            ["subcategory.id"],
        ),
        sa.ForeignKeyConstraint(
            ["fk_user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_operation_id"), "operation", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_operation_id"), table_name="operation")
    op.drop_table("operation")
    # ### end Alembic commands ###
"""update models

Revision ID: 968a96350a69
Revises: 4d69e1dc54d4
Create Date: 2024-02-29 13:09:45.992978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '968a96350a69'
down_revision = '4d69e1dc54d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inquiries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('inquiry', sa.String(), nullable=False),
    sa.Column('submitted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subscriptions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('subscribed_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('sub')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sub',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), nullable=False),
    sa.Column('subscribed_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('subscriptions')
    op.drop_table('inquiries')
    # ### end Alembic commands ###

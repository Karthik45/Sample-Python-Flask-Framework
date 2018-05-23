"""empty message

Revision ID: 23b8b098c9d6
Revises: 5edd7ec46f44
Create Date: 2018-05-23 14:02:21.507730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23b8b098c9d6'
down_revision = '5edd7ec46f44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leaves',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('leaveType', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('from_date', sa.DateTime(), nullable=False),
    sa.Column('to_date', sa.DateTime(), nullable=False),
    sa.Column('num_of_days', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('leave_status', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('modified_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['leaveType'], ['leaves_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('leaves')
    # ### end Alembic commands ###
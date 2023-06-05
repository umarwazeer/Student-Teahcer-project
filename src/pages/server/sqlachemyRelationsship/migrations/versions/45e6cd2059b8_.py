"""empty message

Revision ID: 45e6cd2059b8
Revises: 392ba218107e
Create Date: 2023-06-02 15:50:27.388699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45e6cd2059b8'
down_revision = '392ba218107e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(length=200), nullable=True))
        batch_op.alter_column('emp_name',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=100),
               existing_nullable=True)
        batch_op.alter_column('emp_id',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=10),
               existing_nullable=True)
        batch_op.create_unique_constraint(None, ['emp_id'])
        batch_op.drop_column('emp_age')
        batch_op.drop_column('emp_email')
        batch_op.drop_column('emp_image')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.add_column(sa.Column('emp_image', sa.VARCHAR(length=255), nullable=True))
        batch_op.add_column(sa.Column('emp_email', sa.VARCHAR(length=255), nullable=True))
        batch_op.add_column(sa.Column('emp_age', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('emp_id',
               existing_type=sa.String(length=10),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
        batch_op.alter_column('emp_name',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
        batch_op.drop_column('image')

    # ### end Alembic commands ###

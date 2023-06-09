"""empty message

Revision ID: e1f1dd84d8b2
Revises: fed6da5a11e4
Create Date: 2023-06-11 16:21:30.991406

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e1f1dd84d8b2'
down_revision = 'fed6da5a11e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_info')
    with op.batch_alter_table('t_friend', schema=None) as batch_op:
        batch_op.drop_column('top')
        batch_op.drop_column('remark')
        batch_op.drop_column('black')

    with op.batch_alter_table('t_user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nickname', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('avatar', sa.String(length=500), nullable=True))
        batch_op.add_column(sa.Column('gender', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('mobile', sa.String(length=11), nullable=True))
        batch_op.add_column(sa.Column('email', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('note', sa.String(length=500), nullable=True))
        batch_op.add_column(sa.Column('is_active', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t_user', schema=None) as batch_op:
        batch_op.drop_column('is_active')
        batch_op.drop_column('note')
        batch_op.drop_column('email')
        batch_op.drop_column('mobile')
        batch_op.drop_column('gender')
        batch_op.drop_column('avatar')
        batch_op.drop_column('nickname')

    with op.batch_alter_table('t_friend', schema=None) as batch_op:
        batch_op.add_column(sa.Column('black', mysql.SMALLINT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('remark', mysql.VARCHAR(length=126), nullable=True))
        batch_op.add_column(sa.Column('top', mysql.SMALLINT(), autoincrement=False, nullable=True))

    op.create_table('t_info',
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('nickname', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('avatar', mysql.VARCHAR(length=500), nullable=True),
    sa.Column('gender', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('mobile', mysql.VARCHAR(length=11), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('note', mysql.VARCHAR(length=500), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['t_user.id'], name='t_info_ibfk_1'),
    sa.PrimaryKeyConstraint('user_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###

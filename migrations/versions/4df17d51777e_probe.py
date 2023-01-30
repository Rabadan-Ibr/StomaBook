"""Probe

Revision ID: 4df17d51777e
Revises: 
Create Date: 2023-01-28 17:21:52.208600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4df17d51777e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_clients_id'), 'clients', ['id'], unique=False)
    op.create_table('diagnoses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('detail', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_diagnoses_id'), 'diagnoses', ['id'], unique=False)
    op.create_table('procedures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('detail', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_procedures_id'), 'procedures', ['id'], unique=False)
    op.create_table('teeth',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_teeth_id'), 'teeth', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=False),
    sa.Column('role', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('receptions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_date', sa.DateTime(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.Column('doctor_id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['doctor_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_receptions_id'), 'receptions', ['id'], unique=False)
    op.create_table('diag_reception',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('diag_id', sa.Integer(), nullable=False),
    sa.Column('reception_id', sa.Integer(), nullable=False),
    sa.Column('tooth_id', sa.Integer(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['diag_id'], ['diagnoses.id'], ),
    sa.ForeignKeyConstraint(['reception_id'], ['receptions.id'], ),
    sa.ForeignKeyConstraint(['tooth_id'], ['teeth.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_diag_reception_id'), 'diag_reception', ['id'], unique=False)
    op.create_table('proc_reception',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('proc_id', sa.Integer(), nullable=False),
    sa.Column('reception_id', sa.Integer(), nullable=False),
    sa.Column('tooth_id', sa.Integer(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['proc_id'], ['procedures.id'], ),
    sa.ForeignKeyConstraint(['reception_id'], ['receptions.id'], ),
    sa.ForeignKeyConstraint(['tooth_id'], ['teeth.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_proc_reception_id'), 'proc_reception', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_proc_reception_id'), table_name='proc_reception')
    op.drop_table('proc_reception')
    op.drop_index(op.f('ix_diag_reception_id'), table_name='diag_reception')
    op.drop_table('diag_reception')
    op.drop_index(op.f('ix_receptions_id'), table_name='receptions')
    op.drop_table('receptions')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_teeth_id'), table_name='teeth')
    op.drop_table('teeth')
    op.drop_index(op.f('ix_procedures_id'), table_name='procedures')
    op.drop_table('procedures')
    op.drop_index(op.f('ix_diagnoses_id'), table_name='diagnoses')
    op.drop_table('diagnoses')
    op.drop_index(op.f('ix_clients_id'), table_name='clients')
    op.drop_table('clients')
    # ### end Alembic commands ###

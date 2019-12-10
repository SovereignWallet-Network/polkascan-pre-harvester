"""Added council motion tables

Revision ID: 213043ea4c8f
Revises: a2fc0a403498
Create Date: 2019-12-09 18:24:06.750411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '213043ea4c8f'
down_revision = 'a2fc0a403498'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data_council_motion',
    sa.Column('motion_hash', sa.String(length=64), nullable=False),
    sa.Column('proposal_id', sa.Integer(), nullable=True),
    sa.Column('proposal_hash', sa.String(length=64), nullable=True),
    sa.Column('proposal', sa.JSON(), nullable=True),
    sa.Column('member_threshold', sa.Integer(), nullable=False),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.Column('executed', sa.Boolean(), nullable=True),
    sa.Column('created_at_block', sa.Integer(), nullable=False),
    sa.Column('updated_at_block', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('motion_hash')
    )
    op.create_table('data_council_motion_audit',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('motion_hash', sa.String(length=64), nullable=True),
    sa.Column('block_id', sa.Integer(), nullable=False),
    sa.Column('extrinsic_idx', sa.Integer(), nullable=True),
    sa.Column('event_idx', sa.Integer(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('data', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_data_council_motion_audit_block_id'), 'data_council_motion_audit', ['block_id'], unique=False)
    op.create_table('data_council_vote',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('motion_hash', sa.String(length=64), nullable=True),
    sa.Column('account_id', sa.String(length=64), nullable=True),
    sa.Column('vote', sa.Boolean(), nullable=True),
    sa.Column('yes_votes_count', sa.Integer(), nullable=False),
    sa.Column('no_votes_count', sa.Integer(), nullable=False),
    sa.Column('created_at_block', sa.Integer(), nullable=False),
    sa.Column('updated_at_block', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_data_council_vote_account_id'), 'data_council_vote', ['account_id'], unique=False)
    op.create_index(op.f('ix_data_council_vote_motion_hash'), 'data_council_vote', ['motion_hash'], unique=False)
    op.create_table('data_council_vote_audit',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('motion_hash', sa.String(length=64), nullable=True),
    sa.Column('block_id', sa.Integer(), nullable=False),
    sa.Column('extrinsic_idx', sa.Integer(), nullable=True),
    sa.Column('event_idx', sa.Integer(), nullable=True),
    sa.Column('data', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_data_council_vote_audit_block_id'), 'data_council_vote_audit', ['block_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_data_council_vote_audit_block_id'), table_name='data_council_vote_audit')
    op.drop_table('data_council_vote_audit')
    op.drop_index(op.f('ix_data_council_vote_motion_hash'), table_name='data_council_vote')
    op.drop_index(op.f('ix_data_council_vote_account_id'), table_name='data_council_vote')
    op.drop_table('data_council_vote')
    op.drop_index(op.f('ix_data_council_motion_audit_block_id'), table_name='data_council_motion_audit')
    op.drop_table('data_council_motion_audit')
    op.drop_table('data_council_motion')
    # ### end Alembic commands ###

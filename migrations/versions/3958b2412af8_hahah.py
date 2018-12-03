"""hahah

Revision ID: 3958b2412af8
Revises: 
Create Date: 2018-11-27 00:53:24.581437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3958b2412af8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('info_adminuser',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('card_name', sa.String(length=64), nullable=False),
    sa.Column('card_avatar', sa.String(length=64), nullable=False),
    sa.Column('card_about', sa.String(length=64), nullable=False),
    sa.Column('card_job', sa.String(length=64), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=False),
    sa.Column('keywords', sa.String(length=256), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('qq', sa.String(length=32), nullable=False),
    sa.Column('wxid', sa.String(length=64), nullable=False),
    sa.Column('wxcode', sa.String(length=64), nullable=False),
    sa.Column('butoom_title', sa.String(length=64), nullable=False),
    sa.Column('beian', sa.String(length=64), nullable=False),
    sa.Column('logo_name', sa.String(length=64), nullable=False),
    sa.Column('logo_image', sa.String(length=64), nullable=False),
    sa.Column('about_me', sa.Text(), nullable=False),
    sa.Column('tags', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('info_category',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('info_gbook',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip', sa.String(length=32), nullable=True),
    sa.Column('replyName', sa.String(length=16), nullable=True),
    sa.Column('beReplyName', sa.String(length=16), nullable=True),
    sa.Column('email', sa.String(length=32), nullable=True),
    sa.Column('browser', sa.String(length=16), nullable=True),
    sa.Column('os_name', sa.String(length=16), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('son_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['son_id'], ['info_gbook.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8mb4'
    )
    op.create_table('info_link',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('url', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8mb4'
    )
    op.create_table('info_user',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nick_name', sa.String(length=32), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('mobile', sa.String(length=11), nullable=False),
    sa.Column('avatar_url', sa.String(length=256), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('signature', sa.String(length=512), nullable=True),
    sa.Column('gender', sa.Enum('MAN', 'WOMAN'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mobile'),
    sa.UniqueConstraint('nick_name')
    )
    op.create_table('info_news',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('source', sa.String(length=64), nullable=False),
    sa.Column('digest', sa.String(length=512), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('clicks', sa.Integer(), nullable=True),
    sa.Column('index_image_url', sa.String(length=256), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('like_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['info_category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8mb4'
    )
    op.create_table('info_comment',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('news_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('like_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['news_id'], ['info_news.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['parent_id'], ['info_comment.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8mb4'
    )
    op.create_table('info_news_action',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('news_id', sa.Integer(), nullable=True),
    sa.Column('is_banner', sa.Boolean(), nullable=True),
    sa.Column('is_top', sa.Boolean(), nullable=True),
    sa.Column('is_tuijian', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['news_id'], ['info_news.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('info_news_action')
    op.drop_table('info_comment')
    op.drop_table('info_news')
    op.drop_table('info_user')
    op.drop_table('info_link')
    op.drop_table('info_gbook')
    op.drop_table('info_category')
    op.drop_table('info_adminuser')
    # ### end Alembic commands ###

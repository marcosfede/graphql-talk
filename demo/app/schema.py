from graphene_django import DjangoObjectType
import graphene
from .models import Comment, Post, User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    comments = graphene.List(CommentType)
    posts = graphene.List(PostType)

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_comments(self, info):
        return Comment.objects.all()

    def resolve_posts(self, info):
        return Post.objects.all()


# schema = graphene.Schema(query=Query)


class CreateComment(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)
        user = graphene.ID(required=True)
        post = graphene.ID(required=True)

    ok = graphene.Boolean()
    comment = graphene.Field(lambda: CommentType)

    def mutate(self, info, text, user, post):
        comment = Comment(text=text, user_id=user, post_id=post)
        comment.save()
        ok = True
        return CreateComment(comment=comment, ok=ok)


class Mutations(graphene.ObjectType):
    create_comment = CreateComment.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)

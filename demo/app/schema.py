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

    user = graphene.Field(UserType, id=graphene.Int())
    post = graphene.Field(PostType, id=graphene.Int())
    comment = graphene.Field(CommentType, id=graphene.Int())

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_comments(self, info):
        return Comment.objects.all()

    def resolve_posts(self, info):
        return Post.objects.all()

    def resolve_post(self, info, id):
        return Post.objects.get(id=id)

    def resolve_user(self, info, id):
        return User.objects.get(id=id)

    def resolve_comment(self, info, id):
        return Comment.objects.get(id=id)

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

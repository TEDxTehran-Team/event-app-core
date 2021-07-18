import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphql_jwt.decorators import login_required

from apps.accounts.forms import ProfileForm
from apps.accounts.schema import UserNode

class ProfileMutation(DjangoModelFormMutation):
    user = graphene.Field(UserNode)

    @classmethod
    def get_form_kwargs(cls, root, info, **input):
        return {
            **super().get_form_kwargs(root, info, **input),
            'instance': info.context.user,
        }

    @classmethod
    @login_required
    def mutate(cls, root, info, input):
        return super().mutate(root, info, input)

    class Meta:
        form_class = ProfileForm

class AccountsMutation(graphene.ObjectType):
    update_profile = ProfileMutation.Field()

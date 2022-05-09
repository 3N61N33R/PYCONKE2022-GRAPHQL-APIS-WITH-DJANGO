
# Type

# Query

# Input

# CRUD Mutation

# Mutation
# reqister our queries and mutations with graphene

import graphene

from graphene_django import DjangoObjectType
from .models import Workshop

class WorkshopType(DjangoObjectType):
    class Meta:
        model = Workshop
        fields = "__all__"

class Query(graphene.ObjectType):
    all_workshops = graphene.List(WorkshopType)
    workshop = graphene.Field(WorkshopType, workshop_id=graphene.Int())

    def resolve_all_workshops(self, info, **kwargs):
        return Workshop.objects.all()

    def resolve_workshop(self, info, workshop_id):
        return Workshop.objects.get(pk=workshop_id)

class WorkshopInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    speaker = graphene.String()
    location = graphene.String()

class CreateWorkshop(graphene.Mutation):
    class Arguments:
        data = WorkshopInput(required=True)

    workshop = graphene.Field(WorkshopType)

    @staticmethod
    def mutate(root, info, data=None):
        workshop_instance = Workshop(
            title=data.title,
            speaker=data.speaker,
            location=data.location,
            
        )
        workshop_instance.save()
        return CreateWorkshop(workshop=workshop_instance)

class UpdateWorkshop(graphene.Mutation):
    class Arguments:
        data = WorkshopInput(required=True)

    workshop = graphene.Field(WorkshopType)

    @staticmethod
    def mutate(root, info, data=None):

        workshop_instance = Workshop.objects.get(pk=data.id)

        if workshop_instance:
            workshop_instance.title = data.title
            workshop_instance.speaker = data.speaker
            workshop_instance.location = data.location
            workshop_instance.save()

            return UpdateWorkshop(workshop=workshop_instance)
        return UpdateWorkshop(workshop=None)

class DeleteWorkshop(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    workshop = graphene.Field(WorkshopType)


    @staticmethod
    def mutate(root, info, id):
        workshop_instance = Workshop.objects.get(pk=id)
        workshop_instance.delete()

        return None

class Mutation(graphene.ObjectType):
    create_workshop = CreateWorkshop.Field()
    update_workshop = UpdateWorkshop.Field()
    delete_workshop = DeleteWorkshop.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

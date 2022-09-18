import graphene
from graphene_federation import build_schema
from uaa.schema import Query as Query_view
from uaa.schema import Mutation as Mutation_view

# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = build_schema(query=Query_view, mutation=Mutation_view)

#https://django-graphql-auth.readthedocs.io/en/latest/quickstart/
# a graphql-auth link i used to implement uaa-graph
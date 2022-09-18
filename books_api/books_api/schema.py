import graphene
from graphene_federation import build_schema

from api.schema import Query as Query_view
from api.schema import Mutation as Mutation_view

schema = build_schema(query=Query_view, mutation=Mutation_view)
import datetime
from haystack import indexes
from app.models import Imp

class CustomerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    incoterm = indexes.CharField(model_attr='incoterm')
    descricao_do_produto = indexes.CharField(model_attr='descricao_do_produto')
    qtd_comercial_field = indexes.CharField(model_attr='qtd_comercial_field')
    cod_ncm = indexes.CharField(model_attr='cod_ncm')

    
    def get_model(self):
        return Imp
 
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
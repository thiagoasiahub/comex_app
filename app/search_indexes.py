import datetime
from haystack import indexes
from app.models import Imp

class CustomerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    incoterm = indexes.CharField(model_attr='incoterm')
    descricao_do_produto = indexes.CharField(model_attr='descricao_do_produto')
    valor_un_prod_dolar = indexes.CharField(model_attr='valor_un_prod_dolar')
    unidade_comerc_field = indexes.CharField(model_attr='unidade_comerc_field')
    qtd_comercial_field = indexes.CharField(model_attr='qtd_comercial_field')
    anomes = indexes.CharField(model_attr='anomes')
    cod_ncm = indexes.CharField(model_attr='cod_ncm')
    descricao_do_codigo_ncm = indexes.CharField(model_attr='descricao_do_codigo_ncm')

    
    def get_model(self):
        return Imp
 
    def index_queryset(self, using=None):
        return self.get_model().objects.all()